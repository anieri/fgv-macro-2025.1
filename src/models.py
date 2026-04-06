import numpy as np

class MacroModel:
    """Classe base para modelos macroeconômicos."""
    def __init__(self, y_e=100, pi_T=2):
        self.y_e = y_e  # Output de equilíbrio (potencial)
        self.pi_T = pi_T  # Meta de inflação

class ISPCMR(MacroModel):
    """Modelo IS-PC-MR de Carlin & Soskice."""
    def __init__(self, a=0.8, alpha=1.2, beta=1.0, r_star=2.0, **kwargs):
        super().__init__(**kwargs)
        self.a = a          # Sensibilidade do output à taxa de juros (IS)
        self.alpha = alpha  # Inclinação da Curva de Phillips (PC)
        self.beta = beta    # Preferência do Banco Central (MR)
        self.r_star = r_star # Taxa de juros real estabilizadora

    def get_is_curve(self, r_range, is_shift=0):
        """Retorna os valores de y para um intervalo de r. y = y_e - a(r - r_star) + shift"""
        return self.y_e - self.a * (r_range - self.r_star) + is_shift

    def get_pc_curve(self, y_range, pi_lagged, pc_shift=0):
        """Retorna os valores de pi para um intervalo de y, dada pi_e. pi = pi_e + alpha(y - y_e) + shift"""
        return pi_lagged + self.alpha * (y_range - self.y_e) + pc_shift

    def get_mr_curve(self, y_range):
        """Retorna os valores de pi para a Regra Monetária (MR). pi = pi_T - (y - y_e) / (alpha * beta)"""
        return self.pi_T - (y_range - self.y_e) / (self.alpha * self.beta)

    def solve_equilibrium_pc_mr(self, pi_lagged, pc_shift=0):
        """Encontra o ponto (y, pi) onde PC cruza MR."""
        # pi_e + alpha(y - y_e) + pc_shift = pi_T - (y - y_e) / (alpha * beta)
        # (y - y_e) * (alpha + 1/(alpha*beta)) = pi_T - pi_e - pc_shift
        slope_sum = self.alpha + 1 / (self.alpha * self.beta)
        y_star = self.y_e + (self.pi_T - pi_lagged - pc_shift) / slope_sum
        pi_star = self.get_mr_curve(y_star)
        return y_star, pi_star

class ADBTERU(MacroModel):
    """Modelo AD-BT-ERU para Economia Aberta."""
    def __init__(self, y_e=100, q_bar=1.0, theta=0.3, phi=0.5, gamma=0.3, **kwargs):
        super().__init__(**kwargs)
        self.q_bar = q_bar  # Taxa de câmbio real de equilíbrio
        self.theta = theta  # Sensibilidade da Balança Comercial
        self.phi = phi      # Sensibilidade da Demanda Agregada ao câmbio (Inclinação AD)
        self.gamma = gamma  # Sensibilidade da ERU

    def get_eru_curve(self, y_range, eru_shift=0):
        """Curva ERU (Equilibrium Real Wage) - Inclinada negativamente."""
        return self.q_bar - self.gamma * (y_range - self.y_e) / 10 + eru_shift

    def get_bt_curve(self, y_range, bt_shift=0):
        """Curva BT (Balance of Trade)."""
        return self.q_bar + self.theta * (y_range - self.y_e) / 10 + bt_shift

    def get_ad_curve(self, y_range, ad_shift=0):
        """Curva AD (Aggregate Demand) em termos de q e y."""
        return self.q_bar + (y_range - self.y_e) / (self.phi * 10) + ad_shift
