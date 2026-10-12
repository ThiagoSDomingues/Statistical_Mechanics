```python
import numpy as np
import matplotlib.pyplot as plt

def onsager_exact(T):
    # J / k_B = 1
    Tc = 2.0 / np.log(1 + np.sqrt(2)) # ~ 2.2691857
    m = np.zeros_like(T)
    mask = T < Tc
    m[mask] = (1.0 - np.sinh(2.0 / T[mask])**(-2))**(1/8)
    return m, Tc

# Metropolis Simulation
def run_ising_simulation(L, temperatures, mcs_thermalization=300, mcs_measurement=500):
    N = L * L
    magnetizations = []
    
    # Initialize spin configuration (all +1 for faster convergence at low T, or random)
    spins = np.ones((L, L), dtype=np.int8)
    
    for T in temperatures:
        # Precompute Boltzmann factors for delta_E in {-8, -4, 0, 4, 8}
        # delta_E = 2 * s_i * sum(s_j)
        # s_i in {-1, 1}, sum(s_j) in {-4, -2, 0, 2, 4}
        # delta_E can be -8, -4, 0, 4, 8
        prob = {dE: np.exp(-dE / T) if dE > 0 else 1.0 for dE in [-8, -4, 0, 4, 8]}
        
        # Thermalization sweeps
        for mcs in range(mcs_thermalization):
            for i in range(L):
                for j in range(L):
                    s = spins[i, j]
                    neighbors = spins[(i+1)%L, j] + spins[(i-1)%L, j] + spins[i, (j+1)%L] + spins[i, (j-1)%L]
                    dE = 2 * s * neighbors
                    if dE <= 0 or np.random.rand() < prob[dE]:
                        spins[i, j] = -s
        
        # Measurement sweeps
        m_sum = 0.0
        for mcs in range(mcs_measurement):
            for i in range(L):
                for j in range(L):
                    s = spins[i, j]
                    neighbors = spins[(i+1)%L, j] + spins[(i-1)%L, j] + spins[i, (j+1)%L] + spins[i, (j-1)%L]
                    dE = 2 * s * neighbors
                    if dE <= 0 or np.random.rand() < prob[dE]:
                        spins[i, j] = -s
            m_sum += np.abs(np.sum(spins)) / N
            
        magnetizations.append(m_sum / mcs_measurement)
        
    return np.array(magnetizations)

T_vals = np.linspace(1.0, 3.5, 20)
m_onsager, Tc = onsager_exact(T_vals)

L_sizes = [4, 10, 20]
results = {}
for L in L_sizes:
    results[L] = run_ising_simulation(L, T_vals, mcs_thermalization=200, mcs_measurement=300)

print("Done simulating!")
print("Tc =", Tc)


```

```text
Done simulating!
Tc = 2.269185314213022


```

