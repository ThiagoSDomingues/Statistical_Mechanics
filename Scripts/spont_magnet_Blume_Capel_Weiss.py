import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# Configurações globais de estilo
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.dpi': 150
})

def free_energy(m, d, t):
    x = 2.0 * np.exp(-d / t)
    return 0.5 * m**2 - t * np.log(1.0 + x * np.cosh(m / t))

def eq_m(m, d, t):
    x = 2.0 * np.exp(-d / t)
    return m - x * np.sinh(m / t) / (1.0 + x * np.cosh(m / t))

def find_stationary_points(d, t, N=1000):
    m_grid = np.linspace(1e-8, 1.0, N)
    f_grid = eq_m(m_grid, d, t)
    roots = []
    for i in range(N - 1):
        if not (np.isfinite(f_grid[i]) and np.isfinite(f_grid[i+1])):
            continue
        if f_grid[i] * f_grid[i + 1] < 0:
            root = brentq(lambda m: eq_m(m, d, t), m_grid[i], m_grid[i + 1])
            if root > 1e-6:
                roots.append(root)
    return roots

def spontaneous_magnetization(d, t):
    roots = find_stationary_points(d, t)
    candidates = [0.0] + roots
    energies = [free_energy(m, d, t) for m in candidates]
    return candidates[np.argmin(energies)]

# Parâmetros de simulação
t_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
d_vals = np.linspace(0.0, 0.6, 500)

# Paleta de cores harmônica
colors = plt.cm.inferno(np.linspace(0.2, 0.75, len(t_values)))

fig, ax = plt.subplots(figsize=(7.5, 5))

for t, color in zip(t_values, colors):
    m_vals = np.array([spontaneous_magnetization(d, t) for d in d_vals])

    # Identifica o ponto de salto descontínuo da transição de 1ª ordem (t < t_tc)
    jump_idx = np.where(np.abs(np.diff(m_vals)) > 0.15)[0]

    if len(jump_idx) > 0:
        idx = jump_idx[0]
        # Plota os trechos separados para não interpolar a descontinuidade
        ax.plot(d_vals[:idx+1], m_vals[:idx+1], color=color, linewidth=2.2, label=fr'$t = {t:.1f}$')
        ax.plot(d_vals[idx+1:], m_vals[idx+1:], color=color, linewidth=2.2)
        # Linha pontilhada indicando a queda de 1ª ordem
        ax.vlines(x=d_vals[idx], ymin=0, ymax=m_vals[idx], color=color, linestyle=':', alpha=0.7, linewidth=1.3)
    else:
        ax.plot(d_vals, m_vals, color=color, linewidth=2.2, label=fr'$t = {t:.1f}$')

# Ajustes de Eixos e Títulos
ax.set_xlabel(r'$d = D / J$')
ax.set_ylabel(r'$m_0$')
ax.set_title('Magnetização Espontânea — Blume–Capel Curie-Weiss', pad=12)

ax.set_xlim(0, 0.7)
ax.set_ylim(-0.02, 1.02)

# Estilização do Grid e Bordas
ax.grid(True, linestyle='--', alpha=0.4, color='#888888')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Legenda
ax.legend(title=r'Temperatura $t$', frameon=True, facecolor='white', framealpha=0.9, edgecolor='none', loc='upper right')

plt.tight_layout()
plt.savefig('Blume_Capel_Weiss_m0.png', dpi=300)
plt.show()
