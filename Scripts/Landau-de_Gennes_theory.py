import numpy as np
import matplotlib.pyplot as plt

# Configurações de estilo
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'figure.dpi': 150
})

# Parâmetros fenomenológicos da teoria de Landau-de Gennes
a = 1.0
C = 1.0
T_star = 1.0

# Coeficientes do termo cúbico B
B_1st = -1.5  # B < 0 (Transição de 1ª ordem)
B_2nd = 1.0   # B > 0 (Transição contínua / 2ª ordem)

# Pontos notáveis para a transição de 1ª ordem
T_NI = T_star + (B_1st**2) / (27.0 * a * C)
T_spinodal = T_star + (B_1st**2) / (12.0 * a * C)
S_0 = - (2.0 * B_1st) / (9.0 * C)

# Grades de temperatura
T_low_1st = np.linspace(0.6, T_NI, 300)
T_high_1st = np.linspace(T_NI, 1.35, 200)
T_meta_1st = np.linspace(T_NI, T_spinodal, 100)

T_low_2nd = np.linspace(0.6, T_star, 300)
T_high_2nd = np.linspace(T_star, 1.35, 200)

# Solução física para o parâmetro de ordem uniaxial S(T)
def S_branch(T, B):
    disc = B**2 - 12.0 * a * C * (T - T_star)
    disc = np.maximum(disc, 0)
    return (-B + np.sqrt(disc)) / (6.0 * C)

S_1st = S_branch(T_low_1st, B_1st)
S_meta = S_branch(T_meta_1st, B_1st)
S_2nd = S_branch(T_low_2nd, B_2nd)

# Figura
fig, ax = plt.subplots(figsize=(8, 5.5))

# Curva de 2ª ordem (B > 0)
ax.plot(T_low_2nd, S_2nd, color='#1f77b4', linewidth=2.5, 
        label=r'Transição de 2ª ordem ($B > 0$)')
ax.plot(T_high_2nd, np.zeros_like(T_high_2nd), color='#1f77b4', linewidth=2.5)

# Curva de 1ª ordem (B < 0)
ax.plot(T_low_1st, S_1st, color='#d62728', linewidth=2.5, 
        label=r'Transição de 1ª ordem ($B < 0$)')
ax.plot(T_high_1st, np.zeros_like(T_high_1st), color='#d62728', linewidth=2.5)

# Descontinuidade e Ramo Metaestável (superaquecimento)
ax.plot([T_NI, T_NI], [0, S_0], color='#d62728', linestyle='--', linewidth=1.5, alpha=0.8)
ax.plot(T_meta_1st, S_meta, color='#d62728', linestyle=':', linewidth=1.8, alpha=0.7, 
        label=r'Ramo metaestável ($T_{NI} < T < T_{**}$)')

# Pontos de destaque
ax.plot(T_NI, S_0, 'o', color='#d62728', markersize=7, zorder=5)
ax.plot(T_NI, 0, 'o', color='#d62728', markerfacecolor='white', markeredgewidth=1.8, markersize=7, zorder=5)
ax.plot(T_star, 0, 's', color='#1f77b4', markersize=7, zorder=5)

# Linhas auxiliares e anotações dos eixos
ax.axvline(x=T_star, color='#1f77b4', linestyle=':', alpha=0.4)
ax.axvline(x=T_NI, color='#d62728', linestyle=':', alpha=0.4)
ax.axhline(y=S_0, color='#d62728', linestyle=':', alpha=0.4)

ax.text(T_star, -0.05, r'$T_*$', ha='center', va='top', fontsize=12, color='#1f77b4', fontweight='bold')
ax.text(T_NI, -0.05, r'$T_{NI}$', ha='center', va='top', fontsize=12, color='#d62728', fontweight='bold')
ax.text(0.7, S_0, r'$S_0 = -\frac{2B}{9C}$', ha='right', va='center', fontsize=11, color='#d62728')

# Identificação das fases
ax.text(0.75, 0.52, 'Fase Nemática\n($S > 0$)', fontsize=11, color='#1f4e79', fontweight='bold', ha='center')
ax.text(1.22, 0.12, 'Fase Isotrópica\n($S = 0$)', fontsize=11, color='#7a1f1f', fontweight='bold', ha='center')

# Eixos e Legendas
ax.set_xlabel(r'$T$')
ax.set_ylabel(r'$S$')
ax.set_title('Transição Nemático–Isotrópica (Teoria de Landau–de Gennes)', pad=12)

ax.set_xlim(0.58, 1.35)
ax.set_ylim(-0.08, 0.72)

ax.grid(True, linestyle='--', alpha=0.35, color='#888888')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(frameon=True, facecolor='white', framealpha=0.95, edgecolor='none', loc='upper right', fontsize=10)

plt.tight_layout()
plt.savefig('LdG_S_vs_T.png', dpi=300)
plt.show()
