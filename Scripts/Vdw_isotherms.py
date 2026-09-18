import matplotlib.pyplot as plt
import numpy as np

# Configurações globais de estilo para alta qualidade
plt.rcParams.update(
    {
        "font.size": 12,
        "axes.labelsize": 13,
        "axes.titlesize": 14,
        "xtick.labelsize": 11,
        "ytick.labelsize": 11,
        "figure.dpi": 300,  # Alta resolução
        "text.usetex": False,  # Altere para True se tiver LaTeX instalado no sistema
    }
)

# Intervalo da densidade de ocupação (rho) de 0 até próximo de 1
rho = np.linspace(0.001, 0.99, 500)


# Equação de estado correta: p/epsilon = -t * ln(1 - rho) - 0.5 * rho^2
def p_reduced(rho, t):
    return -t * np.log(1 - rho) - 0.5 * rho**2


# Temperaturas reduzidas t = k_B T / epsilon (Temperatura crítica tc = 0.25)
t_sub = 0.18  # Subcrítica (t < tc)
t_crit = 0.25  # Crítica (t = tc)
t_super = 0.35  # Supercrítica (t > tc)

# Criação da figura
fig, ax = plt.subplots(figsize=(8, 5.5))

# Plotagem das isotermas
ax.plot(
    rho,
    p_reduced(rho, t_sub),
    color="#1f77b4",
    linewidth=2.5,
    label=r"$t = 0{,}18$ (subcrítica)",
)
ax.plot(
    rho,
    p_reduced(rho, t_crit),
    color="#d62728",
    linewidth=2.5,
    label=r"$t = 0{,}25$ ($t_c$ crítica)",
)
ax.plot(
    rho,
    p_reduced(rho, t_super),
    color="#2ca02c",
    linewidth=2.5,
    label=r"$t = 0{,}35$ (supercrítica)",
)

# Linha horizontal de referência em p = 0
ax.axhline(0, color="gray", linestyle="--", linewidth=1, alpha=0.6)

# Destaque do Ponto Crítico (rho_c = 0.5)
rho_c = 0.5
p_c = p_reduced(rho_c, t_crit)
ax.plot(rho_c, p_c, "ko", markersize=6, zorder=5)
ax.annotate(
    r"Ponto Crítico ($\rho_c=0{,}5$)",
    xy=(rho_c, p_c),
    xytext=(rho_c - 0.25, p_c + 0.035),
    arrowprops=dict(
        arrowstyle="->", color="black", lw=1.2, connectionstyle="arc3,rad=0.2"
    ),
    fontsize=11,
)

# Ajuste dos limites dos eixos
ax.set_xlim(0, 1)
ax.set_ylim(-0.05, 0.4)

# Rótulos e Título
ax.set_xlabel(r"$\rho$", labelpad=8)
ax.set_ylabel(r"$p / \epsilon$", labelpad=8)
ax.set_title("Isotermas do Gás de Rede de van der Waals", pad=12)

# Grade e Moldura
ax.grid(True, linestyle="--", alpha=0.35, color="#888888")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Legenda
ax.legend(
    frameon=True,
    facecolor="white",
    framealpha=0.9,
    edgecolor="none",
    loc="upper left",
    fontsize=11,
)

plt.tight_layout()

# Salvando a figura em PNG de alta definição e em PDF vetorial
plt.savefig("isotermas_vdW.png", dpi=300, bbox_inches="tight")
plt.savefig("isotermas_vdW.pdf", bbox_inches="tight")  # Formato vetorial ideal para artigos/LaTeX

plt.show()
