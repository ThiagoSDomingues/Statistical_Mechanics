import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def eq_m(m, d, t):
    x = 2.0 * np.exp(-d / t)
    return m - x * np.sinh(m / t) / (1.0 + x * np.cosh(m / t))

t_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
d_vals = np.linspace(0.0, 0.6, 200)

plt.figure(figsize=(7, 5))
for t in t_values:
    m_vals = []
    for d in d_vals:
        try:
            # Tenta encontrar solução não-trivial
            m = fsolve(eq_m, 0.5, args=(d, t))[0]
            if m < 1e-4:
                m = 0.0
        except:
            m = 0.0
        m_vals.append(m)
    plt.plot(d_vals, m_vals, label=f't = {t:.1f}')

plt.xlabel('d = D/J')
plt.ylabel('magnetização espontânea m')
plt.title('Magnetização espontânea no modelo Blume–Capel Curie–Weiss')
plt.legend()
plt.grid(True)
plt.xlim(0, 0.6)
plt.ylim(0, 1.0)
plt.show()
