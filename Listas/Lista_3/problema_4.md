# Teoria de Landau-de Gennes para Cristais Líquidos Nemáticos

## Exposição conceitual e matemática detalhada

---

## 1. O eixo nemático e a transição nemático-isotrópica

Cristais líquidos nemáticos são formados por moléculas alongadas (tipicamente cilíndricas) que, na fase nemática, apresentam **ordem orientacional** de longo alcance: os eixos maiores das moléculas tendem a se alinhar ao longo de uma direção privilegiada, chamada **diretor nemático** \(\hat{n}\). Diferentemente dos cristais sólidos, não há ordem posicional (translacional) — as moléculas podem se mover livremente como em um líquido, mas mantêm uma orientação média preferencial.

A transição nemático-isotrópica ocorre quando, ao aumentar a temperatura, a agitação térmica destrói essa ordem orientacional, levando o sistema a uma fase **isotrópica** (desordenada), na qual as moléculas apontam em direções aleatórias.

**Ponto crucial**: a fase nemática não possui ordem polar (não distingue \(\hat{n}\) de \(-\hat{n}\)), pois as moléculas são apolares em média. Isso significa que o parâmetro de ordem não pode ser um vetor simples (que mudaria de sinal sob inversão), mas deve ser um **tensor simétrico de traço nulo**.

---

## 2. O parâmetro de ordem \(\mathbf{Q}\)

### 2.1. Por que um tensor?

Em um fluido isotrópico, a distribuição de orientações moleculares \(f(\hat{u})\) é uniforme na esfera unitária. Na fase nemática, há uma direção preferencial \(\hat{n}\), e a distribuição torna-se anisotrópica. O parâmetro de ordem natural é o segundo momento da distribuição:

\[
Q_{ij} = \left\langle u_i u_j - \frac{1}{3}\delta_{ij} \right\rangle
\]

onde \(\hat{u}\) é o vetor unitário ao longo do eixo da molécula. O termo \(-\frac{1}{3}\delta_{ij}\) garante que \(\mathbf{Q}\) seja **de traço nulo**:

\[
\operatorname{Tr}(\mathbf{Q}) = \langle u_x^2 + u_y^2 + u_z^2 \rangle - 1 = \langle 1 \rangle - 1 = 0.
\]

Além disso, \(\mathbf{Q}\) é **simétrico** por construção: \(Q_{ij} = Q_{ji}\).

**Invariância sob inversão**: como \(\hat{u} \to -\hat{u}\) representa a mesma orientação molecular, \(\mathbf{Q}\) é invariante sob essa troca (produto de dois vetores). Isso reflete a simetria apolar da fase nemática.

### 2.2. Diagonalização e fases distintas

Como \(\mathbf{Q}\) é real, simétrico e de traço nulo, ele é **sempre diagonalizável** por uma transformação ortogonal. Em seus **eixos principais** (referencial próprio), podemos escrever:

\[
\mathbf{Q} = \begin{pmatrix}
-\frac{1}{2}(S + \eta) & 0 & 0 \\
0 & -\frac{1}{2}(S - \eta) & 0 \\
0 & 0 & S
\end{pmatrix}
\]

com a condição de traço nulo automaticamente satisfeita:
\[
\operatorname{Tr}(\mathbf{Q}) = -\frac{S+\eta}{2} - \frac{S-\eta}{2} + S = 0.
\]

**Atenção**: esta forma diagonal é válida apenas no **referencial próprio do tensor**, que geralmente **não coincide com o referencial do laboratório**. No laboratório, \(\mathbf{Q}\) é uma matriz cheia (mas ainda simétrica e de traço nulo). A escolha dos eixos principais é sempre possível e simplifica enormemente a análise.

### 2.3. As três fases

| Fase | \(S\) | \(\eta\) | Descrição |
|---|---|---|---|
| **Isotrópica** | 0 | 0 | \(\mathbf{Q} = 0\); completa desordem orientacional |
| **Nemática uniaxial** | \(\neq 0\) | 0 | Simetria axial em torno de \(\hat{n}\); dois autovalores iguais (\(-S/2, -S/2, S\)) |
| **Nemática biaxial** | \(\neq 0\) | \(\neq 0\) | Três autovalores distintos; duas direções privilegiadas |

Na fase uniaxial, o sistema possui simetria de rotação em torno do diretor \(\hat{n}\). Na fase biaxial, essa simetria é quebrada, e o sistema distingue duas direções ortogonais.

### 2.4. É possível uma fase triaxial?

**Não**, no sentido de que o tensor \(\mathbf{Q}\) tem apenas **dois** parâmetros independentes (\(S\) e \(\eta\)) em 3 dimensões. Não há um terceiro parâmetro de ordem independente, pois:

