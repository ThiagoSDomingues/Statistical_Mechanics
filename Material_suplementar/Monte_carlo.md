import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# 1. Solução Exata de Onsager / Yang para a Magnetização no Limite Termodinâmico
# -----------------------------------------------------------------------------
def onsager_exact(T):
    # Considera-se J/k_B = 1
    Tc = 2.0 / np.log(1.0 + np.sqrt(2.0))  # ~ 2.2691857
    m_exact = np.zeros_like(T)
    mask = T < Tc
    m_exact[mask] = (1.0 - np.sinh(2.0 / T[mask])**(-2))**(1.0 / 8.0)
    return m_exact, Tc

# -----------------------------------------------------------------------------
# 2. Algoritmo de Metropolis para a Rede Quadrada 2D
# -----------------------------------------------------------------------------
def simulate_ising_2d(L, temperatures, mcs_thermalization=300, mcs_measurement=600):
    N = L * L
    mag_means = []
    mag_errors = []
    
    # Condição inicial: spins ferromagnéticos (todos +1)
    spins = np.ones((L, L), dtype=np.int8)
    
    for T in temperatures:
        # Tabela pré-calculada do fator de Boltzmann para dE em {-8, -4, 0, 4, 8}
        prob = {dE: np.exp(-dE / T) if dE > 0 else 1.0 for dE in [-8, -4, 0, 4, 8]}
        
        # --- Fase 1: Termalização (Atingir o equilíbrio) ---
        for mcs in range(mcs_thermalization):
            for i in range(L):
                for j in range(L):
                    s = spins[i, j]
                    # Condições de contorno periódicas
                    neighbors = spins[(i+1)%L, j] + spins[(i-1)%L, j] + spins[i, (j+1)%L] + spins[i, (j-1)%L]
                    dE = 2 * s * neighbors
                    
                    if dE <= 0 or np.random.rand() < prob[dE]:
                        spins[i, j] = -s
                        
        # --- Fase 2: Medição de Equilíbrio ---
        m_samples = []
        for mcs in range(mcs_measurement):
            for i in range(L):
                for j in range(L):
                    s = spins[i, j]
                    neighbors = spins[(i+1)%L, j] + spins[(i-1)%L, j] + spins[i, (j+1)%L] + spins[i, (j-1)%L]
                    dE = 2 * s * neighbors
                    
                    if dE <= 0 or np.random.rand() < prob[dE]:
                        spins[i, j] = -s
            
            # Armazena o módulo da magnetização por spin: |M| / N
            m_samples.append(np.abs(np.sum(spins)) / N)
            
        m_samples = np.array(m_samples)
        mag_means.append(np.mean(m_samples))
        # Estimativa simples do erro padrão da média
        mag_errors.append(np.std(m_samples) / np.sqrt(len(m_samples)))
        
    return np.array(mag_means), np.array(mag_errors)

# -----------------------------------------------------------------------------
# 3. Execução das Simulações e Comparação com a Solução Exata
# -----------------------------------------------------------------------------
# Intervalo de Temperatura (em unidades de J / k_B)
T_vals = np.linspace(1.2, 3.5, 24)
m_onsager, Tc = onsager_exact(T_vals)

# Tamanhos de rede para testar os Efeitos de Tamanho Finito
lattice_sizes = [4, 10, 20]
results = {}

print("Iniciando simulações de Monte Carlo...")
for L in lattice_sizes:
    print(f"Simulando para L = {L}...")
    m_mean, m_err = simulate_ising_2d(L, T_vals, mcs_thermalization=400, mcs_measurement=800)
    results[L] = (m_mean, m_err)

# -----------------------------------------------------------------------------
# 4. Geração do Gráfico estilo Landau (1976)
# -----------------------------------------------------------------------------
plt.figure(figsize=(9, 6))

# Solução Exata de Onsager (Linha Pontilhada/Tracejada)
plt.plot(T_vals, m_onsager, 'k--', label='Solução Exata (Onsager)', linewidth=2)

# Resultados de Monte Carlo
markers = ['o', 's', '^']
for idx, L in enumerate(lattice_sizes):
    m_mean, m_err = results[L]
    plt.errorbar(T_vals, m_mean, yerr=m_err, fmt=markers[idx] + '-', 
                 label=f'Monte Carlo (L = {L})', capsize=3, alpha=0.85)

# Linha vertical na Temperatura Crítica Exata
plt.axvline(Tc, color='gray', linestyle=':', label=f'$T_c \\approx {Tc:.3f} J/k_B$')

plt.xlabel('Temperatura ($k_B T / J$)', fontsize=12)
plt.ylabel('Magnetização Média $\\langle |m| \\rangle$', fontsize=12)
plt.title('Modelo de Ising 2D: Comportamento de Tamanho Finito (Landau, 1976)', fontsize=13)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
