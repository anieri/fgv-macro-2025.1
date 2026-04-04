import os
import pandas as pd
from src.data_loader import SocioEconomicDataLoader
from src.models import ISPCMR, ADBTERU
from src.visualizer import MacroVisualizer

def run_analysis():
    print("Iniciando Análise Macroeconômica da Coreia do Sul (1960-2024)...")
    
    # 1. Carregar Dados
    loader = SocioEconomicDataLoader()
    data_file = 'data/south_korea_comprehensive.csv'
    
    if not os.path.exists(data_file):
        df = loader.get_full_dataset()
    else:
        df = pd.read_csv(data_file, index_col=0, parse_dates=True)
    
    # 2. Inicializar Visualizador
    visualizer = MacroVisualizer(output_dir='plots/pt-br')

    # 3. Definir Crises para Análise (Com numeração e em Português)
    crises = {
        '1. Crise do Petroleo': ('1970-01-01', '1985-12-31', '1. Crise do Petróleo (1970-1985)'),
        'Crise_Asiatica': ('1995-01-01', '2002-12-31', 'Crise Asiática (1995-2002)'),
        '2. Crise Financeira': ('2007-01-01', '2012-12-31', '2. Crise Financeira Global (2007-2012)'),
        '3. Pandemia': ('2019-01-01', '2024-12-31', '3. Pandemia COVID-19 (2019-2024)')
    }

    # 4. Loop de Análise por Crise
    for key, (start, end, label) in crises.items():
        print(f"Gerando dashboards para: {label}...")
        df_period = df.loc[start:end]
        
        # Dashboard de Demanda
        visualizer.plot_time_series(
            df_period, ['Consumption_Q', 'Investment_Q', 'Gov_Spending_Q'],
            f"Componentes da Demanda ({label})", "Valor", 
            f"{key}_demanda.png", source="FRED", period_label=label
        )
        
        # Dashboard Monetário
        visualizer.plot_time_series(
            df_period, ['CPI_YoY', 'Unemployment'],
            f"Inflação e Desemprego ({label})", "Percentual (%)", 
            f"{key}_monetario.png", source="FRED", period_label=label
        )

        # Dashboard de Oferta (Setorial)
        visualizer.plot_time_series(
            df_period, ['Agri_VA', 'Ind_VA', 'Srv_VA'],
            f"Valor Adicionado por Setor ({label})", "Valor", 
            f"{key}_oferta.png", source="Banco Mundial (WDI)", period_label=label
        )

        # Dados Específicos de Saúde para Pandemia
        if "Pandemia" in key:
            visualizer.plot_time_series(
                df_period, ['Total_Health_Exp_GDP', 'Public_Health_Exp_GDP', 'CPI_Health'],
                "Indicadores de Saúde (Pandemia)", "Percentual (%)", 
                f"{key}_saude.png", source="Banco Mundial e FRED", period_label=label
            )

    # 5. Modelos Teóricos (Calibrados)
    print("Gerando Diagramas Teóricos (Carlin & Soskice)...")
    is_pc_mr = ISPCMR(y_e=100, pi_T=2.0, r_star=2.5)
    visualizer.plot_is_pc_mr_theoretical(is_pc_mr, pi_lagged=4.0, filename='is_pc_mr_teorico_choque.png')
    
    ad_bt_eru = ADBTERU(y_e=100, q_bar=1.0)
    visualizer.plot_ad_bt_eru_theoretical(ad_bt_eru, filename='ad_bt_eru_teorico.png')

    print("\nProcesso Concluído com Sucesso!")
    print(f"Todos os gráficos salvos em: {os.path.abspath(visualizer.output_dir)}")

if __name__ == "__main__":
    run_analysis()