- \(\mathbf{Q}\) é simétrico (\(6\) componentes independentes);
- \(\operatorname{Tr}(\mathbf{Q}) = 0\) (\(-1\) componente);
- A orientação dos eixos principais é arbitrária (rotação global, que não é um parâmetro de ordem, mas sim uma quebra de simetria contínua).

Restam, portanto, \(6 - 1 - 3 = 2\) parâmetros de ordem independentes: \(S\) e \(\eta\). Uma "fase triaxial" com três parâmetros independentes só seria possível se o tensor não fosse de traço nulo (o que não é o caso) ou em dimensões maiores.

---

## 3. (a) Invariantes do tensor \(\mathbf{Q}\)

### 3.1. Quantos invariantes independentes tem um tensor simétrico em \(N\) dimensões?

Para uma matriz simétrica \(N \times N\), os invariantes fundamentais são os coeficientes do **polinômio característico**:

\[
\det(\lambda \mathbf{I} - \mathbf{Q}) = \lambda^N - c_1 \lambda^{N-1} + c_2 \lambda^{N-2} - \cdots + (-1)^N c_N
\]

onde
\[
c_1 = \operatorname{Tr}(\mathbf{Q}), \quad
c_2 = \frac{1}{2}\left[(\operatorname{Tr}\mathbf{Q})^2 - \operatorname{Tr}(\mathbf{Q}^2)\right], \quad \dots
\]

Ou seja, há **\(N\) invariantes independentes**, que podem ser escritos em termos das potências do traço:
\[
\operatorname{Tr}(\mathbf{Q}), \operatorname{Tr}(\mathbf{Q}^2), \dots, \operatorname{Tr}(\mathbf{Q}^N).
\]

### 3.2. Teorema de Cayley-Hamilton

O **teorema de Cayley-Hamilton** afirma que toda matriz satisfaz sua própria equação característica:

\[
\mathbf{Q}^N - c_1 \mathbf{Q}^{N-1} + c_2 \mathbf{Q}^{N-2} - \cdots + (-1)^N c_N \mathbf{I} = 0.
\]

Tomando o traço desta equação, obtemos uma relação entre \(\operatorname{Tr}(\mathbf{Q}^N)\) e as potências inferiores:
\[
\operatorname{Tr}(\mathbf{Q}^N) - c_1 \operatorname{Tr}(\mathbf{Q}^{N-1}) + \cdots + (-1)^N c_N N = 0.
\]

Isso mostra que \(\operatorname{Tr}(\mathbf{Q}^N)\) **não é independente** — ele pode ser expresso em termos dos invariantes inferiores. Logo, para uma matriz \(N \times N\), há no máximo \(N\) invariantes independentes, mas como \(c_1 = \operatorname{Tr}(\mathbf{Q}) = 0\) no nosso caso, restam \(N-1\) invariantes.

**Generalização para qualquer \(N\)**: sim, o teorema de Cayley-Hamilton é válido para matrizes de qualquer dimensão \(N\), e o argumento acima se aplica igualmente.

### 3.3. Por que apenas \(I_2\) e \(I_3\)?

No nosso caso, \(N = 3\) e \(\operatorname{Tr}(\mathbf{Q}) = 0\). Portanto:

- Os invariantes independentes são \(\operatorname{Tr}(\mathbf{Q}^2)\) e \(\operatorname{Tr}(\mathbf{Q}^3)\).
- \(\operatorname{Tr}(\mathbf{Q}^4)\), \(\operatorname{Tr}(\mathbf{Q}^5)\), etc., são **dependentes** de \(I_2\) e \(I_3\) pelo teorema de Cayley-Hamilton.

**Verificação explícita**: Para uma matriz \(3 \times 3\) de traço nulo, a equação característica é
\[
\lambda^3 - \frac{1}{2} I_2 \lambda - \frac{1}{3} I_3 = 0,
\]
onde \(I_2 = \operatorname{Tr}(\mathbf{Q}^2)\) e \(I_3 = \operatorname{Tr}(\mathbf{Q}^3)\). Multiplicando por \(\mathbf{Q}\) e tomando o traço:
\[
\operatorname{Tr}(\mathbf{Q}^4) = \frac{1}{2} I_2^2,
\]
o que confirma que \(\operatorname{Tr}(\mathbf{Q}^4)\) não é independente.

### 3.4. Cálculo explícito de \(I_2\) e \(I_3\)

Com \(\mathbf{Q}\) diagonal nos eixos principais:
\[
\mathbf{Q} = \operatorname{diag}\left(-\frac{S+\eta}{2}, -\frac{S-\eta}{2}, S\right),
\]
temos:

