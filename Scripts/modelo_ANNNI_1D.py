# ===============================================================================
# Código para gerar a Função de correlação para regimes monotônico e oscilatório
# Problema 3, item (iii) – Lista 2
# Autor: Thiago Siqueira Domingues
# ===============================================================================

import numpy as np
import matplotlib.pyplot as plt

def lambda1_BC(K, d):
    """Maior autovalor da matriz de transferência do Blume-Capel spin-1."""
    a = np.exp(K * (1 - d))
    b = np.exp(-K * d / 2)
    c = np.exp(-K * (1 + d))
    S = a + c
    R = np.sqrt((S - 1)**2 + 8 * b**2)
    return (S + 1 + R) / 2

def U_over_NJ_BC(K, d):
    """
    Energia interna por sítio U/(NJ) = - d/dK ln(lambda1).
    Usa derivada analítica exata.
    """
    a = np.exp(K * (1 - d))
    b = np.exp(-K * d / 2)
    c = np.exp(-K * (1 + d))
    
    S = a + c
    R = np.sqrt((S - 1)**2 + 8 * b**2)
    lam = (S + 1 + R) / 2
    
    dS_dK = (1 - d) * a - (1 + d) * c
    db_dK = -(d / 2) * b
    dR_dK = ((S - 1) * dS_dK + 8 * b * db_dK) / R
    dlam_dK = 0.5 * (dS_dK + dR_dK)
    
    return -dlam_dK / lam

# Parâmetros
t_vals = np.linspace(0.1, 3.0, 500)   # t = k_B T / J
K_vals = 1.0 / t_vals
d_list = [0.0, 0.5, 0.8, 1.0, 1.2, 2.0]

# Plot
plt.figure(figsize=(8, 6))
for d in d_list:
    U = U_over_NJ_BC(K_vals, d)
    plt.plot(t_vals, U, linewidth=2, label=f'd = {d:.1f}')

plt.xlabel('$t = k_B T / J$', fontsize=14)
plt.ylabel('$U / (NJ)$', fontsize=14)
plt.title('Energia interna do modelo de Blume–Capel 1D', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.xlim(0, 3)
plt.ylim(-1.2, 1.5)
plt.tight_layout()
plt.savefig('energy_spin1.png', dpi=300)
plt.show()
