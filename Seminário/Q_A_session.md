Separei as perguntas por tema, das mais prováveis para as mais difíceis. As respostas estão escritas para serem faladas, com um gancho para o slide de apoio quando há conta por trás.

---

## Sobre o modelo e as hipóteses

**1. Por que usar o modelo esférico médio e não o esférico original?**

Porque no médio o vínculo é imposto por um multiplicador, o mi, e as integrais em cada modo ficam independentes e gaussianas. No modelo estrito, a delta acopla todos os modos, e é preciso fazer uma integral de ponto de sela no fim. Para as grandezas termodinâmicas usuais, como magnetização, suscetibilidade e entropia, os dois dão o mesmo resultado no limite termodinâmico, porque a soma dos quadrados no modelo médio flutua com desvio relativo de ordem um sobre raiz de N. A equivalência está no apoio B oito.

**2. O mi é mesmo um potencial químico? Não há partículas aqui.**

É uma analogia. No grande canônico, mi controla o número médio de partículas. Aqui, controla o valor médio da soma dos quadrados dos spins. Formalmente, é um multiplicador de Lagrange conjugado a essa soma. A analogia fica mais forte quando vemos que o mecanismo da transição é idêntico ao da condensação de Bose-Einstein: mi gruda num valor limite e o excesso vai para um único modo.

**3. Curie-Weiss não é uma aproximação de campo médio? Então o resultado não é exato.**

Aqui não é aproximação, é a definição do modelo. Todos interagem com todos com intensidade J sobre N. Para esse hamiltoniano, a solução é exata, para qualquer N. O que acontece é que um modelo de alcance infinito tem, exatamente, os expoentes de campo médio. Se quiséssemos curto alcance, a solução continua exata, mas os expoentes mudam.

**4. Os S r são spins? Eles obedecem à álgebra de momento angular?**

Não. Os S r são números reais, e na versão quântica são operadores do tipo posição, com momentos conjugados p r. O nome spin é herdado do magnetismo e é metafórico. Por isso a quantização é a de um oscilador, e não a de um spin.

**5. Por que a quantização é feita desse jeito, adicionando g sobre dois vezes p ao quadrado?**

É a forma mínima de introduzir não comutatividade: torna cada S r uma coordenada com momento conjugado, e o parâmetro g controla a força das flutuações quânticas, como se fosse um inverso de massa. Com g igual a zero volta o modelo clássico. É a proposta de Vojta e de Nieuwenhuizen, que o artigo segue. Há outras quantizações do modelo esférico na literatura, mas essa é a mais simples que preserva a solubilidade.

## Sobre o mecanismo da transição

**6. Por que não há transição com N finito?**

Porque a função de partição é uma soma finita de termos analíticos, e a solução exata para mi em função de beta é uma função suave. A raiz que aparece, um menos beta J ao quadrado mais quatro beta J sobre N, nunca se anula com N finito. Só quando N vai a infinito o termo quatro beta J sobre N some, a raiz vira o módulo de um menos beta J, e aparece a quina. É o mesmo motivo de uma fita de largura finita não ter transição, como na lista suplementar.

**7. O que exatamente "condensa"?**

O modo coletivo, q igual a zero, proporcional à magnetização total. Na fase ordenada, mi menos J sobre dois é de ordem um sobre N, e o termo desse modo no vínculo, que seria de ordem um sobre N, fica finito: carrega a fração um menos T sobre T c do vínculo. É uma ocupação macroscópica de um único modo, como no Bose-Einstein. A conta está no B cinco.

**8. Esse grudamento é só do modelo de Curie-Weiss?**

Não. Com curto alcance, o vínculo vira uma integral na zona de Brillouin. Em dimensão maior que dois, essa integral é finita quando mi atinge J chapéu de zero sobre dois. Então, abaixo de certa temperatura, mi não consegue mais satisfazer o vínculo e gruda, exatamente como em Berlin e Kac. Em dimensão dois ou menos a integral diverge e não há transição. O que muda com curto alcance são os expoentes, que deixam de ser de campo médio entre duas e quatro dimensões.

**9. Por que o limite N infinito tem que vir antes do limite de campo nulo?**

