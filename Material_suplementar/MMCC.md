### Python code

"""
metropolis_ising.py
===================
Simulação de Monte Carlo pelo algoritmo de Metropolis para o modelo de Ising 2D
na rede quadrada, a campo nulo, com condições de contorno periódicas.

Gera a Figura no estilo de Landau (PRB 13, 2997, 1976):
  <|m|> vs k_B T / J  para N = 4, 10, 20, 30, 40, 60, 100
comparando com a magnetização espontânea exata de Yang (Phys. Rev. 85, 808, 1952).

Uso:
    python metropolis_ising.py

Parâmetros principais (ajustáveis na seção PARÂMETROS abaixo):
    SEED        semente do gerador de números pseudoaleatórios
    N_TERM      número de MCS de termalização (descartados)
    N_MEAS      número de MCS de medida
    N_TEMPS     número de temperaturas na varredura
    T_MIN, T_MAX  intervalo de temperaturas reduzidas k_B T / J
    SIZES       lista de tamanhos lineares N da rede
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

# ─────────────────────────────────────────────────────────────────────────────
# PARÂMETROS
# ─────────────────────────────────────────────────────────────────────────────
SEED   = 42          # semente do gerador (documentar no artigo)
N_TERM = 2000        # MCS de termalização (descartados)
N_MEAS = 4000        # MCS de medida
T_MIN  = 1.0         # temperatura reduzida mínima
T_MAX  = 3.8         # temperatura reduzida máxima
N_TEMPS = 50         # número de temperaturas na varredura
N_BLOCKS = 20        # blocos para estimativa de erro (blocagem)

# Tamanhos de rede a simular (estilo Landau 1976)
SIZES = [4, 10, 20, 30, 40, 60, 100]

# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTE FÍSICA
# ─────────────────────────────────────────────────────────────────────────────
# Temperatura crítica exata (Onsager 1944 / Kramers-Wannier 1941):
#   k_B T_c / J = 2 / ln(1 + sqrt(2)) ≈ 2.269185
THETA_C = 2.0 / np.log(1.0 + np.sqrt(2.0))

# ─────────────────────────────────────────────────────────────────────────────
# MAGNETIZAÇÃO ESPONTÂNEA EXATA — Yang, Phys. Rev. 85, 808 (1952)
# m_inf(T) = [1 - sinh^{-4}(2/T)]^{1/8}  para T < T_c,  0 acima
# ─────────────────────────────────────────────────────────────────────────────
def m_exact(theta_arr):
    """Magnetização espontânea exata no limite termodinâmico (Yang 1952)."""
    theta_arr = np.asarray(theta_arr, dtype=float)
    m = np.zeros_like(theta_arr)
    mask = theta_arr < THETA_C
    x = np.sinh(2.0 / theta_arr[mask])
    m[mask] = (1.0 - x**(-4)) ** 0.125
    return m

# ─────────────────────────────────────────────────────────────────────────────
# VARREDURA DE METROPOLIS  (passo de Monte Carlo = 1 MCS = N² tentativas)
# ─────────────────────────────────────────────────────────────────────────────
def metropolis_sweep(spins, exp_neg4, exp_neg8, rng):
    """
    Uma varredura completa: visita sequencialmente todos os N² sítios.

    Parâmetros
    ----------
    spins      : np.ndarray (N, N), dtype=int8, valores ±1
    exp_neg4   : float = exp(-4/theta)   (pré-calculado fora do loop)
    exp_neg8   : float = exp(-8/theta)
    rng        : numpy.random.Generator

    Retorno
    -------
    magnetização por sítio desta configuração (float)
    """
    N = spins.shape[0]
    N2 = N * N
    rand_u = rng.random(N2)   # números aleatórios uniformes em [0,1)
    idx = 0
    for i in range(N):
        ip = (i + 1) % N
        im = (i - 1) % N
        for j in range(N):
            jp = (j + 1) % N
            jm = (j - 1) % N
            S_nn = (spins[ip, j] + spins[im, j] +
                    spins[i, jp] + spins[i, jm])
            dE_over_J = 2 * spins[i, j] * S_nn   # ΔE/J ∈ {-8,-4,0,4,8}
            if dE_over_J <= 0:
                spins[i, j] *= -1
            elif dE_over_J == 4:
                if rand_u[idx] < exp_neg4:
                    spins[i, j] *= -1
            else:   # dE_over_J == 8
                if rand_u[idx] < exp_neg8:
                    spins[i, j] *= -1
            idx += 1
    return spins.sum() / N2    # magnetização por sítio

# ─────────────────────────────────────────────────────────────────────────────
# SIMULAÇÃO: retorna <|m|> e seu erro por blocagem
# ─────────────────────────────────────────────────────────────────────────────
def simulate(N, theta, n_term, n_meas, n_blocks, rng):
    """
    Retorna (mean_abs_m, err_abs_m) para uma rede N×N à temperatura theta.

    Protocolo
    ---------
    1. Inicialização ordenada: todos os spins +1.
    2. n_term MCS de termalização (descartados).
    3. n_meas MCS de medida; |m_k| coletado após cada varredura.
    4. Erro estimado por blocagem em n_blocks blocos (Flyvbjerg & Petersen 1989).
    """
    beta  = 1.0 / theta
    exp4  = np.exp(-4.0 * beta)
    exp8  = np.exp(-8.0 * beta)

    # Condição inicial ordenada (estado ferromagnético)
    spins = np.ones((N, N), dtype=np.int8)

    # Termalização
    for _ in range(n_term):
        metropolis_sweep(spins, exp4, exp8, rng)

    # Medidas
    abs_m = np.empty(n_meas)
    for k in range(n_meas):
        m_k = metropolis_sweep(spins, exp4, exp8, rng)
        abs_m[k] = abs(m_k)

    mean_m = abs_m.mean()

    # Erro por blocagem
    block_size = n_meas // n_blocks
    block_means = (abs_m[:n_blocks * block_size]
                   .reshape(n_blocks, block_size)
                   .mean(axis=1))
    err_m = block_means.std(ddof=1) / np.sqrt(n_blocks)

    return mean_m, err_m

# ─────────────────────────────────────────────────────────────────────────────
# LOOP PRINCIPAL: simular para cada (N, T)
# ─────────────────────────────────────────────────────────────────────────────
temperatures = np.linspace(T_MIN, T_MAX, N_TEMPS)

results = {}   # results[N] = (mean_m_arr, err_m_arr)

for N in SIZES:
    rng = np.random.default_rng(SEED)   # reinicia a semente para cada N
    mean_arr = np.empty(N_TEMPS)
    err_arr  = np.empty(N_TEMPS)
    print(f"\nRede {N:3d}×{N:<3d}  |  N_term={N_TERM}  N_meas={N_MEAS}")
    for k, theta in enumerate(temperatures):
        mean_arr[k], err_arr[k] = simulate(N, theta, N_TERM, N_MEAS,
                                           N_BLOCKS, rng)
        print(f"  θ={theta:.3f}   ⟨|m|⟩={mean_arr[k]:.4f} ± {err_arr[k]:.4f}")
    results[N] = (mean_arr, err_arr)

# ─────────────────────────────────────────────────────────────────────────────
# CURVA EXATA (Yang 1952)
# ─────────────────────────────────────────────────────────────────────────────
theta_exact = np.linspace(T_MIN, T_MAX, 800)
m_ex = m_exact(theta_exact)

# ─────────────────────────────────────────────────────────────────────────────
# GRÁFICO   (estilo Landau, PRB 13, 2997, 1976)
# ─────────────────────────────────────────────────────────────────────────────
# Paleta de cores distinta para cada tamanho
cmap = plt.cm.viridis
colors = [cmap(i / (len(SIZES) - 1)) for i in range(len(SIZES))]
markers = ['o', 's', '^', 'D', 'v', 'P', '*']

fig, ax = plt.subplots(figsize=(8, 5.5))

# Curva exata
ax.plot(theta_exact, m_ex,
        color='black', lw=2.0, zorder=10,
        label=r'Exata — Yang (1952), $N\to\infty$')

# Linha da temperatura crítica
ax.axvline(THETA_C, color='gray', ls='--', lw=1.0,
           label=rf'$\widetilde{{T}}_c \approx {THETA_C:.4f}$')

# Pontos simulados
for (N, (mean_arr, err_arr)), color, marker in zip(results.items(), colors, markers):
    ax.errorbar(temperatures, mean_arr, yerr=err_arr,
                fmt=marker, ms=4.5, color=color,
                ecolor=color, elinewidth=0.8, capsize=2.5,
                label=rf'$N={N}$')

ax.set_xlabel(r'$\widetilde{T} = k_BT/J$', fontsize=14)
ax.set_ylabel(r'$\langle |m| \rangle$', fontsize=14)
ax.set_title(
    r'Magnetização — Modelo de Ising 2D  (estilo Landau 1976)',
    fontsize=13)
ax.set_xlim(T_MIN, T_MAX)
ax.set_ylim(-0.02, 1.05)
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.legend(fontsize=9, ncol=2, loc='upper right',
          framealpha=0.9, edgecolor='gray')
ax.grid(True, which='major', alpha=0.25)

# Anotação dos parâmetros da simulação (transparência)
param_text = (
    f"semente = {SEED}\n"
    f"$N_{{\\rm term}}$ = {N_TERM} MCS\n"
    f"$N_{{\\rm meas}}$ = {N_MEAS} MCS\n"
    f"erro: blocagem ({N_BLOCKS} blocos)"
)
ax.text(0.02, 0.04, param_text,
        transform=ax.transAxes, fontsize=8,
        va='bottom', ha='left',
        bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.7, ec='gray'))

fig.tight_layout()
fig.savefig('fig_ising_magnetizacao.png', dpi=200, bbox_inches='tight')
plt.show()
print("\nFigura salva em: fig_ising_magnetizacao.png")

-----

### Results 

