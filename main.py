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
    
    # 4. Crescimento PIB Real KOR (YoY)
    if 'Real_GDP_Q' in df.columns:
        df['KOR_GDP_Growth'] = df['Real_GDP_Q'].pct_change(periods=4, fill_method=None) * 100

    return df

def run_analysis():
    print("Iniciando Análise Macroeconômica da Coreia do Sul (1960-2024)...")
    
    # 1. Carregar Dados
    loader = SocioEconomicDataLoader()
    data_file = 'data/south_korea_comprehensive.csv'
    
    if not os.path.exists(data_file):
        df = loader.get_full_dataset()
    else:
        # We re-run loader.get_full_dataset() if we need new columns, 
        # but for safety I'll let the user decide. 
        # Actually I'll force refresh since I just added new columns.
        df = loader.get_full_dataset()
    
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
        '3. Pandemia': ('2019-01-01', '2024-12-31', '3. Pandemia COVID-19 (2019-2024)'),
        '4. Quadro Atual': ('2022-01-01', '2024-12-31', '4. Quadro Atual (2022-2024)')
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
                states_is_pc_mr = {
                    'A': {'pi_lagged': 2.0},
                    'B': {'pi_lagged': 2.0, 'pc_shift': 8.0}, # Choque de Oferta
                    'C': {'pi_lagged': 8.0, 'pc_shift': 0, 'is_shift': -5.0} # Resposta BC e Fiscal
                }
                states_ad_bt_eru = {
                    'A': {},
                    'B': {'bt_shift': 0.5}, # Piora na balança comercial
                    'C': {'bt_shift': 0.5, 'eru_shift': -0.5} # Compressão salarial (ERU para baixo)
                }
            elif "2008" in key:
                states_is_pc_mr = {
                    'A': {'pi_lagged': 3.0},
                    'B': {'pi_lagged': 3.0, 'is_shift': -8.0}, # Queda Exportações
                    'C': {'pi_lagged': 2.0, 'is_shift': 0.0} # Estímulo Fiscal (volta IS)
                }
                states_ad_bt_eru = {
                    'A': {},
                    'B': {'ad_shift': -0.8}, # Queda na demanda global
                    'C': {'ad_shift': -0.8, 'eru_shift': 0.2} # Melhora competitividade/PS
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
