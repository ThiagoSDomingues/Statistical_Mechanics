# ===============================================================================
# Código para gerar a Função de correlação para regimes monotônico e oscilatório
# Problema 3, item (iii) – Lista 2
# Autor: Thiago Siqueira Domingues
# ===============================================================================

import numpy as np
import matplotlib.pyplot as plt

def build_annni_matrix(K, p):
    """Constrói a matriz de transferência 4x4 do modelo ANNNI."""
    T = np.zeros((4, 4))
    T[0, 0] = np.exp(K * (1 - p))
    T[0, 1] = np.exp(K * (p - 1))
    T[1, 2] = np.exp(-K * (1 + p))
    T[1, 3] = np.exp(K * (1 + p))
    T[2, 0] = np.exp(K * (1 + p))
    T[2, 1] = np.exp(-K * (1 + p))
    T[3, 2] = np.exp(K * (p - 1))
    T[3, 3] = np.exp(K * (1 - p))
    return T

def correlation_annni(K, p, r_max=50):
    """
    Calcula C(r) = <sigma_0 sigma_r> usando a decomposição espectral da matriz T.
    """
    T = build_annni_matrix(K, p)
    
    # Autovalores e autovetores (direita e esquerda)
    eigvals, eigvecs_right = np.linalg.eig(T)
    idx = np.argsort(np.abs(eigvals))[::-1]  # ordena por módulo decrescente
    eigvals = eigvals[idx]
    eigvecs_right = eigvecs_right[:, idx]
    
    # Autovetores à esquerda (linhas da inversa da matriz de autovetores)
    eigvecs_left = np.linalg.inv(eigvecs_right)
    
    # Operador O = diag(+1, +1, -1, -1) que mede o primeiro spin do par
    O_mat = np.diag([1, 1, -1, -1])
    
    # Coeficientes c_n = <L1|O|Rn> * <Ln|O|R1>
    R1 = eigvecs_right[:, 0]
    L1 = eigvecs_left[0, :]  # linha 0
    c = np.zeros(4)
    for n in range(4):
        Rn = eigvecs_right[:, n]
        Ln = eigvecs_left[n, :]
        c[n] = np.dot(L1, O_mat @ Rn) * np.dot(Ln, O_mat @ R1)
    
    # Calcular C(r)
    r_vals = np.arange(0, r_max + 1)
    C_r = np.zeros_like(r_vals, dtype=float)
    lam1 = eigvals[0]
    for n in range(4):
        C_r += c[n] * (eigvals[n] / lam1)**r_vals
    
    return r_vals, np.real(C_r)

# Parâmetros
K = 1.2  # beta J
p_list = [0.2, 1.5]  # p < 0.5 (monotônico) e p > 0.5 (oscilatório)
r_max = 30

# Plot
plt.figure(figsize=(8, 6))
for p in p_list:
    r, C = correlation_annni(K, p, r_max)
    plt.semilogy(r, C, 'o-', linewidth=2, markersize=4, label=f'p = {p:.1f}')

plt.xlabel('Distância $r$', fontsize=14)
plt.ylabel('$\\langle \\sigma_0 \\sigma_r \\rangle$', fontsize=14)
plt.title(f'Função de correlação do modelo ANNNI para $K = {K:.1f}$', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('annni_correlation.png', dpi=300)
plt.show()
