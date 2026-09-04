# =============================================================================
# Código para gerar a isoterma H(M) da teoria de Landau
# Problema 4, item (d) – Lista 2
# Autor: Thiago Siqueira Domingues
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

def H_landau(M, tau, a=1.0, b=1.0):
    """
    Equação de estado de Landau: H = 2 a tau M + 4 b M^3
    """
    return 2 * a * tau * M + 4 * b * M**3

# Parâmetros da teoria de Landau
a = 1.0
b = 1.0
tau = -0.5   # temperatura abaixo de Tc (fase ferromagnética)

# Vetor de magnetização
M = np.linspace(-2, 2, 1000)

# Campo H correspondente
H = H_landau(M, tau, a, b)

# Magnetização de equilíbrio (mínimo da energia livre)
M0 = np.sqrt(-a * tau / (2 * b))

# Criação da figura
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(M, H, 'b-', linewidth=2, label='$H = 2a\\tau M + 4b M^3$')
ax.axhline(y=0, color='red', linestyle='--', linewidth=2, label='$H = 0$ (coexistência)')
ax.scatter([-M0, M0], [0, 0], color='black', s=50, zorder=5, label='$\\pm M_0$')

ax.set_xlabel('$M$', fontsize=14)
ax.set_ylabel('$H$', fontsize=14)
ax.set_title('Equação de estado de Landau para $\\tau < 0$', fontsize=14)
ax.legend(fontsize=12)
ax.grid(True)
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 3)

plt.tight_layout()
plt.savefig('landau_H_vs_M.png', dpi=300)
plt.show()
