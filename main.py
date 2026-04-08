import os
import pandas as pd
import numpy as np
from statsmodels.tsa.filters.hp_filter import hpfilter
from src.data_loader import SocioEconomicDataLoader
from src.models import ISPCMR, ADBTERU
from src.visualizer import MacroVisualizer

def calculate_output_gap(df):
    """Calcula o Hiato do Produto usando o Filtro HP."""
    if 'Real_GDP_Q' in df.columns:
        gdp = df['Real_GDP_Q'].dropna()
        if len(gdp) > 20:
            cycle, trend = hpfilter(np.log(gdp), lamb=1600)
            gap = (np.exp(cycle) - 1) * 100
            return pd.Series(gap, index=gdp.index)
    return pd.Series(dtype=float)

def calculate_derived_variables(df):
    """Calcula variáveis derivadas (Juros Real, Câmbio Real, etc.)."""
    # 1. Taxa de Juros Real (i - pi)
    if 'Policy_Rate' in df.columns and 'CPI_YoY' in df.columns:
        df['Real_Interest_Rate'] = df['Policy_Rate'] - df['CPI_YoY']
    
    # 2. Taxa de Câmbio Real (q = E * P_us / P_kor)
    if 'Exchange_Rate' in df.columns and 'CPI_Index_USA' in df.columns and 'CPI_Index_KOR' in df.columns:
        # Normalizamos os índices de preço se necessário, mas a razão E * P*/P já define q.
        # Costuma-se indexar q para facilitar a visualização (ex: base 100 em certa data).
        q = df['Exchange_Rate'] * (df['CPI_Index_USA'] / df['CPI_Index_KOR'])
        # Normalizar para q=1 no início da série para facilitar visualização de depreciação/apreciação
        df['Real_Exchange_Rate'] = q / q.dropna().iloc[0]
    
    # 3. Grau de Abertura (Exp + Imp) / PIB
    if 'Exp_GDP' in df.columns and 'Imp_GDP' in df.columns:
        df['Trade_Openness'] = df['Exp_GDP'] + df['Imp_GDP']
    
    # 5. Dívida como % do PIB (BOK)
    # Public_Debt_KRW_Billion / (Real_GDP_Q * 4 * (CPI_Index_KOR/100) / 1000)
    # Note: Real_GDP_Q is in Million KRW. 4 * Q is Annual Million. / 1000 is Billion.
    if 'Public_Debt_KRW_Billion' in df.columns and 'Real_GDP_Q' in df.columns and 'CPI_Index_KOR' in df.columns:
        nominal_gdp_annual_billion = (df['Real_GDP_Q'] * 4 * (df['CPI_Index_KOR'] / 100)) / 1000
        df['BOK_Gov_Debt_GDP'] = (df['Public_Debt_KRW_Billion'] / nominal_gdp_annual_billion) * 100
        
    # 6. Dívida Externa como % do PIB
    # External_Debt_USD_Million / (Nominal_GDP_KRW_Billion / Exchange_Rate * 1000)
    if 'External_Debt_USD_Million' in df.columns and 'Exchange_Rate' in df.columns:
        # We need Nominal GDP in USD Million
        nominal_gdp_usd_million = (nominal_gdp_annual_billion * 1000) / df['Exchange_Rate']
        df['BOK_External_Debt_GDP'] = (df['External_Debt_USD_Million'] / nominal_gdp_usd_million) * 100

    return df

