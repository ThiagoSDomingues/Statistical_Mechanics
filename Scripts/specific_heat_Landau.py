# =============================================================================
# Código para gerar o calor específico a campo nulo
# Problema 4, item (d) – Lista de Física Estatística Avançada
# Autor: Thiago Siqueira Domingues
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

def C_landau(tau, a=1, b=1):
    C = np.zeros_like(tau)
    C[tau < 0] = a**2 / (2 * b)
    return C

# Parâmetros
a = 1.0
b = 1.0
tau = np.linspace(-2, 2, 1000)

# Calor específico
C = C_landau(tau, a, b)

# Plot
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(tau, C, 'b-', linewidth=2)
ax.axvline(x=0, color='black', linestyle='-', linewidth=1)

ax.set_xlabel('$\\tau$', fontsize=14)
ax.set_ylabel('$C_{\\text{sing}}(\\tau)$', fontsize=14)
ax.set_title('Calor específico singular a campo nulo', fontsize=14)
ax.grid(True)
ax.set_xlim(-2, 2)
ax.set_ylim(0, 1.5)

plt.tight_layout()
plt.savefig('landau_heat_capacity.png', dpi=300)
plt.show()
