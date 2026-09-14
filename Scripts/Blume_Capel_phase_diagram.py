# =============================================================================
# Diagrama de fases do modelo de Blume-Capel em campo médio
#
# Problema 1 – Princípio variacional de Gibbs-Bogoliubov
#
# Autor: Thiago Siqueira Domingues
# Data: 2026
#
# Variáveis adimensionais:
#     t = k_B T / J
#     d = D / J
#
# Hamiltoniano:
#     H = -J sum_<ij> S_i S_j
#         + D sum_i S_i^2
#         - H sum_i S_i
#
# com S_i = -1, 0, +1.
#
# O gráfico mostra:
#   1. linha de transição de segunda ordem;
#   2. ponto tricrítico;
#   3. linha de primeira ordem obtida da energia livre
#      completa de campo médio;
#   4. término da linha de primeira ordem em T = 0;
#   5. regiões paramagnética (m = 0) e ferromagnética (m != 0).
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import brentq


# =============================================================================
# 1. Parâmetros do modelo
# =============================================================================

q = 6.0

# Número de pontos para as curvas
N_points = 1000


# =============================================================================
# 2. Pontos especiais
# =============================================================================

# Ponto tricrítico
t_tc = q / 3.0
d_tc = (q / 3.0) * np.log(4.0)

# Término da linha de primeira ordem em T = 0
t_0 = 0.0
d_0 = q / 2.0

print("Ponto tricrítico:")
print(f"t_tc = {t_tc:.8f}")
print(f"d_tc = {d_tc:.8f}")

print("\nTérmino da linha de primeira ordem:")
print(f"t_0 = {t_0:.8f}")
print(f"d_0 = {d_0:.8f}")


# =============================================================================
# 3. Linha de segunda ordem
# =============================================================================
#
# A condição B = 0 fornece
#
#       t = q x / (1+x),
#
# com
#
#       x = 2 exp(-d/t).
#
# Eliminando x:
#
#       d(t) = t ln[2(q-t)/t].
#
# Essa expressão é válida até o ponto tricrítico.
# =============================================================================

t_second = np.linspace(t_tc * 1.0e-5, t_tc, N_points)

d_second = t_second * np.log(
    2.0 * (q - t_second) / t_second
)


# =============================================================================
# 4. Linha de primeira ordem — campo médio completo
# =============================================================================
#
# Em H = 0:
#
#   f/J =
#       q m^2 / 2
#       - t ln[1 + x cosh(y)]
#
# com
#
#       y = q m / t
#       x = 2 exp(-d/t).
#
# Na coexistência:
#
#       f(m) = f(0)
#
# além da equação de estado.
#
# É conveniente parametrizar a solução por y.
#
# A equação de estado fornece
#
#       x = m / [sinh(y) - m cosh(y)].
#
# A condição de coexistência fornece uma segunda equação
# para m(y).
# =============================================================================


def coexistence_equation(m, y):
    """
    Equação que determina m(y) na linha de coexistência.

    Obtida impondo simultaneamente:
        f(m) = f(0)
    e
        df/dm = 0.

    O parâmetro y = beta J q m.
    """

    numerator = np.sinh(y)

    denominator = (
        np.sinh(y)
        + m * (1.0 - np.cosh(y))
    )

    return np.log(numerator / denominator) - 0.5 * m * y


def coexistence_m(y):
    """
    Resolve numericamente a magnetização m na coexistência
    para um dado valor de y.

    O intervalo físico satisfaz:
        0 < m < tanh(y).
    """

    m_min = 1.0e-10
    m_max = np.tanh(y) * (1.0 - 1.0e-10)

    # Criamos uma malha para localizar a raiz não trivial.
    m_grid = np.linspace(m_min, m_max, 1000)

    f_grid = np.array([
        coexistence_equation(m, y)
        for m in m_grid
    ])

    roots = []

    for i in range(len(m_grid) - 1):

        f1 = f_grid[i]
        f2 = f_grid[i + 1]

        if np.isnan(f1) or np.isnan(f2):
            continue

        if f1 * f2 < 0.0:

            root = brentq(
                coexistence_equation,
                m_grid[i],
                m_grid[i + 1],
                args=(y,)
            )

            roots.append(root)

    if len(roots) == 0:
        return np.nan

    # A raiz relevante é a não trivial.
    return roots[-1]


# Valores de y.
#
# y -> 0:
#       ponto tricrítico
#
# y -> infinito:
#       T -> 0
#       d -> q/2
#
y_values = np.linspace(0.01, 15.0, N_points)

t_first = []
d_first = []
m_first = []


