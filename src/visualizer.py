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

    def _label_curve_inside(self, ax, x_vals, y_vals, label, color, x_lim, y_lim, alpha=1.0):
        """Helper to place a label inside the plot area, aligned to the right."""
        # Find points within limits
        mask = (x_vals >= x_lim[0]) & (x_vals <= x_lim[1]) & (y_vals >= y_lim[0]) & (y_vals <= y_lim[1])
        valid_x = x_vals[mask]
        valid_y = y_vals[mask]
        
        if len(valid_x) == 0:
            return

        # Target the rightmost 5% of the visible curve
        idx = -min(5, len(valid_x))
        x_pos = valid_x[idx]
        y_pos = valid_y[idx]
        
        ax.text(x_pos, y_pos, f' {label}', color=color, fontweight='bold', 
                va='center', ha='right', alpha=alpha, fontsize=9)

    def _get_grouped_point_labels(self, points, labels_dict, x_scale, y_scale):
        """Helper to group overlapping equilibrium points."""
        groups = []
        used = set()
        pts_keys = list(points.keys())
        for i, k1 in enumerate(pts_keys):
            if k1 in used: continue
            group = [k1]
            used.add(k1)
            for k2 in pts_keys[i+1:]:
                if k2 in used: continue
                d = np.sqrt(((points[k1][0] - points[k2][0])/x_scale)**2 + ((points[k1][1] - points[k2][1])/y_scale)**2)
                if d < 0.15:
                    group.append(k2)
                    used.add(k2)
            groups.append(group)
        
        final_labels = {}
        for g in groups:
            combined_pos = np.mean([points[k] for k in g], axis=0)
            combined_label = " & ".join([k for k in g])
            desc = combined_label + ": " + " / ".join([labels_dict[k].split(': ')[1] for k in g])
            final_labels[tuple(combined_pos)] = desc
        return final_labels

    def _group_identical_states(self, states_dict, keys_to_check):
        groups = []
        used = set()
        keys = list(states_dict.keys())
        for i, k1 in enumerate(keys):
            if k1 in used: continue
            group = [k1]
            used.add(k1)
            for k2 in keys[i+1:]:
                if k2 in used: continue
                is_identical = True
                for field in keys_to_check:
                    if states_dict[k1].get(field, 0) != states_dict[k2].get(field, 0):
                        is_identical = False
                        break
                if is_identical:
                    group.append(k2)
                    used.add(k2)
            groups.append(group)
        return groups

    def plot_theoretical_evolution_is_pc_mr(self, model, states, filename):
        """Plota a evolução teórica IS-PC-MR (Estados A, B, C)."""
        points_pc_mr = {}
        points_is = {}
        for state, params in states.items():
            y_eq, pi_eq = model.solve_equilibrium_pc_mr(params.get('pi_lagged', model.pi_T), params.get('pc_shift', 0))
            points_pc_mr[state] = (y_eq, pi_eq)
            r_eq = model.r_star + (model.y_e + params.get('is_shift', 0) - y_eq) / model.a
            points_is[state] = (y_eq, r_eq)

        all_y = [p[0] for p in points_pc_mr.values()] + [model.y_e]
        all_pi = [p[1] for p in points_pc_mr.values()] + [model.pi_T]
        all_r = [p[1] for p in points_is.values()] + [model.r_star]
        
        y_lim = (min(all_y) - 5, max(all_y) + 5)
        pi_lim = (min(all_pi) - 2, max(all_pi) + 2)
        r_lim = (min(all_r) - 2, max(all_r) + 2)
        
        y_range = np.linspace(y_lim[0], y_lim[1], 200)
        r_range = np.linspace(r_lim[0], r_lim[1], 200)

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12), sharex=True)
        colors = {'A': 'gray', 'B': 'red', 'C': 'blue'}
        labels = {'A': 'A: Pré-Crise', 'B': 'B: Choque', 'C': 'C: Resposta'}

        # --- Subplot 1: PC-MR ---
        mr = model.get_mr_curve(y_range)
        ax1.plot(y_range, mr, color='black', lw=2, linestyle='--')
        self._label_curve_inside(ax1, y_range, mr, 'MR', 'black', y_lim, pi_lim)
        
        pc_groups = self._group_identical_states(states, ['pi_lagged', 'pc_shift'])
        for group in pc_groups:
            state = group[0]
            params = states[state]
            pc = model.get_pc_curve(y_range, params.get('pi_lagged', model.pi_T), params.get('pc_shift', 0))
            ax1.plot(y_range, pc, color=colors[state], lw=1.5, alpha=0.7)
            self._label_curve_inside(ax1, y_range, pc, f"PC ({'&'.join(group)})", colors[state], y_lim, pi_lim)
            for s in group:
                ax1.scatter(points_pc_mr[s][0], points_pc_mr[s][1], color=colors[s], s=100, zorder=5)

        grouped_pts = self._get_grouped_point_labels(points_pc_mr, labels, y_lim[1]-y_lim[0], pi_lim[1]-pi_lim[0])
        for pos, txt in grouped_pts.items():
            offset = 0.4 if pos[1] >= model.pi_T else -0.6
            ax1.text(pos[0], pos[1] + offset, txt, color='black', fontweight='bold', ha='center', fontsize=9,
                     bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.2'))

        if 'A' in points_pc_mr and 'B' in points_pc_mr:
            ax1.annotate('', xy=points_pc_mr['B'], xytext=points_pc_mr['A'], arrowprops=dict(arrowstyle="->", color='darkred', lw=2, alpha=0.6))
        if 'B' in points_pc_mr and 'C' in points_pc_mr:
            ax1.annotate('', xy=points_pc_mr['C'], xytext=points_pc_mr['B'], arrowprops=dict(arrowstyle="->", color='darkblue', lw=2, alpha=0.6))

        ax1.axvline(model.y_e, color='black', linestyle=':', alpha=0.5)
        ax1.set_ylabel('Inflação (π %)')
        ax1.set_ylim(pi_lim)
        ax1.set_title('Evolução Teórica: Diagrama PC-MR', fontsize=14, fontweight='bold')

        # --- Subplot 2: IS ---
        is_groups = self._group_identical_states(states, ['is_shift'])
        for group in is_groups:
            state = group[0]
            params = states[state]
            y_is = model.get_is_curve(r_range, params.get('is_shift', 0))
            ax2.plot(y_is, r_range, color=colors[state], lw=1.5, alpha=0.7)
            self._label_curve_inside(ax2, y_is, r_range, f"IS ({'&'.join(group)})", colors[state], y_lim, r_lim)
            for s in group:
                ax2.scatter(points_is[s][0], points_is[s][1], color=colors[s], s=100, zorder=5)

        grouped_is_pts = self._get_grouped_point_labels(points_is, labels, y_lim[1]-y_lim[0], r_lim[1]-r_lim[0])
        for pos, txt in grouped_is_pts.items():
            offset = 0.4 if pos[1] >= model.r_star else -0.6
            ax2.text(pos[0], pos[1] + offset, txt, color='black', fontweight='bold', ha='center', fontsize=9,
                     bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.2'))

        if 'A' in points_is and 'B' in points_is:
            ax2.annotate('', xy=points_is['B'], xytext=points_is['A'], arrowprops=dict(arrowstyle="->", color='darkred', lw=2, alpha=0.6))
        if 'B' in points_is and 'C' in points_is:
            ax2.annotate('', xy=points_is['C'], xytext=points_is['B'], arrowprops=dict(arrowstyle="->", color='darkblue', lw=2, alpha=0.6))

        ax2.axvline(model.y_e, color='black', linestyle=':', alpha=0.5)
        ax2.set_xlabel('Produto (y)')
        ax2.set_ylabel('Taxa de Juros Real (r %)')
        ax2.set_ylim(r_lim)
        ax2.set_xlim(y_lim)
        ax2.set_title('Evolução Teórica: Curva IS', fontsize=14, fontweight='bold')
        
        self._add_source(plt.gca(), "Fonte: Elaboração baseada em Carlin & Soskice (2015)")
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/{filename}")
        plt.close()

    def plot_theoretical_evolution_ad_bt_eru(self, model, states, filename):
        """Plota a evolução teórica AD-BT-ERU (Estados A, B, C)."""
        points_eq = {}
        for state, params in states.items():
            slope_ad = 1 / (model.phi * 10)
            slope_eru = model.gamma / 10
            y_eq = model.y_e + (params.get('eru_shift', 0) - params.get('ad_shift', 0)) / (slope_ad + slope_eru)
            q_eq = model.get_ad_curve(y_eq, params.get('ad_shift', 0))
            points_eq[state] = (y_eq, q_eq)

        all_y = [p[0] for p in points_eq.values()] + [model.y_e]
        all_q = [p[1] for p in points_eq.values()] + [model.q_bar]
        
        y_lim = (min(all_y) - 10, max(all_y) + 10)
        q_lim = (min(all_q) - 1.5, max(all_q) + 1.5)
        y_range = np.linspace(y_lim[0], y_lim[1], 200)

        fig, ax = plt.subplots(figsize=(10, 8))
        colors = {'A': 'gray', 'B': 'red', 'C': 'blue'}
        labels = {'A': 'A: Pré-Crise', 'B': 'B: Choque', 'C': 'C: Resposta'}

        ad_groups = self._group_identical_states(states, ['ad_shift'])
        for group in ad_groups:
            state = group[0]
            ad = model.get_ad_curve(y_range, states[state].get('ad_shift', 0))
            ax.plot(y_range, ad, color=colors[state], lw=2, alpha=0.7)
            self._label_curve_inside(ax, y_range, ad, f"AD ({'&'.join(group)})", colors[state], y_lim, q_lim)

        bt_groups = self._group_identical_states(states, ['bt_shift'])
        for group in bt_groups:
            state = group[0]
            bt = model.get_bt_curve(y_range, states[state].get('bt_shift', 0))
            ax.plot(y_range, bt, color=colors[state], lw=1.2, linestyle='--', alpha=0.5)
            self._label_curve_inside(ax, y_range, bt, f"BT ({'&'.join(group)})", colors[state], y_lim, q_lim, alpha=0.6)

        eru_groups = self._group_identical_states(states, ['eru_shift'])
        for group in eru_groups:
            state = group[0]
            eru = model.get_eru_curve(y_range, states[state].get('eru_shift', 0))
            ax.plot(y_range, eru, color=colors[state], lw=1.2, linestyle=':', alpha=0.5)
            self._label_curve_inside(ax, y_range, eru, f"ERU ({'&'.join(group)})", colors[state], y_lim, q_lim, alpha=0.6)

        for s, pos in points_eq.items():
            ax.scatter(pos[0], pos[1], color=colors[s], s=100, zorder=5)
            
        grouped_pts = self._get_grouped_point_labels(points_eq, labels, y_lim[1]-y_lim[0], q_lim[1]-q_lim[0])
        for pos, txt in grouped_pts.items():
            offset = 0.2 if pos[1] >= model.q_bar else -0.3
            ax.text(pos[0], pos[1] + offset, txt, color='black', fontweight='bold', ha='center', fontsize=9,
                     bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.2'))

        if 'A' in points_eq and 'B' in points_eq:
            ax.annotate('', xy=points_eq['B'], xytext=points_eq['A'], arrowprops=dict(arrowstyle="->", color='darkred', lw=2, alpha=0.6))
        if 'B' in points_eq and 'C' in points_eq:
            ax.annotate('', xy=points_eq['C'], xytext=points_eq['B'], arrowprops=dict(arrowstyle="->", color='darkblue', lw=2, alpha=0.6))

        ax.axvline(model.y_e, color='black', linestyle=':', alpha=0.5)
        ax.set_xlabel('Produto (y)')
        ax.set_ylabel('Taxa de Câmbio Real (q)')
        ax.set_xlim(y_lim)
        ax.set_ylim(q_lim)
        ax.set_title('Evolução Teórica: Modelo AD-BT-ERU', fontsize=15, fontweight='bold')
        
        self._add_source(ax, "Fonte: Elaboração baseada em Carlin & Soskice (2015)")
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/{filename}")
        plt.close()