**Para \(I_2\):**
\[
I_2 = \operatorname{Tr}(\mathbf{Q}^2) = \left(\frac{S+\eta}{2}\right)^2 + \left(\frac{S-\eta}{2}\right)^2 + S^2.
\]
Expandindo:
\[
\left(\frac{S+\eta}{2}\right)^2 = \frac{S^2}{4} + \frac{S\eta}{2} + \frac{\eta^2}{4}, \quad
\left(\frac{S-\eta}{2}\right)^2 = \frac{S^2}{4} - \frac{S\eta}{2} + \frac{\eta^2}{4}.
\]
Somando:
\[
I_2 = \frac{S^2}{2} + \frac{\eta^2}{2} + S^2 = \frac{3}{2}S^2 + \frac{1}{2}\eta^2.
\]

**Para \(I_3\):**
\[
I_3 = \operatorname{Tr}(\mathbf{Q}^3) = \left(-\frac{S+\eta}{2}\right)^3 + \left(-\frac{S-\eta}{2}\right)^3 + S^3.
\]
Usando \((a+b)^3 + (a-b)^3 = 2a^3 + 6ab^2\) com \(a = -S/2\) e \(b = \eta/2\):
\[
\left(-\frac{S+\eta}{2}\right)^3 + \left(-\frac{S-\eta}{2}\right)^3 = 2\left(-\frac{S}{2}\right)^3 + 6\left(-\frac{S}{2}\right)\left(\frac{\eta}{2}\right)^2 = -\frac{S^3}{4} - \frac{3S\eta^2}{4}.
\]
Portanto:
\[
I_3 = S^3 - \frac{S^3}{4} - \frac{3S\eta^2}{4} = \frac{3}{4}S^3 - \frac{3}{4}S\eta^2.
\]

### 3.5. Significado físico de \(I_2\) e \(I_3\)

- \(I_2 = \operatorname{Tr}(\mathbf{Q}^2) \geq 0\) mede a **magnitude global da ordem** (quanto maior \(I_2\), mais ordenado o sistema). É análogo a \(|\mathbf{M}|^2\) no modelo de Ising.
- \(I_3 = \operatorname{Tr}(\mathbf{Q}^3)\) mede a **biaxialidade** e a **assimetria** da distribuição de orientações. Em particular, \(I_3 \neq 0\) é necessário para distinguir a fase uniaxial da biaxial. Na fase uniaxial (\(\eta = 0\)), \(I_3 = \frac{3}{4}S^3 \propto S^3\), enquanto na fase biaxial há uma contribuição extra \(-\frac{3}{4}S\eta^2\).

---

## 4. (b) Energia livre de Landau-de Gennes

### 4.1. Expansão em invariantes

A energia livre é uma função escalar, invariante sob rotações. Portanto, só pode depender de \(I_2\) e \(I_3\) (e de produtos entre eles). A expansão de Landau-de Gennes é:

\[
F = F_0 + \frac{1}{2}A(T) I_2 + \frac{1}{3}B(T) I_3 + \frac{1}{4}C(T) I_2^2 + \cdots
\]

Os fatores \(1/2\), \(1/3\), \(1/4\) são convenções que simplificam os coeficientes posteriores.

### 4.2. Caso uniaxial (\(\eta = 0\))

Com \(\eta = 0\):
\[
I_2 = \frac{3}{2}S^2, \quad I_3 = \frac{3}{4}S^3, \quad I_2^2 = \frac{9}{4}S^4.
\]

Substituindo:
\[
F = F_0 + \frac{1}{2}A(T)\frac{3}{2}S^2 + \frac{1}{3}B(T)\frac{3}{4}S^3 + \frac{1}{4}C(T)\frac{9}{4}S^4
\]
\[
\boxed{F = F_0 + \frac{3}{4}A(T) S^2 + \frac{1}{4}B(T) S^3 + \frac{9}{16}C(T) S^4 + \cdots}
\]

### 4.3. Coeficientes fenomenológicos

Assumimos:
- \(A(T) = a(T - T_*)\), com \(a > 0\) (a temperatura \(T_*\) é a temperatura "nua" onde o coeficiente quadrático se anula);
- \(B(T) = B = \text{constante}\) (pode ser positivo ou negativo);
- \(C(T) = C > 0\) (garante estabilidade para \(S\) grande).

Escrevemos:
\[
F(S) - F_0 = A_2 S^2 + A_3 S^3 + A_4 S^4,
\]
com
\[
A_2 = \frac{3}{4}a(T - T_*), \quad A_3 = \frac{1}{4}B, \quad A_4 = \frac{9}{16}C.
\]