Porque com N finito e H igual a zero a simetria S para menos S é exata, e a magnetização média é zero sempre. A magnetização espontânea só aparece se o sistema for primeiro infinito, com um campo pequeno escolhendo a direção, e depois o campo for retirado. É a quebra espontânea de simetria, a mesma razão pela qual medimos o módulo da magnetização no Monte Carlo da lista seis.

## Sobre as anomalias clássicas

**10. Por que a entropia clássica fica negativa? Isso não é absurdo?**

Para variáveis contínuas, a entropia clássica só é definida a menos de uma constante, porque depende da medida de integração. O que é físico é a derivada: o calor específico. Aqui o calor específico fica constante, meio k B, até T igual a zero, pela equipartição. Calor específico constante até o zero absoluto obriga a entropia a ir com log de T, que vai a menos infinito. Esse é o problema real: o calor específico não vai a zero, violando a terceira lei.

**11. O modelo de curto alcance também tem esse problema?**

Sim. Abaixo de T c, cada modo é uma gaussiana clássica e contribui com meio k B. A diferença é só que, com curto alcance, o calor específico não tem salto em T c, decai suavemente. Por isso o artigo diz que qualquer modelo de spins contínuos clássico tem essa anomalia.

## Sobre a versão quântica

**12. Por que só o modo q igual a zero precisa de Bogoliubov?**

Porque a interação de Curie-Weiss depende só da soma de todos os spins, ou seja, só do modo q igual a zero. Os outros modos não sabem que existe interação: só sentem mi, e já ficam diagonais após a transformada de Fourier. Na verdade nem é preciso Bogoliubov: escrevendo a coordenada e o momento coletivos, o modo zero é um oscilador deslocado com mola dois vezes mi menos J sobre dois. O B doze mostra isso.

**13. O que acontece para mi menor que J sobre dois no caso quântico?**

A frequência ômega zero fica imaginária, ou seja, a constante de mola do modo coletivo é negativa. É um oscilador invertido, sem estado fundamental, e a função de partição diverge. É exatamente a mesma catástrofe do caso clássico, com o mesmo valor crítico. Por isso o modo zero é chamado de modo mole: sua frequência vai a zero quando mi se aproxima de J sobre dois.

**14. Qual é a diferença entre ômega q e as frequências de Matsubara?**

São coisas diferentes. Ômega e ômega zero são as frequências dos modos normais espaciais, que vêm da quantização canônica. As frequências de Matsubara, dois pi n sobre beta, são os harmônicos de uma trajetória periódica em tempo imaginário. Elas só aparecem no formalismo de integrais de trajetória, e o produto sobre elas reconstrói o seno hiperbólico de cada oscilador.

**15. Por que tempo imaginário e trajetórias periódicas?**

Porque exponencial de menos beta H é o operador de evolução temporal com tempo t igual a menos i beta, em unidades de h barra igual a um. A função de partição é um traço, então o estado final tem de ser igual ao inicial: as trajetórias são periódicas, S de zero igual a S de beta. A integral soma todas essas trajetórias com peso exponencial de menos a ação euclidiana. Não é um princípio de mínimo: são todas as trajetórias.

**16. De onde vem a curva crítica?**

Do vínculo esférico no limite termodinâmico. Ele vale em qualquer ponto do diagrama. Na fronteira, mi acabou de grudar em J sobre dois. Então basta colocar mi igual a J sobre dois e campo nulo no vínculo, e sai: um igual a meio raiz de g sobre J vezes cotangente hiperbólica de raiz de g J sobre dois k B T.

**17. Por que g c é igual a quatro J?**

No zero absoluto, a cotangente hiperbólica vai a um, e o vínculo na fronteira fica meio raiz de g sobre J igual a um. A interpretação: o valor médio de S ao quadrado de cada oscilador no estado fundamental é a flutuação de ponto zero, meio raiz de g sobre J quando mi é J sobre dois. Quando essa flutuação sozinha esgota o orçamento da soma dos quadrados igual a N, não sobra nada para o condensado, e a ordem desaparece. Isso acontece em g igual a quatro J.

**18. Por que a magnetização é calculada pelo lado ordenado e a suscetibilidade pelo desordenado?**

