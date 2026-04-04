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

    def get_is_curve(self, r_range):
        """Retorna os valores de y para um intervalo de r."""
        # y = y_e - a(r - r_star)
        return self.y_e - self.a * (r_range - self.r_star)

    def get_pc_curve(self, y_range, pi_lagged):
        """Retorna os valores de pi para um intervalo de y, dada pi_e."""
        # pi = pi_e + alpha(y - y_e)
        return pi_lagged + self.alpha * (y_range - self.y_e)

    def get_mr_curve(self, y_range):
        """Retorna os valores de pi para a Regra Monetária (MR)."""
        # MR: (y - y_e) = - (alpha * beta) * (pi - pi_T)
        # pi = pi_T - (y - y_e) / (alpha * beta)
        return self.pi_T - (y_range - self.y_e) / (self.alpha * self.beta)

class ADBTERU(MacroModel):
    """Modelo AD-BT-ERU para Economia Aberta."""
    def __init__(self, y_e=100, q_bar=1.0, theta=0.1, phi=0.05, **kwargs):
        super().__init__(**kwargs)
        self.q_bar = q_bar  # Taxa de câmbio real de equilíbrio
        self.theta = theta  # Sensibilidade da Balança Comercial
        self.phi = phi      # Sensibilidade da Demanda Agregada ao câmbio

    def get_eru_curve(self, y_range):
        """Curva ERU (Equilibrium Real Wage) - Inclinada negativamente."""
        # q = q_bar - gamma * (y - y_e)
        gamma = 0.08
        return self.q_bar - gamma * (y_range - self.y_e)

    def get_bt_curve(self, y_range):
        """Curva BT (Balance of Trade)."""
        # q = q_bar + theta * (y - y_e)
        return self.q_bar + self.theta * (y_range - self.y_e)

    def get_ad_curve(self, y_range):
        """Curva AD (Aggregate Demand) em termos de q e y."""
        # q = q_bar + (y - y_e) / phi (Simplificado para visualização)
        return self.q_bar + (y_range - self.y_e) / self.phi
