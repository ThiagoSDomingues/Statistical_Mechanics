# =============================================================================
# Código para gerar o gráfico do parâmetro de ordem S vs temperatura
# Problema 4, item (b) – Teoria de Landau-de Gennes
# Autor: Thiago Siqueira Domingues
# Data: 2026
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. Parâmetros do modelo (unidades adimensionais)
# ============================================================
a = 1.0        # coeficiente do termo quadrático A(T) = a(T - T*)
C = 1.0        # coeficiente do termo quártico (estabilidade)
T_star = 0.5   # temperatura "nua" (bare) da teoria de Landau

B_second = 0.5   # B > 0 → transição de segunda ordem
B_first  = -0.5  # B < 0 → transição de primeira ordem

# ============================================================
# 2. Funções que fornecem o parâmetro de ordem de equilíbrio
# ============================================================
def S_segunda_ordem(T, B, a, C, T_star):
    """
    Parâmetro de ordem para B > 0.
    Transição de segunda ordem em T = T_star.
    Para T >= T_star: S = 0.
    Para T <  T_star: S = (-B + sqrt(B^2 + 24 a C (T_star - T))) / (6C).
    """
    if T >= T_star:
        return 0.0
    else:
        disc = B**2 + 24.0 * a * C * (T_star - T)
        return (-B + np.sqrt(disc)) / (6.0 * C)


def S_primeira_ordem_equilibrio(T, B, a, C, T_star):
    """
    Parâmetro de ordem de equilíbrio (mínimo global) para B < 0.
    Transição de primeira ordem em T_NI = T_star + B^2 / (27 a C).
    Para T >= T_NI: S = 0 (fase isotrópica).
    Para T <  T_NI: S = (-B + sqrt(B^2 + 24 a C (T_star - T))) / (6C).
    """
    T_NI = T_star + B**2 / (27.0 * a * C)
    if T >= T_NI:
        return 0.0
    else:
        disc = B**2 + 24.0 * a * C * (T_star - T)
        return (-B + np.sqrt(disc)) / (6.0 * C)


def S_primeira_ordem_metaestavel(T, B, a, C, T_star):
    """
    Ramo metaestável (mínimo local) para B < 0.
    Existe para T < T_spinodal = T_star + B^2 / (24 a C).
    Retorna nan fora desse intervalo.
    """
    T_spinodal = T_star + B**2 / (24.0 * a * C)
    if T >= T_spinodal:
        return np.nan
    else:
        disc = B**2 + 24.0 * a * C * (T_star - T)
        if disc < 0:
            return np.nan
        return (-B + np.sqrt(disc)) / (6.0 * C)


# ============================================================
# 3. Varredura em temperatura
# ============================================================
T_vals = np.linspace(0.3, 1.0, 800)

# Curva de segunda ordem (B > 0)
S_2nd = np.array([S_segunda_ordem(T, B_second, a, C, T_star) for T in T_vals])

# Curva de primeira ordem (B < 0): equilíbrio e metaestável
S_1st_eq   = np.array([S_primeira_ordem_equilibrio(T, B_first, a, C, T_star) for T in T_vals])
S_1st_meta = np.array([S_primeira_ordem_metaestavel(T, B_first, a, C, T_star) for T in T_vals])

# ============================================================
# 4. Temperaturas características e salto de S
# ============================================================
T_NI = T_star + B_first**2 / (27.0 * a * C)   # coexistência (1ª ordem)
S0   = -2.0 * B_first / (9.0 * C)             # salto de S em T_NI

# ============================================================
# 5. Figura de alta qualidade
# ============================================================
plt.rcParams.update({
    'font.size': 13,
    'axes.labelsize': 15,
    'axes.titlesize': 15,
    'legend.fontsize': 11,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'lines.linewidth': 2.5,
    'figure.dpi': 120,
})

fig, ax = plt.subplots(figsize=(9, 6.5))

# --- Curva de segunda ordem (B > 0) ---
ax.plot(T_vals, S_2nd, color='#1f77b4', linewidth=2.8,
        label=r'$B > 0$: transição de 2ª ordem')

# --- Curva de primeira ordem (B < 0): equilíbrio ---
ax.plot(T_vals, S_1st_eq, color='#d62728', linewidth=2.8,
        label=r'$B < 0$: transição de 1ª ordem')

# --- Ramo metaestável (tracejado) ---
ax.plot(T_vals, S_1st_meta, color='#d62728', linewidth=1.8, linestyle='--',
        alpha=0.6, label=r'$B < 0$: ramo metaestável')

# --- Linhas verticais nas temperaturas de transição ---
ax.axvline(x=T_star, color='#1f77b4', linestyle=':', linewidth=1.5, alpha=0.7)
ax.axvline(x=T_NI,   color='#d62728', linestyle=':', linewidth=1.5, alpha=0.7)

# --- Marcação do salto descontínuo em T_NI ---
ax.plot([T_NI, T_NI], [0, S0], color='#d62728', linestyle='--',
        linewidth=1.8, alpha=0.8)
ax.plot(T_NI, S0, 'o', color='#d62728', markersize=9, zorder=5)
ax.plot(T_NI, 0,  'o', color='#d62728', markersize=9,
        markerfacecolor='white', zorder=5)

# --- Anotações ---
ax.annotate(r'$T_*$', xy=(T_star, 0.02), xytext=(T_star - 0.07, 0.05),
            fontsize=14, color='#1f77b4')
ax.annotate(r'$T_{NI}$', xy=(T_NI, 0.02), xytext=(T_NI + 0.02, 0.05),
            fontsize=14, color='#d62728')
ax.annotate(r'$S_0$', xy=(T_NI, S0), xytext=(T_NI + 0.03, S0 + 0.015),
            fontsize=14, color='#d62728')

# --- Eixos e título ---
ax.set_xlabel(r'$T$', fontsize=15)
ax.set_ylabel(r'$S$', fontsize=15)
ax.set_title(r'Parâmetro de ordem $S$ em função da temperatura', fontsize=15)
ax.legend(fontsize=11, loc='upper right')
ax.grid(True, alpha=0.3)
ax.set_xlim(0.3, 1.0)
ax.set_ylim(0, 0.5)

plt.tight_layout()
plt.savefig('LdG_S_vs_T.png', dpi=300, bbox_inches='tight')
plt.show()
