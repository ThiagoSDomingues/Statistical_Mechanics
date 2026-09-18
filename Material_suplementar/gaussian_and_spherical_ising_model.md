Para contornar a dificuldade de resolver o modelo de Ising discreto ($s_i = \pm 1$) em dimensões $d \ge 3$, Berlin e Kac (1952) introduziram o **Modelo Gaussiano** e o **Modelo Esférico**, que relaxam a restrição discreta dos spins mantendo a solvabilidade exata em qualquer dimensão.

---

### 1. O Modelo Gaussiano

Em vez de restringir $s_i \in \{-1, +1\}$, permite-se que $s_i \in (-\infty, \infty)$ sob uma distribuição gaussiana individual centralizada em zero com parâmetro $b > 0$.

#### **Hamiltoniana e Função de Partição**

A função de partição para uma rede de $N$ sites sob campo externo $H$ é:

$$Z_G = \int_{-\infty}^{\infty} \left( \prod_{i=1}^N ds_i \right) \exp \left[ -\frac{b}{2} \sum_{i} s_i^2 + \beta J \sum_{\langle i,j \rangle} s_i s_j + \beta H \sum_i s_i \right]$$

#### **Diagonalização no Espaço de Recíproco (Transformada de Fourier)**

Usando as variáveis do espaço de Fourier $s_i = \frac{1}{\sqrt{N}} \sum_k e^{i k \cdot r_i} s_k$:

$$\sum_{\langle i,j \rangle} s_i s_j = \frac{1}{2} \sum_k \gamma_k \vert{}s_k\vert{}^2 \quad \text{onde} \quad \gamma_k = 2 \sum_{\mu=1}^d \cos(k_\mu)$$

O argumento do expoente toma a forma quadrática diagonalizada:

$$\mathcal{H}_{eff} = -\frac{1}{2} \sum_k (b - \beta J \gamma_k) \vert{}s_k\vert{}^2 + \beta H \sqrt{N} s_{k=0}$$

Realizando a integração gaussiana para cada modo $k$:

$$Z_G = \left( \frac{2\pi}{b} \right)^{N/2} \left[ \det \left( \mathbb{I} - \frac{\beta J}{b} \mathbf{A} \right) \right]^{-1/2} \exp \left( \frac{N \beta^2 H^2}{2(b - 2d\beta J)} \right)$$

onde $\mathbf{A}$ é a matriz de adjacência da rede.

#### **A Patologia do Modelo Gaussiano**

Para que a integral gaussiana convirja, a matriz precisa ser definida positiva. Isso exige que $b - \beta J \gamma_k > 0$ para todo $k$. Como o valor máximo de $\gamma_k$ é $2d$ (em $k=0$):

$$k_B T > \frac{2d J}{b}$$

**Problema:** Em baixas temperaturas ($T \to 0$, ou $\beta \to \infty$), a condição falha. As flutuações dos spins crescem sem limite ($\vert{}s_i\vert{} \to \infty$), gerando um modelo não-físico e instável abaixo de uma temperatura crítica fictícia.

---

### 2. O Modelo Esférico

Para corrigir a instabilidade do modelo gaussiano sem perder a integrabilidade, Berlin e Kac substituíram o peso gaussiano local por uma **restrição global** (a "esfera" de raio $\sqrt{N}$):

$$\sum_{i=1}^N s_i^2 = N$$

#### **Formulação via Integrais de Contorno**

A restrição é incorporada à função de partição através da representação integral da função Delta de Dirac:

$$Z_S = \int \left( \prod_i ds_i \right) \delta\left( N - \sum_i s_i^2 \right) \exp \left( \beta J \sum_{\langle i,j \rangle} s_i s_j + \beta H \sum_i s_i \right)$$

Usando a identidade $\delta(x) = \frac{1}{2\pi i} \int_{z_0 - i\infty}^{z_0 + i\infty} e^{z x} dz$:

$$Z_S = \frac{1}{2\pi i} \int_{z_0 - i\infty}^{z_0 + i\infty} dz \, e^{z N} \int \left( \prod_i ds_i \right) \exp \left[ -z \sum_i s_i^2 + \beta J \sum_{\langle i,j \rangle} s_i s_j + \beta H \sum_i s_i \right]$$

Integrando sobre as variáveis $s_i$ (que agora é uma Gaussiana controlada pelo parâmetro $z$):

$$Z_S = \frac{1}{2\pi i} \int_{z_0 - i\infty}^{z_0 + i\infty} dz \, \exp \left[ N \cdot g(z) \right]$$

$$g(z) = z - \frac{1}{2N} \sum_k \ln (2z - \beta J \gamma_k) + \frac{\beta^2 H^2}{2(2z - 2d \beta J)}$$

#### **Método do Ponto de Sela (Limite Termodinâmico $N \to \infty$)**

No limite $N \to \infty$, a integral sobre $z$ é dominada pelo ponto de sela $z_s$, dado por $\frac{dg}{dz} = 0$:

$$1 = \frac{1}{N} \sum_k \frac{1}{2z_s - \beta J \gamma_k} + \frac{\beta^2 H^2}{(2z_s - 2d \beta J)^2}$$

Esta é a **Equação da Esfera**. O valor de $z_s(T, H)$ atua como um multiplicador de Lagrange ajustado termodinamicamente para manter o comprimento médio dos spins unitário.

---

### Key Takeaways para a Aula

* **Transição de Fase ($H=0$):** No limite $N \to \infty$, a soma vira uma integral no espaço de momentos:

$$1 = \int \frac{d^d k}{(2\pi)^d} \frac{1}{2z_s - \beta J \gamma_k}$$


* Para $d \le 2$, a integral diverge quando $2z_s \to 2d\beta J$, impedindo transição de fase a $T > 0$ (consistente com o Teorema de Mermin-Wagner).
* Para $d > 2$, a integral converge em $2z_s = 2d\beta J$, definindo uma temperatura crítica finita $T_c$.


* **Relação com o Modelo $O(n)$:** O modelo esférico é formalmente idêntico ao limite do modelo vetorial de spins $O(n)$ quando o número de componentes de spin tende ao infinito ($n \to \infty$).