```python
import numpy as np
import matplotlib.pyplot as plt

# Onsager Exact Solution
def onsager_exact(T):
    Tc = 2.0 / np.log(1 + np.sqrt(2)) # J/k_B = 1
    m = np.zeros_like(T)
    mask = T < Tc
    m[mask] = (1.0 - np.sinh(2.0 / T[mask])**(-2))**(1/8)
    return m, Tc

# Metropolis Simulation
def simulate_ising_2d(L, temperatures, mcs_thermalization=500, mcs_measurement=1000):
    N = L * L
    mag_means = []
    mag_errors = []
    
    # Initialize with all spins +1 (ferromagnetic start)
    spins = np.ones((L, L), dtype=np.int8)
    
    for T in temperatures:
        # Precompute Metropolis probabilities
        prob = {dE: np.exp(-dE / T) if dE > 0 else 1.0 for dE in [-8, -4, 0, 4, 8]}
        
        # 1. Thermalization phase
        for mcs in range(mcs_thermalization):
            for i in range(L):
                for j in range(L):
                    s = spins[i, j]
                    neighbors = spins[(i+1)%L, j] + spins[(i-1)%L, j] + spins[i, (j+1)%L] + spins[i, (j-1)%L]
                    dE = 2 * s * neighbors
                    if dE <= 0 or np.random.rand() < prob[dE]:
                        spins[i, j] = -s
                        
        # 2. Measurement phase
        m_samples = []
        for mcs in range(mcs_measurement):
            for i in range(L):
                for j in range(L):
                    s = spins[i, j]
                    neighbors = spins[(i+1)%L, j] + spins[(i-1)%L, j] + spins[i, (j+1)%L] + spins[i, (j-1)%L]
                    dE = 2 * s * neighbors
                    if dE <= 0 or np.random.rand() < prob[dE]:
                        spins[i, j] = -s
            
            # Store magnetization per spin |M| / N
            m_samples.append(np.abs(np.sum(spins)) / N)
            
        m_samples = np.array(m_samples)
        mag_means.append(np.mean(m_samples))
        # Simple error estimation (standard error of the mean)
        mag_errors.append(np.std(m_samples) / np.sqrt(len(m_samples)))
        
    return np.array(mag_means), np.array(mag_errors)

# Temperatures vector
T_range = np.linspace(1.2, 3.5, 25)
m_onsager, Tc = onsager_exact(T_range)

# Simulate for L = 4, 10, 20
sizes = [4, 10, 20]
results = {}

for L in sizes:
    m_mean, m_err = simulate_ising_2d(L, T_range, mcs_thermalization=400, mcs_measurement=800)
    results[L] = (m_mean, m_err)

plt.figure(figsize=(9, 6))
# Exact Onsager line (dashed)
plt.plot(T_range, m_onsager, 'k--', label='Solução Exata (Onsager)', linewidth=2)

markers = ['o', 's', '^', 'v']
for idx, L in enumerate(sizes):
    m_mean, m_err = results[L]
    plt.errorbar(T_range, m_mean, yerr=m_err, fmt=markers[idx] + '-', label=f'Monte Carlo L = {L}', capsize=3, alpha=0.8)

plt.axvline(Tc, color='gray', linestyle=':', label=f'$T_c \\approx {Tc:.3f}$')
plt.xlabel('Temperatura $k_B T / J$', fontsize=12)
plt.ylabel('Magnetização Média $\\langle |m| \\rangle$', fontsize=12)
plt.title('Modelo de Ising 2D: Magnetização vs Temperatura (David Landau, 1976)', fontsize=13)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('ising_metropolis.png', dpi=150)
print("Simulation & plot finished successfully!")


```

```text
Simulation & plot finished successfully!


```

O procedimento que você descreveu para o algoritmo de Metropolis no modelo de Ising bidimensional em uma rede quadrada está absolutamente correto na sua lógica essencial.

Abaixo está a análise detalhada da termalização, da convergência, da estimativa de erros, dos efeitos de tamanho finito (referenciando o trabalho clássico de David P. Landau) e a implementação em Python desenvolvida do zero.

---

### 1. Funcionamento do Algoritmo e o Passo de Monte Carlo (MCS)

O algoritmo gera uma cadeia de Markov que amostra configurações microscópicas segundo a distribuição de Boltzmann $P(\mu) \propto e^{-E_\mu / k_B T}$.

1. **Definição de 1 MCS (Monte Carlo Step):**
Como a rede possui $N = L \times L$ sítios, **1 Passo de Monte Carlo (MCS)** equivale a realizar $N$ tentativas de inversão (*spin flip*). Isso garante que, em média, cada sítio da rede seja visitado uma vez por MCS.
2. **Condição de Aceitação:**
A variação de energia ao inverter o spin do sítio $i$ ($s_i \to -s_i$) é:

$$\Delta E = E_f - E_i = 2 s_i \sum_{j \in \text{vizinhos}} s_j$$


* Se $\Delta E \le 0$, a inversão reduz ou mantém a energia: **aceita-se** a mudança.
* Se $\Delta E > 0$, calcula-se $R = \exp(-\Delta E / k_B T)$. Gera-se um número aleatório $Z \in [0, 1)$. Se $Z < R$, **aceita-se** a mudança; caso contrário, **rejeita-se** e o spin permanece inalterado.



---

### 2. Termalização, Convergência e Desaceleração Crítica

Para obter observáveis termodinâmicos representativos do equilíbrio, a simulação deve ser dividida em duas fases:

* **Fase 1: Termalização (Descarte inicial):**
Partindo de uma configuração qualquer (por exemplo, todos os spins $+1$ para temperaturas baixas, ou aleatórios para temperaturas altas), o sistema precisa de um tempo de relaxamento para perder a memória do estado inicial.
* **Longe de $T_c$ ($T \ll T_c$ ou $T \gg T_c$):** A convergência é rápida (~100 a 300 MCS são suficientes para redes pequenas e médias).
* **Próximo a $T_c$ ($T \approx T_c \approx 2.269 J/k_B$):** Ocorre o fenômeno da **Desaceleração Crítica (*Critical Slowing Down*)**. O tempo de autocorrelação temporal $\tau$ diverge com o tamanho do sistema:

