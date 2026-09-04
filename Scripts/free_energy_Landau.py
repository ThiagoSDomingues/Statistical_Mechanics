# ===============================================================================================
# Código para gerar a energia livre da teoria de Landau (poço único e poço duplo)
# Problema 4, item (a) – Lista 2
# Autor: Thiago Siqueira Domingues
# ===============================================================================================

import numpy as np
import matplotlib.pyplot as plt

def F_landau(M, tau, a=1.0, b=1.0):
    return a * tau * M**2 + b * M**4

# Parâmetros
a, b = 1.0, 1.0
M = np.linspace(-2, 2, 1000)

# Plot lado a lado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# t > 0
tau_pos = 0.5
F_pos = F_landau(M, tau_pos, a, b)
ax1.plot(M, F_pos, 'b-', linewidth=2)
ax1.set_xlabel('$M$', fontsize=14)
ax1.set_ylabel('$F(M) - F_0$', fontsize=14)
ax1.set_title('$t > 0$ (paramagnético)', fontsize=14)
ax1.grid(True)
ax1.set_xlim(-2, 2)
ax1.set_ylim(-0.5, 4)

# t < 0
tau_neg = -0.5
F_neg = F_landau(M, tau_neg, a, b)
ax2.plot(M, F_neg, 'r-', linewidth=2)
ax2.set_xlabel('$M$', fontsize=14)
ax2.set_ylabel('$F(M) - F_0$', fontsize=14)
ax2.set_title('$t < 0$ (ferromagnético)', fontsize=14)
ax2.grid(True)
ax2.set_xlim(-2, 2)
ax2.set_ylim(-1, 1.5)

plt.tight_layout()
plt.savefig('landau_f_vs_m.png', dpi=300)
plt.show()
