import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns

class MacroVisualizer:
    def __init__(self, output_dir='plots/pt-br'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        sns.set_theme(style="whitegrid")
        plt.rcParams['figure.autolayout'] = True

    def _add_source(self, ax, source="Fonte: FRED e Banco Mundial (WDI)"):
        """Adiciona a fonte no rodapé do gráfico."""
        plt.figtext(0.95, 0.02, source, horizontalalignment='right', 
                    fontsize=8, color='gray', style='italic')

    def _format_axis_labels(self, ax, values):
        """Formata os rótulos do eixo Y para Milhões, Bilhões ou Trilhões."""
        from matplotlib.ticker import FuncFormatter
        
        # Filtra valores válidos (não nulos e não infinitos)
        valid_values = [v for v in values if np.isfinite(v)]
        if not valid_values:
            return
        
        max_val = max(abs(np.array(valid_values)))
        
        if max_val >= 1e12:
            scale = 1e12
            suffix = "(Trilhões)"
        elif max_val >= 1e9:
            scale = 1e9
            suffix = "(Bilhões)"
        elif max_val >= 1e6:
            scale = 1e6
            suffix = "(Milhões)"
        else:
            scale = 1
            suffix = ""

        def format_func(x, pos):
            return f"{x/scale:,.1f}".replace(',', 'X').replace('.', ',').replace('X', '.')

        ax.yaxis.set_major_formatter(FuncFormatter(format_func))
        return suffix

    def plot_time_series(self, df, columns, title, ylabel, filename, source="FRED", period_label=None):
        """Plota séries temporais simples com tradução e escala legível."""
        plt.figure(figsize=(12, 6))
        all_values = []
        for col in columns:
            if col in df.columns:
                valid_data = df[col].dropna()
                if not valid_data.empty:
                    label = self._translate_col(col)
                    plt.plot(valid_data.index, valid_data.values, label=label, marker='o' if len(valid_data) < 50 else None)
                    all_values.extend(valid_data.values)
        
        ax = plt.gca()
        suffix = self._format_axis_labels(ax, all_values)
        
        plt.title(f"Coreia do Sul: {title}", fontsize=14, fontweight='bold')
        plt.ylabel(f"{ylabel} {suffix}")
        plt.xlabel("Ano")
        plt.legend()
        self._add_source(ax, f"Fonte: {source}")
        
        if period_label:
            plt.figtext(0.1, 0.02, f"Período: {period_label}", fontsize=9)

        plt.savefig(f"{self.output_dir}/{filename}")
        plt.close()

    def _translate_col(self, col):
        translations = {
            'CPI_YoY': 'Inflação (YoY %)',
            'Unemployment': 'Taxa de Desemprego (%)',
            'Real_GDP_Q': 'PIB Real (Trimestral)',
            'Consumption_Q': 'Consumo (C)',
            'Gov_Spending_Q': 'Gastos do Governo (G)',
            'Investment_Q': 'Investimento (I)',
            'Exports_M': 'Exportações (Mês)',
            'Imports_M': 'Importações (Mês)',
            'Exchange_Rate': 'Câmbio (Won/USD)',
            'Ind_Prod': 'Produção Industrial',
            'Agri_VA': 'V.A. Agropecuária',
            'Ind_VA': 'V.A. Indústria',
            'Srv_VA': 'V.A. Serviços',
            'Public_Health_Exp_GDP': 'Gasto Público Saúde (% PIB)',
            'Total_Health_Exp_GDP': 'Gasto Total Saúde (% PIB)',
            'CPI_Health': 'Inflação Saúde (YoY)',
            'Retail_Sales': 'Vendas no Varejo (Proxy C)',
            'Gov_Debt_GDP': 'Dívida Pública (% PIB)'
        }
        return translations.get(col, col)

    def plot_is_pc_mr_theoretical(self, model, pi_lagged=3, filename='is_pc_mr_teorico.png'):
        """Gera o diagrama IS-PC-MR de Carlin & Soskice."""
        y_range = np.linspace(model.y_e - 10, model.y_e + 10, 100)
        pi_pc = model.get_pc_curve(y_range, pi_lagged)
        pi_mr = model.get_mr_curve(y_range)
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12), sharex=True)
        
        # PC-MR
        ax1.plot(y_range, pi_pc, label=f'PC (Inflação Esperada={pi_lagged}%)', color='red', lw=2)
        ax1.plot(y_range, pi_mr, label='Regra Monetária (MR)', color='blue', lw=2)
        ax1.axvline(model.y_e, color='black', linestyle='--', alpha=0.5, label='y_e (Produto Potencial)')
        ax1.axhline(model.pi_T, color='green', linestyle=':', alpha=0.5, label='Meta de Inflação (pi_T)')
        ax1.set_ylabel('Inflação (%)')
        ax1.set_title('Modelo de 3-Equações: PC-MR', fontsize=14)
        ax1.legend()
        
        # IS
        r_range = np.linspace(model.r_star - 4, model.r_star + 4, 100)
        y_is = model.get_is_curve(r_range)
        ax2.plot(y_is, r_range, label='Curva IS', color='darkgreen', lw=2)
        ax2.axvline(model.y_e, color='black', linestyle='--', alpha=0.5)
        ax2.axhline(model.r_star, color='purple', linestyle=':', alpha=0.5, label='r* (Taxa Estabilizadora)')
        ax2.set_xlabel('Produto (y)')
        ax2.set_ylabel('Taxa de Juros Real (r)')
        ax2.set_title('Curva IS', fontsize=14)
        ax2.legend()
        
        self._add_source(plt.gca(), "Fonte: Elaboração baseada em Carlin & Soskice (2015)")
        plt.savefig(f"{self.output_dir}/{filename}")
        plt.close()

    def plot_ad_bt_eru_theoretical(self, model, filename='ad_bt_eru_teorico.png'):
        """Gera o diagrama AD-BT-ERU com eixo duplo para legibilidade das curvas BT e ERU."""
        y_range = np.linspace(model.y_e - 15, model.y_e + 15, 100)
        eru = model.get_eru_curve(y_range)
        bt = model.get_bt_curve(y_range)
        ad = model.get_ad_curve(y_range)

        fig, ax1 = plt.subplots(figsize=(10, 8))
        
        # Eixo Esquerdo: Curva AD (Maior Range/Escala Geral)
        ax1.plot(y_range, ad, color='green', lw=3, label='AD (Demanda)')
        ax1.set_xlabel('Produto (y)')
        ax1.set_ylabel('Câmbio Real (q) - Escala AD', color='green', fontweight='bold')
        ax1.tick_params(axis='y', labelcolor='green')
        
        # Eixo Direito: Zoom nas curvas BT e ERU
        ax2 = ax1.twinx()
        ax2.plot(y_range, bt, color='blue', lw=2.5, linestyle='-', label='BT')
        ax2.plot(y_range, eru, color='red', lw=2.5, linestyle='-', label='ERU')
        ax2.set_ylabel('Câmbio Real (q) - Escala BT e ERU', color='blue', fontweight='bold')
        ax2.tick_params(axis='y', labelcolor='blue')

        # Centralizar ambos os eixos no q_bar
        # Range amplo para AD
        ax1.set_ylim(model.q_bar - 5, model.q_bar + 5)
        # Range menor (zoom) para BT/ERU conforme pedido (perto de 1)
        ax2.set_ylim(model.q_bar - 1, model.q_bar + 1)

        # Adicionar linhas de referência
        ax1.axvline(model.y_e, color='black', linestyle='--', alpha=0.3, label='y_e')
        ax1.axhline(model.q_bar, color='gray', linestyle=':', alpha=0.3)
        
        # Rótulos diretos para facilitar leitura
        ax1.text(y_range[-1], ad[-1], ' AD', color='green', fontweight='bold', va='center')
        ax2.text(y_range[-1], bt[-1], ' BT', color='blue', fontweight='bold', va='center')
        ax2.text(y_range[-1], eru[-1], ' ERU', color='red', fontweight='bold', va='center')

        plt.title('Modelo AD-BT-ERU: Equilíbrio de Economia Aberta', fontsize=15, fontweight='bold', pad=20)
        self._add_source(ax1, "Fonte: Elaboração baseada em Carlin & Soskice (2015)")
        
        fig.tight_layout()
        plt.savefig(f"{self.output_dir}/{filename}")
        plt.close()