def run_analysis():
    print("Iniciando Análise Macroeconômica da Coreia do Sul (1960-2024)...")
    
    # 1. Carregar Dados
    loader = SocioEconomicDataLoader()
    df = loader.get_full_dataset()
    
    # Merge com dados do BOK (Dívida e Câmbio Histórico)
    bok_path = 'data/bok_debt_history.csv'
    if os.path.exists(bok_path):
        print("Integrando dados do BOK...")
        bok_df = pd.read_csv(bok_path)
        bok_df['Year'] = pd.to_datetime(bok_df['Date']).dt.year
        
        # Preserve original index
        original_index = df.index
        df['Year'] = df.index.year
        
        # Merge - Add BOK FX as well if available
        merge_cols = ['Year', 'Public_Debt_KRW_Billion', 'External_Debt_USD_Million']
        if 'Exchange_Rate_BOK' in bok_df.columns:
            merge_cols.append('Exchange_Rate_BOK')
        
        df = pd.merge(df, bok_df[merge_cols], on='Year', how='left')
        
        # Fill FRED exchange rate gaps with BOK historical rates
        if 'Exchange_Rate_BOK' in df.columns:
            df['Exchange_Rate'] = df['Exchange_Rate'].fillna(df['Exchange_Rate_BOK'])
        
        # Restore index
        df.index = original_index
        df.drop(columns=['Year'], inplace=True)

    # 1.1. Integrar dados de alta frequência do BOK (2025 coverage)
    extra_path = 'data/bok_macro_extra.csv'
    if os.path.exists(extra_path):
        print("Integrando dados extras do BOK (Alta Frequência)...")
        extra_df = pd.read_csv(extra_path)
        extra_df['Date'] = pd.to_datetime(extra_df['Date'])
        
        # Merge on Date index
        df = df.reset_index()
        if 'Date' not in df.columns: # happened in some versions
             df.rename(columns={df.columns[0]: 'Date'}, inplace=True)
        df['Date'] = pd.to_datetime(df['Date'])
        
        df = pd.merge(df, extra_df, on='Date', how='left')
        
        # Fill gaps
        mappings = {
            'Exchange_Rate': 'Exchange_Rate_BOK',
            'CPI_Index_KOR': 'CPI_Index_KOR_BOK',
            'Policy_Rate': 'Policy_Rate_BOK',
            'Real_GDP_Q': 'Real_GDP_Q_BOK'
        }
        for fred_col, bok_col in mappings.items():
            if fred_col in df.columns and bok_col in df.columns:
                df[fred_col] = df[fred_col].fillna(df[bok_col])
        
        # Recalculate CPI_YoY if missing
        if 'CPI_Index_KOR' in df.columns:
            df['CPI_YoY'] = df['CPI_YoY'].fillna(df['CPI_Index_KOR'].pct_change(12) * 100)

        # Drop temporary BOK columns
        cols_to_drop = [c for c in mappings.values() if c in df.columns]
        df.drop(columns=cols_to_drop, inplace=True)
        
        df.set_index('Date', inplace=True)

    # 2. Calcular Variáveis
    print("Calculando Variáveis Derivadas...")
    df['Output_Gap'] = calculate_output_gap(df)
    df = calculate_derived_variables(df)
    
    # Salvar dataset final com variáveis derivadas
    df.to_csv('data/south_korea_comprehensive_final.csv')
    print("Dataset final com variáveis derivadas salvo em data/south_korea_comprehensive_final.csv")
    
    # 3. Inicializar Visualizador
    visualizer = MacroVisualizer(output_dir='plots/pt-br')

    # 4. Definir Crises para Análise
    crises = {
        '1. Crise do Petroleo': ('1970-01-01', '1985-12-31', '1. Crise do Petróleo (1970-1985)'),
        'Crise_Asiatica': ('1995-01-01', '2002-12-31', 'Crise Asiática (1995-2002)'),
        '2. Crise Financeira': ('2007-01-01', '2012-12-31', '2. Crise Financeira Global (2007-2012)'),
        '3. Pandemia': ('2019-10-01', '2024-03-31', '3. Pandemia COVID-19 (2019-2024)'),
        '4. Quadro Atual': ('2022-01-01', '2025-12-31', '4. Quadro Atual (2022-2025)')
    }

    # Gráfico de Longo Prazo: Grau de Abertura
    print("Gerando gráfico de Abertura Comercial...")
    visualizer.plot_openness(df, "Evolução do Grau de Abertura Comercial", "longo_prazo_abertura.png")

    # 5. Loop de Análise por Crise
    for key, (start, end, label) in crises.items():
        print(f"Gerando dashboards para: {label}...")
        df_period = df.loc[start:end]
        
        # Dashboard de Demanda (C, I, G, X, M)
        visualizer.plot_time_series(
            df_period, ['Consumption_KD', 'Investment_KD', 'Gov_Spending_KD', 'Exports_KD', 'Imports_KD'],
            f"Componentes da Demanda ({label})", "Valor (USD 2015)", 
            f"{key}_demanda.png", source="Banco Mundial (WDI)", period_label=label
        )
        
        # Dashboard de Câmbio (Nominal e Real)
        visualizer.plot_exchange_rate(
            df_period, f"Evolução do Câmbio ({label})",
            f"{key}_cambio.png", source="FRED", period_label=label
        )

        # Dashboard de Endividamento
        visualizer.plot_debt_structure(
            df_period, f"Estrutura de Endividamento ({label})",
            f"{key}_divida.png", source="FRED e Banco Mundial", period_label=label
        )
        
        # Dashboard Monetário (Nova Versão)
        visualizer.plot_monetary_policy(
            df_period, f"Política Monetária e Hiato ({label})", 
            f"{key}_monetario.png", source="FRED e Cálculos Próprios", period_label=label
        )

        # Dashboard de Desequilíbrios (Dívida e Externo)
        visualizer.plot_macro_imbalances(
            df_period, f"Desequilíbrios Macroeconômicos ({label})",
            f"{key}_desequilibrios.png", source="Banco Mundial (WDI)", period_label=label
        )

        # Dashboard Comparativo OCDE
        visualizer.plot_benchmark(
            df_period, ['CPI_YoY'], ['OECD_Inflation'],
            f"Inflação Comparada ({label})", f"{key}_benchmark_inflacao.png", source="FRED e WDI", period_label=label
        )
        visualizer.plot_benchmark(
            df_period, ['KOR_GDP_Growth_WDI'], ['OECD_GDP_Growth'],
            f"Crescimento Comparado ({label})", f"{key}_benchmark_pib.png", source="Banco Mundial (WDI)", period_label=label
        )

        # Dashboard Institucional (Confiança e Salários)
        if "Petroleo" not in key:
            visualizer.plot_institutional(
                df_period, f"Confiança e Ciclo ({label})", 
                f"{key}_institucional.png", source="FRED", period_label=label
            )
            visualizer.plot_time_series(
                df_period, ['Real_Wages'], f"Evolução do Salário Real ({label})", "Índice",
                f"{key}_salario_real.png", source="FRED", period_label=label
            )

        # Dashboard de Oferta (Setorial)
        visualizer.plot_time_series(
            df_period, ['Agri_VA', 'Ind_VA', 'Srv_VA'],
            f"Valor Adicionado por Setor ({label})", "Valor", 
            f"{key}_oferta.png", source="Banco Mundial (WDI)", period_label=label
        )

        # Gráficos de Evolução Teórica (Apenas para as crises principais, não para Quadro Atual)
        if "Quadro Atual" not in label:
            y_e = 100
            is_pc_mr = ISPCMR(y_e=y_e, pi_T=2.0)
            ad_bt_eru = ADBTERU(y_e=y_e)
            
            print(f"Gerando Evolução Teórica para {key}...")
            
            # Cenários de Evolução customizados por crise
            if "Petroleo" in key:
                is_pc_mr.pi_T = 2.0
                states_is_pc_mr = {
                    'A': {'pi_lagged': 2.0},
                    'B': {'pi_lagged': 2.0, 'pc_shift': 8.0}, # Choque de Oferta
                    'C': {'pi_lagged': 8.0, 'pc_shift': 0, 'is_shift': -5.0} # Resposta BC e Fiscal
                }
                states_ad_bt_eru = {
                    'A': {},
                    'B': {'bt_shift': 0.5, 'ad_shift': 0.5}, # Piora na balança comercial
                    'C': {'bt_shift': 0.5, 'ad_shift': 0.5, 'eru_shift': -0.5} # Compressão salarial (ERU para baixo)
                }
            elif "Financeira" in key:
                is_pc_mr.pi_T = 3.0
                states_is_pc_mr = {
                    'A': {'pi_lagged': 3.0, 'y_e': 100.0, 'pi_T': 3.0},
                    'B': {'y_override': 96.0, 'pi_override': 3.0 + 1.2*(96.0-100.0), 'is_shift': -8.0, 'y_e': 100.0, 'pi_T': 3.0},
                    'C': {'pi_lagged': 2.0, 'y_e': 103.0, 'pi_T': 2.0, 'is_shift': 5.0} 
                }


                states_ad_bt_eru = {
                    'A': {},
                    'B': {'ad_shift': 0.8}, # Choque negativo de demanda (AD p/ esquerda)
                    'C': {} # Volta à condição inicial (igual a A)
                }
            elif "Pandemia" in key:
                states_is_pc_mr = {
                    'A': {'pi_lagged': 1.0},
                    'B': {'pi_lagged': 1.0, 'is_shift': -6.0, 'pc_shift': 3.0}, # Choque misto
                    'C': {'pi_lagged': 3.0, 'is_shift': 0.0, 'pc_shift': 0} # Resposta Massiva
                }
                states_ad_bt_eru = {
                    'A': {},
                    'B': {'ad_shift': -0.5},
                    'C': {'ad_shift': -0.5, 'eru_shift': 0.3} # Liderança Tecnológica (ERU p/ cima)
                }
            else: # Crise Asiática ou Outros
                states_is_pc_mr = {
                    'A': {'pi_lagged': 4.0},
                    'B': {'pi_lagged': 4.0, 'is_shift': -10.0},
                    'C': {'pi_lagged': 6.0, 'is_shift': -2.0}
                }
                states_ad_bt_eru = {
                    'A': {},
                    'B': {'ad_shift': -1.0},
                    'C': {'ad_shift': -1.0, 'bt_shift': -0.5}
                }

            visualizer.plot_theoretical_evolution_is_pc_mr(
                is_pc_mr, states_is_pc_mr, 
                filename=f"{key}_evolucao_ISPCMR.png"
            )
            visualizer.plot_theoretical_evolution_ad_bt_eru(
                ad_bt_eru, states_ad_bt_eru,
                filename=f"{key}_evolucao_ADBTERU.png"
            )

        # Dados Específicos de Saúde para Pandemia
        if "Pandemia" in key:
            visualizer.plot_time_series(
                df_period, ['Total_Health_Exp_GDP', 'Public_Health_Exp_GDP', 'CPI_Health'],
                "Indicadores de Saúde (Pandemia)", "Percentual (%)", 
                f"{key}_saude.png", source="Banco Mundial e FRED", period_label=label
            )

    print("\nProcesso Concluído com Sucesso!")
    print(f"Todos os gráficos salvos em: {os.path.abspath(visualizer.output_dir)}")

if __name__ == "__main__":
    run_analysis()