for y in y_values:

    m = coexistence_m(y)

    if np.isnan(m):
        continue

    # t = q m / y
    t = q * m / y

    # Da equação de estado:
    #
    # x = m / [sinh(y) - m cosh(y)]
    #
    x = m / (
        np.sinh(y)
        - m * np.cosh(y)
    )

    if x <= 0.0:
        continue

    # x = 2 exp(-d/t)
    d = -t * np.log(x / 2.0)

    t_first.append(t)
    d_first.append(d)
    m_first.append(m)


t_first = np.array(t_first)
d_first = np.array(d_first)
m_first = np.array(m_first)


# Ordenamos os pontos para facilitar o plot.
order = np.argsort(t_first)

t_first = t_first[order]
d_first = d_first[order]
m_first = m_first[order]


# =============================================================================
# 5. Configuração visual
# =============================================================================

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 13,
    "axes.labelsize": 16,
    "axes.titlesize": 16,
    "legend.fontsize": 11,
    "xtick.labelsize": 13,
    "ytick.labelsize": 13,
    "lines.linewidth": 2.5,
    "figure.dpi": 120,
})


# =============================================================================
# 6. Figura
# =============================================================================

fig, ax = plt.subplots(
    figsize=(9.0, 6.8)
)


# =============================================================================
# 7. Regiões do diagrama
# =============================================================================

# Região de baixa temperatura / ferromagnética
#
# Fazemos apenas um preenchimento qualitativo abaixo das linhas.
ax.fill_between(
    t_second,
    0.0,
    d_second,
    alpha=0.08,
    label=None
)


# =============================================================================
# 8. Linha de segunda ordem
# =============================================================================

ax.plot(
    t_second,
    d_second,
    linewidth=3.0,
    label=r"Transição de 2ª ordem ($B=0,\ C>0$)"
)


# =============================================================================
# 9. Linha de primeira ordem
# =============================================================================

ax.plot(
    t_first,
    d_first,
    linewidth=3.0,
    linestyle="--",
    label=r"Transição de 1ª ordem"
)


# =============================================================================
# 10. Ponto tricrítico
# =============================================================================

ax.plot(
    t_tc,
    d_tc,
    marker="o",
    markersize=9,
    markerfacecolor="white",
    markeredgewidth=2.2,
    zorder=10,
    label=r"Ponto tricrítico"
)


# =============================================================================
# 11. Ponto T = 0
# =============================================================================

ax.plot(
    t_0,
    d_0,
    marker="o",
    markersize=9,
    zorder=10
)


# =============================================================================
# 12. Linha vertical indicando d = q/2
# =============================================================================

ax.axhline(
    d_0,
    linestyle=":",
    linewidth=1.5,
    alpha=0.7
)


# =============================================================================
# 13. Anotações
# =============================================================================

ax.annotate(
    r"$\mathrm{TC}$",
    xy=(t_tc, d_tc),
    xytext=(t_tc + 0.18, d_tc + 0.10),
    fontsize=15
)


ax.annotate(
    r"$T=0,\ d=q/2$",
    xy=(t_0, d_0),
    xytext=(0.35, d_0 + 0.10),
    fontsize=13
)


# Região paramagnética / m = 0
ax.text(
    2.9,
    1.5,
    r"$m=0$",
    fontsize=16
)


# Região ferromagnética
ax.text(
    0.75,
    3.5,
    r"$m\neq0$",
    fontsize=16
)


# =============================================================================
# 14. Eixos
# =============================================================================

ax.set_xlabel(
    r"$t = k_B T/J$"
)

ax.set_ylabel(
    r"$d = D/J$"
)


# =============================================================================
# 15. Limites do gráfico
# =============================================================================

ax.set_xlim(
    0.0,
    2.35
)

ax.set_ylim(
    0.0,
    3.35
)


# =============================================================================
# 16. Grade
# =============================================================================

ax.grid(
    True,
    alpha=0.25,
    linewidth=0.8
)


# =============================================================================
# 17. Legenda
# =============================================================================

ax.legend(
    loc="upper right",
    frameon=True
)


# =============================================================================
# 18. Título
# =============================================================================

ax.set_title(
    r"Diagrama de fases do modelo de Blume--Capel "
    r"(campo médio, $q=6$)"
)


# =============================================================================
# 19. Layout e salvamento
# =============================================================================

plt.tight_layout()

plt.savefig(
    "Blume_Capel_phase_diagram.png",
    dpi=400,
    bbox_inches="tight"
)

plt.savefig(
    "Blume_Capel_phase_diagram.pdf",
    bbox_inches="tight"
)


plt.show()