A magnetização espontânea é zero na fase desordenada, então só se mede o expoente beta pelo lado ordenado. A suscetibilidade a campo nulo é infinita em toda a fase ordenada, porque mi menos J sobre dois é de ordem um sobre N. Isso é uma peculiaridade do modelo esférico. Então o expoente gama só faz sentido pelo lado desordenado.

**19. Por que os expoentes quânticos são iguais aos clássicos? Em geral, uma transição quântica em d dimensões não se comporta como uma clássica em d mais z?**

Sim, essa é a regra geral: a dimensão temporal imaginária se soma às espaciais. Mas aqui a interação é de alcance infinito, o que já coloca o sistema acima da dimensão crítica superior. Somar uma dimensão efetiva não muda nada: continua campo médio. É por isso que tanto a rota térmica quanto a quântica dão beta igual a meio e gama igual a um.

**20. Como a quântica corrige a terceira lei?**

Cada modo vira um oscilador quântico com níveis discretos, espaçados por ômega, que na fase ordenada é raiz de g J. Quando k B T é muito menor que esse espaçamento, nenhum oscilador sobe o primeiro degrau, e só sobra uma configuração: a entropia vai a zero exponencialmente, e o calor específico tem a forma de Einstein. Quem congela a entropia é esse gap. As flutuações de ponto zero têm outro papel: são elas que reduzem a magnetização e destroem a ordem em g c.

**21. Por que a entropia quântica não volta à clássica quando g vai a zero?**

Porque o modelo quântico tem dois graus de liberdade por sítio, S e p, e o clássico só tinha S. Quando g vai a zero a temperatura fixa, a entropia quântica tende à clássica mais a entropia clássica dos momentos, meio vezes um mais log de k B T sobre dois pi g, que diverge. É o termo em log de beta g que o artigo menciona. Por isso os limites não comutam: tirar a quântica e depois esfriar dá menos infinito; esfriar e depois tirar a quântica dá zero. Está no slide 22 e no B catorze.

**22. Por que o calor específico quântico vai a k B, e não a meio k B, em altas temperaturas?**

Pelo mesmo motivo: S e p são dois graus de liberdade quadráticos por sítio, cada um contribuindo com meio k B pela equipartição.

## Sobre a extensão e o contexto

**23. O que muda com campos aleatórios?**

Cada modo de Fourier vira um oscilador deslocado pelo seu próprio campo. O espectro não muda, mas o vínculo ganha um termo de desordem, que no limite termodinâmico vale delta ao quadrado sobre J ao quadrado na fronteira. A superfície crítica fica: um igual a delta ao quadrado sobre J ao quadrado mais o termo térmico e quântico. Essa conta é minha, seguindo o método do artigo, e está no B dezenove. A afirmação de que a desordem é mais relevante que as flutuações quânticas é dos autores, em acordo com Vojta e Schreiber, e diz respeito ao comportamento crítico, que não refiz.

**24. Esse modelo descreve algum material real?**

Não diretamente. Variáveis de spin contínuas e interação de alcance infinito são idealizações. O valor do modelo é pedagógico e conceitual: mostra, com contas exatas, o mecanismo de uma transição tipo Bose-Einstein, como o limite termodinâmico cria a singularidade, como a quantização corrige a terceira lei e como funciona um ponto crítico quântico. Versões quânticas do modelo esférico são usadas na literatura como ponto de partida para sistemas frustrados, desordenados e vidros de spin, justamente por serem solúveis.

**25. As erratas que você encontrou mudam algum resultado?**

Não. São tipográficas: expoentes de N trocados, um log que não deveria estar lá, um quadrado faltando num denominador, uma equação que mostra a energia livre em vez da entropia, e uma convenção no deslocamento da transformação de Bogoliubov. Todos os resultados físicos do artigo conferem, e as passagens completas estão nos slides de apoio.

---

**Duas dicas para a sessão de perguntas:**
- Se a pergunta for sobre uma conta, responda primeiro a ideia física em uma frase e só depois ofereça abrir o slide de apoio ("está no B cinco, posso mostrar").
- Se não souber, diga que não refez aquela parte e cite a referência. As perguntas mais arriscadas são a 19, sobre a dimensão efetiva em transições quânticas, e a 23, sobre a relevância da desordem. Em ambas, vale deixar claro o que você verificou e o que é afirmação da literatura.
