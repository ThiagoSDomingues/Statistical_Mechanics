import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# ---------- Configurações Gerais ----------
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'figure.dpi': 150
})

q = 6.0  # Número de coordenação (Rede cúbica simples)

# ---------- Ponto Tricrítico (Analítico) ----------
t_tc = q / 3.0                                  # t_tc = 2.0
d_tc = (q / 3.0) * np.log(4.0)                 # d_tc = 4*ln(2) ≈ 2.7726

# ---------- Linha de 2ª Ordem (Analítica: B=0, C>0) ----------
# d(t) = t * ln(2*(q-t)/t), válida de t_tc=2.0 até t=2q/3=4.0 (onde d=0)
t2 = np.linspace(t_tc, 2.0 * q / 3.0, 400)
d2 = t2 * np.log(2.0 * (q - t2) / t2)

# ---------- Linha de 1ª Ordem (Numérica: g(m)=g(0) e dg/dm=0) ----------
def equations_md(vars, m, q_val=6.0):
    t, d = vars
    x = 2.0 * np.exp(-d / t)
    eq1 = m - (x * np.sinh(q_val * m / t)) / (1.0 + x * np.cosh(q_val * m / t))
    eq2 = 0.5 * q_val * m**2 - t * np.log((1.0 + x * np.cosh(q_val * m / t)) / (1.0 + x))
    return [eq1, eq2]

m_vals = np.linspace(1e-4, 0.9999, 400)
t_prev, d_prev = t_tc, d_tc
t_first, d_first = [], []

for m in m_vals:
    sol, info, ier, msg = fsolve(equations_md, [t_prev, d_prev], args=(m, q),
                                 full_output=True, xtol=1e-12)
    if ier == 1 and 0 <= sol[0] <= t_tc and 0 <= sol[1] <= q:
        t_prev, d_prev = sol
        t_first.append(sol[0])
        d_first.append(sol[1])

# Conecta aos limites teóricos: (t_tc, d_tc) e (t=0, d=q/2=3)
t_first = np.concatenate(([t_tc], t_first, [0.0]))
d_first = np.concatenate(([d_tc], d_first, [q / 2.0]))

# Curva completa para sombreamento da fase ordenada
t_full = np.concatenate((t_first[::-1], t2))
d_full = np.concatenate((d_first[::-1], d2))

# ---------- Construção do Gráfico ----------
fig, ax = plt.subplots(figsize=(7.5, 5.5))

# Curvas de transição
ax.plot(t2, d2, '-', color='#1f77b4', linewidth=2.5, 
        label=r'Transição de 2ª ordem ($B=0, C>0$)')
ax.plot(t_first, d_first, '--', color='red', linewidth=2.5, 
        label=r'Transição de 1ª ordem ($B=0, C<0$)')

# Pontos notáveis
ax.plot(t_tc, d_tc, 'o', color='#2ca02c', markersize=9, zorder=5, 
        label=fr'Ponto tricrítico $(t={t_tc:.0f}, d \approx {d_tc:.3f})$')
ax.plot(0.0, q / 2.0, 'o', color='black', markersize=8, zorder=5, 
        label=r'Fim da linha de coexistência $(t=0, d=3)$')

# Sombreamento das fases
ax.fill_between(t_full, d_full, 0, color='#1f77b4', alpha=0.08)

# Rótulos das fases
ax.text(1.2, 1.0, 'Fase Ferromagnética\n(ordenada, $m_0 > 0$)', 
        ha='center', va='center', fontsize=11, color='#1f4e79', fontweight='bold')
ax.text(1.2, 3.4, 'Fase Paramagnética\n(desordenada, $m_0 = 0$)', 
        ha='center', va='center', fontsize=11, color='#7a1f1f', fontweight='bold')

# Estilização
ax.set_xlabel(r'$t = k_B T / J$')
ax.set_ylabel(r'$d = D / J$')
ax.set_title(r'Diagrama de Fases do Modelo de Blume–Capel ($q=6$)', pad=12)

ax.set_xlim(0, 4.2)
ax.set_ylim(0, 4.0)

ax.grid(True, linestyle='--', alpha=0.4, color='#888888')
ax.legend(frameon=True, facecolor='white', framealpha=0.95, loc='upper right', fontsize=9.5)

plt.tight_layout()
plt.savefig('Blume_Capel_phase_diagram_MF.png', dpi=300)
plt.show()
