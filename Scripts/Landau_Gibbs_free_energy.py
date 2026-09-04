# ===============================================================================================
# Código para gerar a Energia livre de Gibbs com construção de Maxwell / envoltória convexa
# Problema 4, item (c) – Lista 2
# Autor: Thiago Siqueira Domingues
# ===============================================================================================

import numpy as np
import matplotlib.pyplot as plt

def g_legendre(H, tau, a=1.0, b=1.0):
    """
    Transformada de Legendre: g(H) = min_M [a tau M^2 + b M^4 - H M]
    """
    M_vals = np.linspace(-2, 2, 2000)
    g_vals = a * tau * M_vals**2 + b * M_vals**4 - H * M_vals
    return np.min(g_vals)

# Parâmetros
a, b = 1.0, 1.0
tau = -0.5  # t < 0

# Pontos especiais
M0 = np.sqrt(-a * tau / (2 * b))       # magnetização de equilíbrio
Ms = np.sqrt(-a * tau / (6 * b))       # ponto de inflexão (spinodal)
Hs = 2 * a * tau * Ms + 4 * b * Ms**3   # campo nos spinodais (positivo)
g0 = a * tau * M0**2 + b * M0**4       # g(0) = f(M0)

# Vetor de H
H_vals = np.linspace(-1.5 * Hs, 1.5 * Hs, 300)
g_direta = np.array([g_legendre(H, tau, a, b) for H in H_vals])

# Construção de Maxwell: substituir região |H| <= Hs por reta horizontal
g_maxwell = np.copy(g_direta)
mask = np.abs(H_vals) <= Hs
g_maxwell[mask] = g0

# Plot
plt.figure(figsize=(8, 6))
plt.plot(H_vals, g_direta, 'b--', linewidth=2.5, label='$g_{\\rm direta}(H)$ (sem Maxwell)')
plt.plot(H_vals, g_maxwell, 'r-', linewidth=2.5, label='$g_{\\rm Maxwell}(H)$ (com Maxwell)')
plt.axhline(y=g0, color='red', linestyle=':', alpha=0.5, label='patamar $H=0$')
plt.axvline(x=Hs, color='gray', linestyle='--', alpha=0.7, label='spinodais $\\pm H_s$')
plt.axvline(x=-Hs, color='gray', linestyle='--', alpha=0.7)

plt.xlabel('$H$', fontsize=14)
plt.ylabel('$g(t,H)$', fontsize=14)
plt.title('Energia livre de Gibbs para $t < 0$ (construção de Maxwell)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.xlim(-1.5*Hs, 1.5*Hs)
plt.tight_layout()
plt.savefig('landau_g_vs_H.png', dpi=300)
plt.show()