### 4.4. Análise da transição de primeira ordem

**Condição de mínimo**: \(\partial F/\partial S = 0\):
\[
2A_2 S + 3A_3 S^2 + 4A_4 S^3 = 0.
\]
Dividindo por \(S \neq 0\):
\[
2A_2 + 3A_3 S + 4A_4 S^2 = 0. \tag{1}
\]

**Coexistência de fases**: \(F(S_0) = F(0)\):
\[
A_2 S_0^2 + A_3 S_0^3 + A_4 S_0^4 = 0.
\]
Dividindo por \(S_0^2\):
\[
A_2 + A_3 S_0 + A_4 S_0^2 = 0. \tag{2}
\]

**Resolvendo o sistema** (1)-(2):
Da equação (2): \(A_2 = -A_3 S_0 - A_4 S_0^2\). Substituindo em (1):
\[
2(-A_3 S_0 - A_4 S_0^2) + 3A_3 S_0 + 4A_4 S_0^2 = 0
\]
\[
A_3 S_0 + 2A_4 S_0^2 = 0 \quad \Longrightarrow \quad S_0 = -\frac{A_3}{2A_4}.
\]
Substituindo \(A_3 = B/4\) e \(A_4 = 9C/16\):
\[
\boxed{S_0 = -\frac{B/4}{2 \cdot 9C/16} = -\frac{2B}{9C}.}
\]

**Temperatura de transição** \(T_{NI}\): da equação (2),
\[
A_2 = -A_3 S_0 - A_4 S_0^2.
\]
Substituindo \(S_0 = -2B/(9C)\):
\[
A_3 S_0 = -\frac{B^2}{18C}, \quad A_4 S_0^2 = \frac{B^2}{36C},
\]
\[
A_2 = \frac{B^2}{18C} - \frac{B^2}{36C} = \frac{B^2}{36C}.
\]
Mas \(A_2 = \frac{3}{4}a(T_{NI} - T_*)\), logo:
\[
\frac{3}{4}a(T_{NI} - T_*) = \frac{B^2}{36C} \quad \Longrightarrow \quad
\boxed{T_{NI} = T_* + \frac{B^2}{27aC}.}
\]

### 4.5. Interpretação física

- **Para \(B > 0\)**: o termo cúbico é positivo e a transição é de **segunda ordem** em \(T = T_*\). O parâmetro de ordem cresce continuamente a partir de zero.
- **Para \(B < 0\)**: o termo cúbico é negativo, gerando um mínimo local em \(S \neq 0\) **antes** de \(T_*\). A transição ocorre em \(T_{NI} > T_*\), com um **salto descontínuo** de \(S = 0\) para \(S = S_0\). Isso é a assinatura da **transição de primeira ordem**, observada experimentalmente em praticamente todos os cristais líquidos nemáticos.
- **Temperatura spinodal**: o ramo metaestável da fase nemática existe até \(T_{\text{spinodal}} = T_* + B^2/(24aC) > T_{NI}\), onde o mínimo local desaparece.

### 4.6. Resumo dos resultados

| Grandeza | Expressão |
|---|---|
| Parâmetro de ordem na coexistência | \(S_0 = -2B/(9C)\) |
| Temperatura de transição | \(T_{NI} = T_* + B^2/(27aC)\) |
| Temperatura spinodal | \(T_{\text{sp}} = T_* + B^2/(24aC)\) |
| Ordem da transição | 1ª ordem (se \(B \neq 0\)) |

A presença do termo cúbico \(I_3\) é, portanto, a **razão fundamental** pela qual a transição nemático-isotrópica é de primeira ordem. Se \(B = 0\) (por exemplo, em sistemas com simetria adicional), a transição seria de segunda ordem.

---

## 5. Conclusão

A teoria de Landau-de Gennes fornece uma descrição fenomenológica elegante e quantitativa da transição nemático-isotrópica. Os pontos-chave são:

1. O parâmetro de ordem é um **tensor simétrico de traço nulo**, com dois invariantes independentes \(I_2\) e \(I_3\).
2. A expansão da energia livre em \(I_2\) e \(I_3\) contém um **termo cúbico** (\(I_3\)) que é permitido pela simetria apolar do sistema.
3. Esse termo cúbico induz uma **transição de primeira ordem**, com coexistência entre as fases isotrópica e nemática uniaxial em \(T_{NI} > T_*\).
4. Os resultados quantitativos (\(S_0\), \(T_{NI}\), \(T_{\text{sp}}\)) estão em excelente acordo com as observações experimentais em cristais líquidos nemáticos.
