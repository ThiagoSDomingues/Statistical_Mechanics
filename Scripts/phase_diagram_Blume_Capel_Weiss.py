import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Segunda ordem: B = 0
# Parametrizamos por x = 2 exp(-d/t)
x_vals = np.linspace(0.5, 2.0, 200)
t2 = x_vals / (1.0 + x_vals)
d2 = -t2 * np.log(x_vals / 2.0)

# Ordena por d
idx = np.argsort(d2)
d2 = d2[idx]
t2 = t2[idx]

# Ponto tricrítico
d_tc = (2.0/3.0) * np.log(2.0)
t_tc = 1.0/3.0

# Primeira ordem: resolver g(m)=g(0) e g'(m)=0
def equations(vars, d):
    t, m = vars
    x = 2.0 * np.exp(-d / t)
    eq1 = m - x * np.sinh(m / t) / (1.0 + x * np.cosh(m / t))
    eq2 = 0.5 * m**2 - t * np.log((1.0 + x * np.cosh(m / t)) / (1.0 + x))
    return [eq1, eq2]

d_first = np.linspace(d_tc + 1e-4, 0.5 - 1e-4, 80)
t_first = []
for d in d_first:
    # Chute inicial: próximo ao ponto tricrítico
    t0 = 0.3 if d < 0.48 else 0.1
    m0 = 0.5
    sol = fsolve(equations, [t0, m0], args=(d,))
    t_first.append(sol[0])
t_first = np.array(t_first)

# Gráfico
plt.figure(figsize=(7, 5))
plt.plot(d2, t2, 'b-', linewidth=2, label='2ª ordem (B=0, C>0)')
plt.plot(d_first, t_first, 'r--', linewidth=2, label='1ª ordem')
plt.plot(d_tc, t_tc, 'go', markersize=8, label='Ponto tricrítico')
plt.plot(0.5, 0.0, 'ko', markersize=8, label='T=0, d=1/2')
plt.xlabel('d = D/J')
plt.ylabel('t = k_B T / J')
plt.title('Diagrama de fases Blume–Capel Curie–Weiss')
plt.legend()
plt.grid(True)
plt.xlim(0, 0.6)
plt.ylim(0, 0.8)
plt.show()
