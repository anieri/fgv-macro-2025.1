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
        
        # Linha em zero em evidência (especialmente útil para o Hiato do Produto)
        plt.axhline(0, color='black', linestyle='-', linewidth=1.5, alpha=0.6, zorder=1)
        
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

    def plot_monetary_policy(self, df, title, filename, source="FRED", period_label=None):
        """Gráfico especializado para Política Monetária: Inflação, Juros e Hiato."""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        plt.axhline(0, color='black', linestyle='-', linewidth=1.2, alpha=0.5)
        
        cols = ['CPI_YoY', 'Policy_Rate', 'Real_Interest_Rate', 'Output_Gap']
        for col in cols:
            if col in df.columns:
                valid_data = df[col].dropna()
                if not valid_data.empty:
                    ax.plot(valid_data.index, valid_data.values, label=self._translate_col(col), 
                             linewidth=2.5 if 'Real' in col else 1.5,
                             linestyle='--' if 'Gap' in col else '-')

        ax.set_title(f"Coreia do Sul: {title}", fontsize=14, fontweight='bold')
        ax.set_ylabel("Percentual (%)")
        ax.set_xlabel("Ano")
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
        self._add_source(ax, f"Fonte: {source}")
        
        if period_label:
            plt.figtext(0.1, 0.02, f"Período: {period_label}", fontsize=9)
            
        plt.savefig(f"{self.output_dir}/{filename}")
        plt.close()

    def plot_macro_imbalances(self, df, title, filename, source="Banco Mundial (WDI)", period_label=None):
        """Gráfico especializado para Desequilíbrios: Dívida e Conta Corrente."""
        fig, ax = plt.subplots(figsize=(12, 6))
        plt.axhline(0, color='black', linestyle='-', linewidth=1.2, alpha=0.5)

        cols = ['Gov_Debt_GDP', 'Current_Account_GDP', 'Private_Credit_GDP']
        for col in cols:
            if col in df.columns:
                valid_data = df[col].dropna()
                if not valid_data.empty:
                    ax.plot(valid_data.index, valid_data.values, label=self._translate_col(col), 
                             marker='o', markersize=4)

        ax.set_title(f"Coreia do Sul: {title}", fontsize=14, fontweight='bold')
        ax.set_ylabel("Percentual do PIB (%)")
        ax.set_xlabel("Ano")
        ax.legend()
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
            'Gov_Debt_GDP': 'Dívida Pública (% PIB)',
            'Real_Interest_Rate': 'Taxa de Juros Real (%)',
            'Policy_Rate': 'Taxa de Juros Nominal (%)',
            'Current_Account_GDP': 'Balanço de Conta Corrente (% PIB)',
            'Private_Credit_GDP': 'Crédito ao Setor Privado (% PIB)',
            'Real_Exchange_Rate': 'Câmbio Real (q)'
        }
        return translations.get(col, col)

    def plot_theoretical_evolution_is_pc_mr(self, model, states, filename):
        """Plota a evolução teórica IS-PC-MR (Estados A, B, C)."""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12), sharex=True)
        y_range = np.linspace(model.y_e - 15, model.y_e + 15, 100)
        r_range = np.linspace(model.r_star - 5, model.r_star + 5, 100)
        
        colors = {'A': 'gray', 'B': 'red', 'C': 'blue'}
        labels = {'A': 'A: Pré-Crise', 'B': 'B: Choque', 'C': 'C: Resposta'}
        
        # PC-MR plot (ax1)
        mr = model.get_mr_curve(y_range)
        ax1.plot(y_range, mr, color='black', lw=2, linestyle='--', label='Regra Monetária (MR)')
        
        points_pc_mr = {}
        for state, params in states.items():
            pc = model.get_pc_curve(y_range, params.get('pi_lagged', model.pi_T), params.get('pc_shift', 0))
            ax1.plot(y_range, pc, color=colors[state], lw=1.5, alpha=0.7, label=f'PC ({state})')
            
            y_eq, pi_eq = model.solve_equilibrium_pc_mr(params.get('pi_lagged', model.pi_T), params.get('pc_shift', 0))
            ax1.scatter(y_eq, pi_eq, color=colors[state], s=100, zorder=5)
            ax1.text(y_eq + 0.5, pi_eq + 0.2, labels[state], color=colors[state], fontweight='bold')
            points_pc_mr[state] = (y_eq, pi_eq)

        # Draw arrows for PC-MR
        if 'A' in points_pc_mr and 'B' in points_pc_mr:
            ax1.annotate('', xy=points_pc_mr['B'], xytext=points_pc_mr['A'], 
                         arrowprops=dict(arrowstyle="->", color='darkred', lw=2, alpha=0.6))
        if 'B' in points_pc_mr and 'C' in points_pc_mr:
            ax1.annotate('', xy=points_pc_mr['C'], xytext=points_pc_mr['B'], 
                         arrowprops=dict(arrowstyle="->", color='darkblue', lw=2, alpha=0.6))

        ax1.axvline(model.y_e, color='black', linestyle=':', alpha=0.5)
        ax1.set_ylabel('Inflação (π %)')
        ax1.set_title('Evolução Teórica: Diagrama PC-MR', fontsize=14, fontweight='bold')
        ax1.legend()

        # IS plot (ax2)
        points_is = {}
        for state, params in states.items():
            y_is = model.get_is_curve(r_range, params.get('is_shift', 0))
            ax2.plot(y_is, r_range, color=colors[state], lw=1.5, alpha=0.7, label=f'IS ({state})')
            
            y_curr = points_pc_mr[state][0]
            r_eq = model.r_star + (model.y_e + params.get('is_shift', 0) - y_curr) / model.a
            ax2.scatter(y_curr, r_eq, color=colors[state], s=100, zorder=5)
            points_is[state] = (y_curr, r_eq)

        if 'A' in points_is and 'B' in points_is:
            ax2.annotate('', xy=points_is['B'], xytext=points_is['A'], 
                         arrowprops=dict(arrowstyle="->", color='darkred', lw=2, alpha=0.6))
        if 'B' in points_is and 'C' in points_is:
            ax2.annotate('', xy=points_is['C'], xytext=points_is['B'], 
                         arrowprops=dict(arrowstyle="->", color='darkblue', lw=2, alpha=0.6))

        ax2.axvline(model.y_e, color='black', linestyle=':', alpha=0.5)
        ax2.set_xlabel('Produto (y)')
        ax2.set_ylabel('Taxa de Juros Real (r %)')
        ax2.set_title('Evolução Teórica: Curva IS', fontsize=14, fontweight='bold')
        ax2.legend()
        
        self._add_source(plt.gca(), "Fonte: Elaboração baseada em Carlin & Soskice (2015)")
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/{filename}")
        plt.close()

    def plot_theoretical_evolution_ad_bt_eru(self, model, states, filename):
        """Plota a evolução teórica AD-BT-ERU (Estados A, B, C)."""
        fig, ax = plt.subplots(figsize=(10, 8))
        y_range = np.linspace(model.y_e - 15, model.y_e + 15, 100)
        
        colors = {'A': 'gray', 'B': 'red', 'C': 'blue'}
        labels = {'A': 'A: Pré-Crise', 'B': 'B: Choque', 'C': 'C: Resposta'}

        for state, params in states.items():
            ad = model.get_ad_curve(y_range, params.get('ad_shift', 0))
            bt = model.get_bt_curve(y_range, params.get('bt_shift', 0))
            eru = model.get_eru_curve(y_range, params.get('eru_shift', 0))
            
            ax.plot(y_range, ad, color=colors[state], lw=1.5, alpha=0.6, label=f'AD ({state})')
            ax.plot(y_range, bt, color=colors[state], lw=1, linestyle='--', alpha=0.4)
            ax.plot(y_range, eru, color=colors[state], lw=1, linestyle=':', alpha=0.4)
            
            slope_ad = 1 / (model.phi * 10)
            slope_eru = model.gamma / 10
            y_eq = model.y_e + (params.get('eru_shift', 0) - params.get('ad_shift', 0)) / (slope_ad + slope_eru)
            q_eq = model.get_ad_curve(y_eq, params.get('ad_shift', 0))
            
            ax.scatter(y_eq, q_eq, color=colors[state], s=100, zorder=5)
            ax.text(y_eq + 0.5, q_eq, labels[state], color=colors[state], fontweight='bold')

        ax.axvline(model.y_e, color='black', linestyle=':', alpha=0.5)
        ax.set_xlabel('Produto (y)')
        ax.set_ylabel('Taxa de Câmbio Real (q)')
        ax.set_title('Evolução Teórica: Modelo AD-BT-ERU', fontsize=15, fontweight='bold')
        ax.legend()
        
        self._add_source(ax, "Fonte: Elaboração baseada em Carlin & Soskice (2015)")
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/{filename}")
        plt.close()

