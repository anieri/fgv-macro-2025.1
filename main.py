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
        # Fills NaNs temporarily for the filter, then takes quarterly points
        gdp = df['Real_GDP_Q'].dropna()
        if len(gdp) > 20:
            # lambda = 1600 para dados trimestrais
            cycle, trend = hpfilter(np.log(gdp), lamb=1600)
            # Hiato = (y - y_trend) / y_trend * 100
            gap = (np.exp(cycle) - 1) * 100
            return pd.Series(gap, index=gdp.index)
    return pd.Series(dtype=float)

def run_analysis():
    print("Iniciando Análise Macroeconômica da Coreia do Sul (1960-2024)...")
    
    # 1. Carregar Dados
    loader = SocioEconomicDataLoader()
    data_file = 'data/south_korea_comprehensive.csv'
    
    if not os.path.exists(data_file):
        df = loader.get_full_dataset()
    else:
        df = pd.read_csv(data_file, index_col=0, parse_dates=True)
    
    # 2. Calcular Hiato do Produto
    print("Calculando Hiato do Produto (Filtro HP)...")
    df['Output_Gap'] = calculate_output_gap(df)
    
    # 3. Inicializar Visualizador
    visualizer = MacroVisualizer(output_dir='plots/pt-br')

    # 4. Definir Crises para Análise
    crises = {
        '1. Crise do Petroleo': ('1970-01-01', '1985-12-31', '1. Crise do Petróleo (1970-1985)'),
        'Crise_Asiatica': ('1995-01-01', '2002-12-31', 'Crise Asiática (1995-2002)'),
        '2. Crise Financeira': ('2007-01-01', '2012-12-31', '2. Crise Financeira Global (2007-2012)'),
        '3. Pandemia': ('2019-01-01', '2024-12-31', '3. Pandemia COVID-19 (2019-2024)')
    }

    # 5. Loop de Análise por Crise
    for key, (start, end, label) in crises.items():
        print(f"Gerando dashboards para: {label}...")
        df_period = df.loc[start:end]
        
        # Dashboard de Demanda
        visualizer.plot_time_series(
            df_period, ['Consumption_Q', 'Investment_Q', 'Gov_Spending_Q'],
            f"Componentes da Demanda ({label})", "Valor", 
            f"{key}_demanda.png", source="FRED", period_label=label
        )
        
        # Dashboard Monetário e Hiato
        visualizer.plot_time_series(
            df_period, ['CPI_YoY', 'Output_Gap'],
            f"Inflação e Hiato do Produto ({label})", "Percentual (%)", 
            f"{key}_hiato_inflacao.png", source="FRED e Cálculos Próprios", period_label=label
        )

        # Dashboard de Oferta (Setorial)
        visualizer.plot_time_series(
            df_period, ['Agri_VA', 'Ind_VA', 'Srv_VA'],
            f"Valor Adicionado por Setor ({label})", "Valor", 
            f"{key}_oferta.png", source="Banco Mundial (WDI)", period_label=label
        )

        # Gráficos Teóricos para cada Crise
        # Ajustamos a meta de inflação ou o choque dependendo do período
        pi_expected = df_period['CPI_YoY'].mean()
        y_e = 100
        
        is_pc_mr = ISPCMR(y_e=y_e, pi_T=2.0)
        ad_bt_eru = ADBTERU(y_e=y_e)
        
        print(f"Gerando Diagramas Teóricos para {key}...")
        visualizer.plot_is_pc_mr_theoretical(
            is_pc_mr, pi_lagged=pi_expected, 
            filename=f"{key}_teorico_ISPCMR.png"
        )
        visualizer.plot_ad_bt_eru_theoretical(
            ad_bt_eru, 
            filename=f"{key}_teorico_ADBTERU.png"
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


if __name__ == "__main__":
    run_analysis()