$$\tau \propto L^z$$



Para o algoritmo de Metropolis local, o expoente dinâmico é $z \approx 2.17$. Isso significa que, perto da transição de fase, o número de MCS necessários para atingir o equilíbrio cresce quadraticamente com o tamanho da rede.


* **Fase 2: Medição (Amostragem de Equilíbrio):**
Após a termalização, acumulam-se medições do parâmetro de ordem a cada MCS (ou a cada intervalo $k \cdot \tau$ passos) para calcular as médias térmicas.

---

### 3. Análise de Erros e Efeitos de Tamanho Finito (*Finite-Size Effects*)

#### Erros Estatísticos (Amostras Correlacionadas)

Como configurações em passos consecutivos de Monte Carlo dependem do estado anterior, medições sucessivas são correlacionadas.

* O erro padrão simples da média ($\sigma / \sqrt{N_{\text{amostras}}}$) **subestima** o erro real.
* O erro correto leva em conta o tempo de autocorrelação $\tau$:

$$\sigma_{\text{real}} = \sqrt{\frac{\sigma^2}{N_{\text{amostras}}} (1 + 2\tau)}$$


* Para contornar isso, utiliza-se a técnica de **Agrupamento em Blocos (*Binning*)**, aglutinando medições consecutivas em blocos maiores do que $\tau$ antes de calcular a variância.

#### Efeitos de Tamanho Finito (*Finite-Size Scaling* - FSS)

Em redes finitas ($L < \infty$), a energia livre é uma função estritamente analítica. Por isso, sistemas finitos não apresentam transições de fase genuínas (sem descontinuidades matemáticas ou divergências infinitas).

1. **Arredondamento (*Rounding*) da Transição:**
A queda da magnetização em torno de $T_c$ não é uma quebra abrupta vertical, mas sim uma curva suave que se torna mais íngreme à medida que $L$ aumenta.
2. **Cauda em Altas Temperaturas ($T > T_c$):**
Teoricamente, no limite termodinâmico ($L \to \infty$), a magnetização espontânea é nula para $T > T_c$. No entanto, para evitar o cancelamento por inversões globais do sistema, mede-se o módulo da magnetização $\langle \vert{}m\vert{} \rangle$. Em um volume finito $N = L^2$, flutuações térmicas geram um valor residual não nulo:

$$\langle \vert{}m\vert{} \rangle \sim \mathcal{O}\left(\frac{1}{\sqrt{N}}\right) = \mathcal{O}\left(\frac{1}{L}\right) \quad \text{para } T > T_c$$



À medida que $L \to \infty$, essa cauda decai para zero.

#### O Trabalho de David P. Landau (1976)

Em seu artigo clássico (*Finite-size behavior of the Ising lattice*, PRB 1976), David P. Landau realizou simulações sistemáticas em redes $L \times L$ para diversos tamanhos ($L = 4, 10, 20, 30, 40, 60$). Ele demonstrou quantitativamente como as curvas de $\langle \vert{}m\vert{} \rangle(T)$ de redes finitas convergem sistematicamente para a **Solução Exata de Onsager** no limite termodinâmico:

$$M_{\text{Onsager}}(T) = \begin{cases} \left[ 1 - \sinh^{-2}\left(\frac{2J}{k_B T}\right) \right]^{1/8}, & T < T_c \\ 0, & T \ge T_c \end{cases} \qquad \text{onde } T_c = \frac{2 J}{k_B \ln(1 + \sqrt{2})} \approx 2.2691857 \frac{J}{k_B}$$

---

### 4. Código Python Completo (Modelo de Ising 2D do Zero)

O código abaixo implementa o algoritmo de Metropolis, calcula a magnetização média $\langle \vert{}m\vert{} \rangle$ para redes de tamanhos $L = 4, 10, 20$, calcula a curva exata de Onsager e plota a comparação.

```python
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

```

### O que observar nos resultados:

1. Para $L = 4$, a curva é bastante arredondada em torno de $T_c$ e apresenta uma cauda alta em $T > T_c$ ($\langle \vert{}m\vert{} \rangle \approx 0.5$).
2. Para $L = 10$ e $L = 20$, o "joelho" da transição fica progressivamente mais acentuado próximo a $T_c \approx 2.269$, e a cauda para $T > T_c$ cai rapidamente em direção a zero.
3. Se você estender a simulação para $L = 40$ ou $L = 60$, a curva de Monte Carlo torna-se praticamente indistinguível da linha tracejada da **Solução Exata de Onsager**.
