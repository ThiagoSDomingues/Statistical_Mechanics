import numpy as np
import matplotlib.pyplot as plt

def H_landau(M, tau, a=1, b=1):
    return 2 * a * tau * M + 4 * b * M**3

# Parâmetros
a = 1.0
b = 1.0
tau = -0.5
M = np.linspace(-2, 2, 1000)

# Equação de estado
H = H_landau(M, tau, a, b)

# Pontos de coexistência
M0 = np.sqrt(-a * tau / (2 * b))
H_coex = 0

# Plot
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(M, H, 'b-', linewidth=2, label='$H = 2a\\tau M + 4b M^3$')
ax.axhline(y=0, color='red', linestyle='--', linewidth=2, label='$H = 0$ (coexistência)')
ax.scatter([-M0, M0], [0, 0], color='black', s=50, zorder=5)

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
