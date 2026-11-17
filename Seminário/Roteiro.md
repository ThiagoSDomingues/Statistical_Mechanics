Segue o roteiro completo em texto corrido, pronto para ler em voz alta. Os títulos marcam cada slide; o resto é a fala.

---

**Slide 1 de 27 — Capa**

Boa tarde a todos. Hoje eu vou apresentar o artigo Modelo esférico quântico elementar, de Paula Bienzobaz e Sílvio Salinas, publicado em 2013 na Revista Brasileira de Ensino de Física. É um artigo pedagógico, mas ele junta, num modelo só, várias ideias que trabalhamos no curso: o mecanismo de uma transição de fase, o papel do limite termodinâmico, a mudança de ensemble, a versão de Curie-Weiss e, no fim, o que acontece quando a mecânica quântica entra no problema.

**Slide 2 de 27 — Roteiro**

O roteiro é o seguinte. Começo pelo contexto histórico, do modelo gaussiano de Kac até o modelo esférico. Depois resolvo o modelo clássico na versão de Curie-Weiss e mostro o mecanismo da transição e as anomalias que ele tem a baixas temperaturas. Em seguida falo rapidamente do que é uma transição de fase quântica, construo o modelo quântico e discuto o diagrama de fases, os expoentes críticos e a correção das anomalias. Termino com as conclusões e uma extensão para campos aleatórios.

No rodapé eu coloquei uma legenda: ao longo dos slides, em verde e entre parênteses, aparecem referências às nossas listas. L três P dois, por exemplo, quer dizer lista três, problema dois. Muitas das contas do artigo são contas que nós já fizemos durante a disciplina. Em azul aparecem os números das equações do artigo. E todas as passagens algébricas estão nos slides de apoio, depois do agradecimento, caso alguém queira ver algum detalhe.

**Slide 3 de 27 — A pergunta deste seminário**

Eu gosto de começar pela pergunta. Qual é o modelo mais simples, resolvido exatamente, que tenha três coisas ao mesmo tempo? Primeiro, uma transição térmica cujo mecanismo a gente consiga ver acontecer. Segundo, um defeito clássico a baixas temperaturas que a mecânica quântica corrige. Terceiro, uma transição de fase quântica, no zero absoluto.

A resposta do artigo é: o modelo esférico médio, com interação de campo médio, mais uma energia cinética, g sobre dois vezes a soma dos p ao quadrado. E tudo se reduz a duas ferramentas que todos aqui conhecem: integrais gaussianas e osciladores harmônicos.

Se vocês guardarem três mensagens, que sejam estas. Um: o potencial químico gruda em J sobre dois, e esse é o mecanismo de Bose-Einstein. Dois: um g positivo restaura a terceira lei da termodinâmica. Três: existe um ponto crítico quântico em g c igual a quatro J, com os mesmos expoentes de campo médio do caso clássico.

**Slide 4 de 27 — Modelos exatamente solúveis**

Por que modelos exatos? Porque eles funcionam como um laboratório: testamos hipóteses sem aproximações e vemos o mecanismo da transição. O exemplo clássico é o modelo de Ising. Onsager resolveu a rede quadrada em 1944, como vimos na lista suplementar e na lista quatro, mas a solução é muito difícil, e em três dimensões não há solução exata.

Kac propôs então trocar os spins discretos, mais ou menos um, por variáveis contínuas, que vão de menos infinito a mais infinito, com um peso gaussiano, exponencial de menos b sobre dois vezes S ao quadrado em cada sítio. O problema fica gaussiano e se resolve com Fourier. Mas há a catástrofe de baixas temperaturas: abaixo de uma temperatura crítica, a integral diverge, mesmo com o peso gaussiano.

Berlin e Kac, em 1952, trocam o peso gaussiano por um vínculo rígido: uma delta de N menos a soma dos quadrados dos spins. É o modelo esférico. E Lewis e Wannier propõem logo depois o modelo esférico médio, em que o vínculo vale só em média, com um multiplicador mi, o potencial químico. É essa versão média que vamos usar.

**Slide 5 de 27 — Três maneiras de limitar os spins**

Este desenho ajuda a fixar as ideias, com só dois spins, S um e S dois. À esquerda, o Ising: as configurações são os quatro cantos de um quadrado. No meio, o modelo gaussiano: uma nuvem que cobre o plano todo, com densidade maior perto da origem e decrescendo para fora. À direita, o modelo esférico: um círculo de raio raiz de dois, que passa exatamente pelos quatro estados de Ising, os pontos vermelhos.

Em N dimensões, é uma hiperesfera que circunscreve o hipercubo de Ising. Ela contém todos os estados de Ising, permite spins contínuos e nunca diverge, porque a superfície é compacta. Isso resolve a catástrofe de baixas temperaturas.

**Slide 6 de 27 — Esférico ou esférico médio**

Qual é a diferença entre os dois modelos esféricos? No modelo de Berlin e Kac, a soma dos quadrados é igual a N exatamente. É o ensemble canônico. No modelo médio, de Lewis e Wannier, a soma dos quadrados flutua, e o mi é escolhido para que a média seja N. É análogo ao grande canônico, com mi conjugado à soma dos quadrados em vez do número de partículas, como fizemos com o gás de rede na lista três, problema três.

A figura mostra a distribuição da soma dos quadrados dividida por N no modelo médio, acima de T c, para N igual a dez, cem e mil, em azul. A linha vermelha vertical em um é o modelo esférico estrito. A largura relativa é da ordem de raiz de dois sobre N: é a mesma lei de um sobre raiz de N que vimos na urna de Ehrenfest, na lista seis. Com N grande, a distribuição colapsa na delta, e as duas descrições dão a mesma termodinâmica para magnetização, suscetibilidade e entropia.

**Slide 7 de 27 — Uma família de modelos**

Esta tabela resume o que muda em cada passo. Em todos, a energia é menos meio vezes a soma dupla de J r r linha S r S r linha, menos H vezes a soma dos spins, com spins reais. O gaussiano multiplica por um peso fixo e diverge abaixo de T c. O esférico multiplica pela delta, vínculo rígido. O esférico médio multiplica por exponencial de menos beta mi vezes a soma dos quadrados, com mi ajustado para que a média seja N.

Em cima disso o artigo faz duas modificações. A de Curie-Weiss: J r r linha vira J sobre N, todos com todos. E a quântica: acrescenta g sobre dois vezes a soma dos p ao quadrado, com S e p canonicamente conjugados. Uma observação: mi funciona como multiplicador de Lagrange. A soma dos quadrados flutua, mas com desvio relativo de ordem um sobre raiz de N.

**Slide 8 de 27 — Versão Curie-Weiss**

À esquerda, interação de primeiros vizinhos. À direita, todos interagem com todos, com a mesma intensidade J sobre N. A hamiltoniana fica menos J sobre dois N vezes o quadrado da magnetização total, menos H vezes a magnetização total.

O fator um sobre N garante a extensividade: sem ele, como o quadrado da soma tem N ao quadrado termos, a energia cresceria como N ao quadrado. É a mesma construção que usamos no Blume-Capel de Curie-Weiss, na lista três, problema dois, e no Ising com campos aleatórios da lista sete. Aqui ela não é uma aproximação: é a definição do modelo.

**Slide 9 de 27 — Função de partição exata**

A função de partição tem três termos no expoente: a interação, o campo e o termo menos beta mi vezes a soma dos quadrados, que impõe o vínculo em média.

O truque é uma rotação ortogonal das variáveis. Defino o modo coletivo, x zero, igual a um sobre raiz de N vezes a soma dos spins. Os outros N menos um modos são transversais. A soma dos quadrados não muda com a rotação, e o jacobiano é um. Os modos transversais só sentem mi, e cada um dá uma gaussiana, raiz de pi sobre beta mi. O modo coletivo sente mi menos J sobre dois e o campo, e dá uma gaussiana com termo linear. É a identidade gaussiana, a mesma da lista três.

O resultado, equação catorze, é exato para qualquer N: pi sobre beta elevado a N sobre dois, vezes um sobre mi elevado a N menos um sobre dois, vezes mi menos J sobre dois elevado a menos meio, vezes uma exponencial do campo. Tudo só faz sentido para mi maior que J sobre dois. Se mi for menor, a gaussiana do modo coletivo cresce em vez de decrescer, e a integral diverge. Então J sobre dois é o potencial químico crítico.

**Slide 10 de 27 — O grudamento de mi**

Este é o slide central da parte clássica. Derivando log Z em relação a mi e impondo o vínculo, com campo nulo, sai uma equação do segundo grau em mi, que se resolve exatamente.

A figura mostra mi sobre J em função de k B T sobre J. As curvas azuis, da mais clara para a mais escura, são N igual a dez, cem, mil e dez mil. Elas são todas suaves: com N finito, não há transição, assim como a fita de largura finita da lista suplementar não tinha transição. A curva vermelha tracejada é o limite N infinito: mi igual a k B T sobre dois acima de T c, e mi grudado em J sobre dois abaixo de T c. A quina está em k B T c igual a J.

E para onde vai o vínculo quando mi gruda? Na fase ordenada, mi menos J sobre dois é da ordem de um sobre N. Isso faz o termo do modo coletivo, que parecia desprezível, ficar finito: ele vale um menos T sobre T c. Uma fração macroscópica do vínculo vai para um único modo. É exatamente a ocupação macroscópica do estado de momento zero na condensação de Bose-Einstein.

**Slide 11 de 27 — Sucessos e anomalias do modelo clássico**

Os sucessos. A magnetização é H sobre dois vezes mi menos J sobre dois. Com o vínculo, abaixo de T c, a magnetização espontânea é raiz de um menos T sobre T c: expoente beta igual a meio. Acima de T c, a suscetibilidade é beta sobre um menos beta J, e diverge como T menos T c elevado a menos um: gama igual a um. São os expoentes de campo médio, os mesmos de van der Waals, na lista um, e da teoria de Landau, na lista dois.

A falha. A entropia por sítio na fase ordenada é meio vezes log de dois pi T sobre T c mais um. Quando T vai a zero, o log vai a menos infinito: a entropia fica negativa e diverge. A terceira lei é violada. E o calor específico é constante, igual a meio abaixo de T c, e zero acima, com um salto, como o salto de van der Waals da lista um, problema oito. Não há congelamento dos graus de liberdade.

**Slide 12 de 27 — Visualizando sucessos e anomalias**

Aqui estão as três grandezas. À esquerda, a magnetização espontânea: raiz de um menos T sobre T c, indo a zero em T c, e zero acima. No meio, o calor específico: o degrau de meio para zero em T c, que é a figura dois do artigo. À direita, a entropia: constante acima de T c e, abaixo, decresce com o log de T, cruza o zero e despenca para menos infinito, a área sombreada em vermelho.

A causa é o caráter contínuo das variáveis. Um grau de liberdade quadrático clássico sempre contribui com meio k B ao calor específico, pela equipartição. Calor específico constante até T igual a zero significa entropia com log de T.

**Slide 13 de 27 — O que é uma transição de fase quântica**

Antes de quantizar, uma palavra sobre transições quânticas. Nas transições clássicas, quem destrói a ordem são as flutuações térmicas, e o ponto crítico está em T c. Numa transição quântica, que acontece no zero absoluto, quem destrói a ordem são as flutuações quânticas, consequência do princípio de incerteza. Elas são controladas por um parâmetro não térmico, como pressão, campo ou composição. Aqui vai ser o g. O ponto em que isso acontece é o ponto crítico quântico, como o campo transverso crítico do Ising quântico, onde o gap fecha.

No esboço, T e g são os dois parâmetros de controle. O parâmetro de ordem continua sendo a magnetização. A fase ordenada fica embaixo, a desordenada fora, o ponto vermelho é o ponto crítico quântico, e o leque acima dele é a região quântica crítica: mesmo a temperatura finita, o comportamento é governado pelo ponto crítico quântico.

**Slide 14 de 27 — Formulando o modelo quântico**

A quantização é mínima. Seguindo Vojta, adiciono momentos p r canonicamente conjugados aos S r, e uma energia cinética g sobre dois vezes a soma dos p ao quadrado. O comutador de S r com p r linha é i delta. O limite clássico é g indo a zero.

Um detalhe importante: os S r continuam sendo números reais. Não são componentes de momento angular. A palavra spin aqui é só metafórica.

Para diagonalizar, olho para a hamiltoniana mais mi vezes a soma dos quadrados. Em cada sítio isso é um oscilador harmônico, e por isso uso os operadores de criação e aniquilação usuais: S r é um sobre raiz de dois vezes g sobre dois mi elevado a um quarto vezes a mais a adaga, e p r é o análogo com a menos a adaga. Com essa escolha, a parte local vira raiz de dois g mi vezes a adaga a mais meio.

**Slide 15 de 27 — Diagonalização**

Passando os operadores para Fourier, todos os modos com q diferente de zero já ficam diagonais, com frequência ômega igual a raiz de dois g mi. O único modo que não fica diagonal é o coletivo, q igual a zero. Ele contém a interação, com termos a zero ao quadrado e a zero adaga ao quadrado, e o termo linear do campo.

Para ele, o artigo usa uma transformação de Bogoliubov, b zero igual a u a zero menos v a zero adaga mais uma translação w, com u ao quadrado menos v ao quadrado igual a um. É o mesmo tipo de transformação que usamos no Ising quântico e na lista suplementar, aqui na versão bosônica. A hamiltoniana fica uma soma de osciladores independentes, mais uma constante do campo.

O gráfico mostra as duas frequências em função de mi. A curva azul é ômega, dos N menos um modos com q diferente de zero, que só sentem mi. A curva vermelha é ômega zero, o modo coletivo, igual a raiz de dois g mi vezes raiz de um menos J sobre dois mi. Ela vai a zero em mi igual a J sobre dois: é um modo mole. A faixa cinza é mi menor que J sobre dois. Ali ômega zero seria imaginária, a mola teria constante negativa, um oscilador invertido sem estado fundamental, e a função de partição diverge. É a mesma catástrofe do caso clássico, com o mesmo valor crítico.

**Slide 16 de 27 — Função de partição quântica exata**

Como são osciladores independentes, o traço no espaço de Fock é imediato. O espaço de Fock é só a base dos números de ocupação de cada modo. Cada oscilador dá a soma geométrica de exponencial de menos beta ômega vezes n mais meio, que é um sobre dois seno hiperbólico de beta ômega sobre dois. A função de partição, equação sessenta e três, é a exponencial do campo, vezes dois elevado a menos N, vezes um fator com ômega zero e N menos um fatores com ômega. Vale para qualquer N.

O vínculo, derivando em mi, tem uma leitura simples: cada termo é o valor médio de S ao quadrado de um oscilador quântico, g sobre dois ômega vezes a cotangente hiperbólica de beta ômega sobre dois. No limite termodinâmico, com campo nulo, fica: um igual a meio raiz de g sobre dois mi vezes cotangente hiperbólica de raiz de dois g mi sobre dois k B T. Quando g vai a zero, a cotangente vira um sobre x, cada termo vira a equipartição, e recuperamos mi igual a k B T sobre dois.

**Slide 17 de 27 — Integrais de trajetória**

O artigo mostra que o mesmo resultado sai por integrais de trajetória. Vou passar rápido, porque é uma verificação. A transformada de Legendre dá a lagrangiana, com termo cinético um sobre dois g vezes S ponto ao quadrado. A ideia é que exponencial de menos beta H é a evolução temporal com tempo imaginário. Como a função de partição é um traço, as trajetórias têm de voltar ao ponto inicial: S de zero igual a S de beta, como no desenho à direita, duas trajetórias periódicas.

Uma função periódica em zero, beta se expande em harmônicos, as frequências de Matsubara, ômega n igual a dois pi n sobre beta. Tudo fica gaussiano, e o produto infinito sobre as frequências de Matsubara reproduz o seno hiperbólico do oscilador. Os detalhes estão no apoio, B quinze.

**Slide 18 de 27 — Diagrama de fases quântico**

Agora o resultado principal. A fronteira é o ponto onde mi acabou de grudar em J sobre dois. Colocando mi igual a J sobre dois no vínculo, com N infinito e campo nulo, sai a curva crítica: um igual a meio raiz de g sobre J vezes cotangente hiperbólica de raiz de g J sobre dois k B T.

Dois limites. Com g indo a zero, a cotangente vira um sobre x e recuperamos k B T c igual a J, o clássico. Com T indo a zero, a cotangente vai a um, e a condição vira meio raiz de g sobre J igual a um: g c igual a quatro J, como no gap que fecha do Ising quântico.

No gráfico, o eixo horizontal é k B T sobre J e o vertical é g sobre J. A região azul é a fase ordenada, com magnetização diferente de zero e mi igual a J sobre dois. Fora dela, a desordenada, com magnetização zero e mi maior que J sobre dois. O ponto cinza no eixo horizontal é a transição clássica, em k B T igual a J. O ponto vermelho no eixo vertical é o ponto crítico quântico, em g igual a quatro J.

**Slide 19 de 27 — Lendo o diagrama**

Vale a pena gastar um minuto lendo esse diagrama. Na fase ordenada, o vínculo diz que a flutuação dos modos com q diferente de zero, meio raiz de g sobre J vezes a cotangente, tem que ser no máximo um. O que sobra até um vai para o condensado: é a magnetização ao quadrado.

No regime térmico, essa flutuação é aproximadamente k B T sobre J, e a ordem some em T c igual a J. No regime quântico, sobra só a flutuação de ponto zero, meio raiz de g sobre J, que sozinha esgota o orçamento em g igual a quatro J, sem calor nenhum.

Entre os dois, k B T c é aproximadamente J menos g sobre doze para g pequeno, e perto de g c a temperatura crítica vai a zero só logaritmicamente, como dois J sobre log de quatro g c sobre g c menos g. Por isso a curva chega a g c de forma tão achatada.

A mensagem é: calor e incerteza competem pelo mesmo orçamento, a soma dos quadrados igual a N.

**Slide 20 de 27 — Expoentes críticos quânticos**

A magnetização tem a mesma forma do caso clássico, porque o campo entra da mesma maneira na função de partição. A T igual a zero, m zero ao quadrado é um menos raiz de g sobre g c, que perto de g c fica proporcional a g c menos g. Então m zero vai como g c menos g elevado a meio: beta g igual a meio. Calculo pelo lado ordenado, porque do lado desordenado a magnetização é zero.

Para a suscetibilidade, vou pelo lado desordenado, porque na fase ordenada ela é infinita, uma peculiaridade do modelo esférico. A T igual a zero, o vínculo dá mi igual a g sobre oito, e chi é exatamente quatro sobre g menos g c: gama g igual a um.

O gráfico, em escala log-log, mostra a magnetização em função da distância ao ponto crítico pelas duas rotas: a térmica em azul, variando T, e a quântica em vermelho, variando g. As duas têm inclinação meio. A tabela resume: mesma classe de universalidade de campo médio, o que faz sentido para uma interação de alcance infinito, e se conecta com a ideia de universalidade e de escala da lista quatro.

**Slide 21 de 27 — Restauração da terceira lei**

Agora a correção da anomalia. A entropia é a de um oscilador quântico com frequência ômega, que na fase ordenada vale raiz de g J. Quando T vai a zero, ela vai a zero exponencialmente.

O gráfico compara: em vermelho, a entropia clássica, que despenca para menos infinito. Em azul, a entropia quântica para g igual a meio J, um J e dois J. Ela sai de zero em T igual a zero e não fica negativa. A intuição é a escada de níveis: quando k B T é muito menor que o espaçamento ômega, nenhum oscilador consegue subir o primeiro degrau, e só sobra uma configuração. O teorema de Nernst está restaurado.

Há uma sutileza: os limites g indo a zero e T indo a zero não comutam. Isso é o próximo slide.

**Slide 22 de 27 — O que o modelo quântico recupera quando g vai a zero**

Este gráfico, em escala log no eixo da temperatura, explica a não comutatividade. A curva azul é a entropia quântica com g igual a dois centésimos de J. Ela não cai sobre a clássica, em vermelho. Ela cai sobre a curva verde tracejada, que é a clássica mais a entropia dos momentos, meio vezes um mais log de k B T sobre dois pi g. É o termo proporcional a log de beta g que o artigo menciona. O modelo quântico tem dois graus de liberdade por sítio, S e p. O clássico só tinha S.

A linha pontilhada marca k B T igual a raiz de g J. Abaixo dela, a quantização dos níveis domina e a entropia vai a zero. Então: tirar a quântica e depois esfriar dá menos infinito. Esfriar e depois tirar a quântica dá zero.

**Slide 23 de 27 — Calor específico**

O mesmo se vê no calor específico. Em vermelho, o clássico: o degrau de meio para zero. Em azul, o quântico, para g igual a meio, um e dois J.

Na fase ordenada, ele tem a forma de Einstein: x ao quadrado sobre seno hiperbólico de x ao quadrado, com x igual a raiz de g J sobre dois k B T. Para T indo a zero, ele cai exponencialmente, porque há um gap ômega para excitar os modos. A temperaturas altas ele tenderia a um, e não a meio, de novo porque cada sítio agora tem S e p. Na temperatura crítica de cada g, ele cai bruscamente, e acima dela fica em torno de meio, que é a contribuição dos momentos.

**Slide 24 de 27 — Magnetização espontânea variando g**

Este gráfico junta tudo. Para cada g, a magnetização espontânea em função da temperatura. A curva mais escura, g indo a zero, é a raiz de um menos T sobre T c. À medida que g aumenta, duas coisas acontecem: a magnetização no zero absoluto diminui, porque parte do orçamento vai para as flutuações de ponto zero, e a temperatura crítica também diminui. Em g igual a quatro J, a fase ordenada desaparece. É a leitura vertical do diagrama de fases.

**Slide 25 de 27 — Conclusões**

Para concluir, quatro pontos. Primeiro, o valor didático: um modelo exatamente solúvel em que se estudam transições térmicas e quânticas no mesmo lugar. Segundo, o mecanismo: o grudamento de mi em J sobre dois, análogo direto da condensação de Bose-Einstein, e que só aparece no limite termodinâmico. Terceiro, as flutuações de ponto zero restauram a terceira lei sem alterar os expoentes críticos. Quarto, existe um ponto crítico quântico em g c igual a quatro J, com expoentes de campo médio, beta g igual a meio e gama g igual a um.

**Slide 26 de 27 — Extensão: campos aleatórios**

Uma extensão que os autores sugerem, e que se liga à lista sete, problema um: trocar o campo uniforme por campos aleatórios independentes, de média zero e variância delta ao quadrado. Cada modo de Fourier vira um oscilador deslocado pelo seu campo. O espectro não muda, mas o vínculo ganha um termo de desordem, delta ao quadrado sobre J ao quadrado.

A superfície crítica fica: um igual a delta ao quadrado sobre J ao quadrado mais o mesmo termo térmico e quântico de antes. Desordem, calor e incerteza dividem o mesmo orçamento. Segundo os autores, em acordo com Vojta e Schreiber, não há ponto tricrítico, e as flutuações de desordem são mais relevantes que as quânticas. Essa última afirmação é sobre o comportamento crítico, que eu não refiz aqui.

**Slide 27 de 27 — Obrigado**

Obrigado pela atenção. Nos slides de apoio estão todas as passagens algébricas, do modelo gaussiano às integrais de trajetória, e uma tabela com pequenas erratas que encontrei no texto impresso. Nenhuma delas altera os resultados físicos. Fico à disposição para perguntas.

---

## Slides de apoio

**Índice**

A partir daqui, são os slides de apoio, numerados separadamente, que eu só uso se aparecer uma pergunta. O índice mostra os blocos: B um a B três, ferramentas, modelo gaussiano e a função delta. B quatro a B dez, o modelo clássico. B onze a B quinze, a quantização e as integrais de trajetória. B dezesseis a B dezoito, a termodinâmica quântica. B dezenove, campos aleatórios. E B vinte, as erratas.

**B1 — Ferramentas**

Três ferramentas usadas o tempo todo. A integral gaussiana: integral de exponencial de menos a x ao quadrado mais b x é raiz de pi sobre a vezes exponencial de b ao quadrado sobre quatro a, para a positivo. Sai completando quadrados.

O oscilador harmônico quântico, com frequência raiz de g k: a função de partição é um sobre dois seno hiperbólico de beta ômega sobre dois, e o valor médio de S ao quadrado é g sobre dois ômega vezes a cotangente hiperbólica, que no limite clássico vira um sobre beta k, a equipartição.

E por que derivar a mi fixo. A energia livre de verdade é phi menos mi, com phi igual a menos um sobre beta N log de Z. O vínculo é exatamente a condição de que essa energia livre seja estacionária em mi. Então, para calcular entropia e magnetização, a derivada de mi em relação a T ou H não contribui.

**B2 — Rede hipercúbica, J chapéu e a catástrofe gaussiana**

Se a interação só depende da distância, a matriz J de r menos r linha é invariante por translação, e os autovetores são ondas planas. Os autovalores são J chapéu de q, a transformada de Fourier das interações. Diagonalizar é só mudar para essa base: os termos cruzados somem. Para primeiros vizinhos numa rede hipercúbica, J chapéu de q é dois J vezes a soma dos cossenos, cujo máximo é dois d J, em q igual a zero.

No modelo gaussiano, cada modo tem peso exponencial de menos meio vezes b menos beta J chapéu de q. A integral converge se b for maior que beta J chapéu para todo q, ou seja, maior que beta dois d J. Daí k B T c igual a dois d J sobre b, como na lista oito, problema um. O artigo dá d J sobre b, um fator dois que vem da definição de b.

**B3 — Representação integral da delta**

A delta de Fourier é um sobre dois pi vezes a integral de exponencial de i k x. Trocando s igual a i k, a integral passa a correr no eixo imaginário. Deslocar o contorno para parte real c não muda nada, porque exponencial de c x vezes delta de x é delta de x. A escolha de c serve para que as integrais em S convirjam, c maior que beta J chapéu de zero sobre dois, o que permite trocar a ordem das integrações. Na equação seis impressa falta o termo s N e o sinal negativo da soma dos quadrados.

**B4 — Curie-Weiss para qualquer N**

Aqui está a conta completa da equação catorze. Rotação ortogonal com x zero proporcional à soma dos spins. A soma dos quadrados é invariante e o quadrado da soma vira N x zero ao quadrado. O expoente separa no modo coletivo, com coeficiente beta vezes mi menos J sobre dois e termo linear beta H raiz de N, e nos N menos um modos transversais, com coeficiente beta mi. Cada um é uma gaussiana, e o produto dá a equação catorze. É o mesmo espírito da identidade gaussiana da lista três, problema dois.

**B5 — Vínculo, solução exata de mi e condensado**

Derivando log Z em mi sai a equação quinze, e com campo nulo, a dezesseis. Multiplicando por quatro N mi vezes mi menos J sobre dois, obtemos a quadrática, e a raiz com mi maior que J sobre dois é um sobre quatro beta vezes um mais beta J mais a raiz de um menos beta J ao quadrado mais quatro beta J sobre N.

Com N finito, é analítica. Com N infinito, a raiz vira o módulo de um menos beta J, e saem os dois ramos. Na fase ordenada, mi menos J sobre dois é aproximadamente J sobre dois N vezes beta J menos um, de ordem um sobre N, e o modo x zero carrega a fração um menos T sobre T c do vínculo.

**B6 — Fourier para interações gerais**

A transformada de Fourier, com S chapéu de menos q igual ao conjugado de S chapéu de q, porque os spins são reais. A soma dos quadrados vira a soma dos módulos ao quadrado, a interação vira J chapéu de q vezes o módulo ao quadrado, e a soma dos spins vira raiz de N vezes S chapéu de zero. Aqui o artigo tem um erro tipográfico: imprime N elevado a menos meio.

Para integrar, separa-se metade da zona de Brillouin e escreve-se S chapéu de q como x mais i y sobre raiz de dois. É a base real de senos e cossenos, ortonormal, com jacobiano um.

**B7 — Função de partição e vínculo gerais**

Cada par x, y dá pi sobre beta vezes mi menos meio J chapéu de q. Tomando o log, a soma em metade da zona vira meio da soma em todos os q. Daí o vínculo geral, equação vinte e oito. No caso de Curie-Weiss, J chapéu de q é J delta de q zero: um termo com mi menos J sobre dois e N menos um termos com mi, e recuperamos a equação quinze. Com curto alcance, a soma vira integral, e o mesmo grudamento acontece para dimensão maior que dois.

**B8 — Ensemble canônico e ponto de sela**

No ensemble canônico, a delta vira uma integral em s, e Z é a integral de exponencial de N vezes Phi de s. Para N grande, a integral é dominada pelo ponto de sela, Phi linha igual a zero. Ao longo do eixo real é um mínimo e ao longo do contorno vertical é um máximo, por isso o nome sela. É o mesmo método de ponto de sela da lista três.

A condição de sela, com s igual a beta mi, é exatamente o vínculo esférico médio. Os dois ensembles dão a mesma termodinâmica, desde que o limite N infinito seja tomado antes de H indo a zero. Com N finito e H igual a zero, a simetria garante magnetização zero, como vimos no Monte Carlo da lista seis.

**B9 — Forma de Kastner e Schnetz**

Fixando a magnetização por sítio z, entre menos um e um, os spins restantes vivem numa esfera de dimensão N menos dois com raio proporcional a raiz de um menos z ao quadrado. A área dessa esfera dá o fator um menos z ao quadrado elevado a N menos três sobre dois. O expoente fica beta N z vezes z sobre dois mais H. Normalizando pela área da esfera inteira, aparecem as funções gama, e sai a equação trinta e quatro.

Para N grande, o máximo em z dá z ao quadrado igual a um menos T sobre T c, a mesma magnetização. Para N finito, expandindo em série, cada termo vira uma função hipergeométrica confluente.

**B10 — Termodinâmica clássica**

A magnetização é um sobre N beta vezes a derivada de log Z em H: H sobre dois vezes mi menos J sobre dois. Com o vínculo, m ao quadrado é um menos um sobre dois beta mi. A suscetibilidade acima de T c é beta sobre um menos beta J.

A entropia é a derivada de T sobre N log Z em T, a mi fixo, e dá a equação quarenta e dois. A quarenta e um impressa é, na verdade, a energia livre phi. Acima de T c, a entropia é constante; abaixo, vai a menos infinito. O calor específico é meio abaixo e zero acima.

**B11 — Quantização canônica**

Aqui verifico o comutador: S r com p r dá i. E a parte local: g sobre dois p ao quadrado mais mi S ao quadrado é raiz de dois g mi vezes a adaga a mais meio. Em Fourier, a soma dos a r é raiz de N vezes a chapéu zero, então só o modo zero recebe a interação, com o termo menos J sobre quatro vezes raiz de g sobre dois mi vezes a zero mais a zero adaga ao quadrado, e o termo de campo. Os outros modos já são diagonais.

**B12 — Modo q igual a zero, rota direta**

Uma forma transparente de ver o resultado sem Bogoliubov. Defino as coordenadas coletivas S til zero e p til zero, que são canonicamente conjugadas. No modo coletivo, a hamiltoniana é g sobre dois p til ao quadrado mais mi menos J sobre dois vezes S til ao quadrado, menos H raiz de N S til. Completando o quadrado, é um oscilador deslocado com mola dois vezes mi menos J sobre dois, frequência ômega zero, e o deslocamento só gera a constante menos N H ao quadrado sobre quatro vezes mi menos J sobre dois.

**B13 — Bogoliubov**

A versão do artigo. A parte quadrática do modo zero é A a adaga a menos B sobre dois vezes a ao quadrado mais a adaga ao quadrado. Com b zero igual a u a zero menos v a zero adaga, e u ao quadrado menos v ao quadrado igual a um, os termos não diagonais se anulam se u ao quadrado mais v ao quadrado for A sobre ômega zero e dois u v for B sobre ômega zero. A frequência é raiz de A ao quadrado menos B ao quadrado, a mesma da rota direta.

A translação absorve o campo. Uma observação: o w da equação cinquenta e oito é o deslocamento de a zero; em b zero, ele aparece multiplicado por u menos v. Não muda a função de partição.

**B14 — Xi, vínculo quântico e o termo log beta g**

A função de partição quântica, equação sessenta e três. O vínculo é a derivada da energia livre em mi igual a um, usando que a derivada de ômega em mi é g sobre ômega. Cada termo é o valor médio de S ao quadrado de um oscilador.

Quando g vai a zero, a diferença entre a energia livre quântica e a clássica tende a um sobre dois beta vezes log de dois pi beta g. É a energia livre clássica dos momentos. Ela não depende de H nem de mi, então não muda a magnetização nem o vínculo, mas muda a entropia.

**B15 — Integrais de trajetória**

A lagrangiana vem da transformada de Legendre, com S ponto igual a g p. Em tempo imaginário, com trajetórias periódicas, expando em modos espaciais e frequências de Matsubara. A ação fica uma soma de termos beta ao quadrado vezes ômega n ao quadrado sobre dois g mais mi menos J sobre dois delta de q zero, vezes o módulo ao quadrado.

O produto sobre n se resolve com a identidade produto de um mais x ao quadrado sobre pi ao quadrado n ao quadrado igual a seno hiperbólico de x sobre x. Fixando a normalização pelo limite clássico, cada modo dá um sobre dois seno hiperbólico de beta ômega sobre dois.

**B16 — Curva crítica**

A forma explícita da fronteira: k B T c é raiz de g J sobre duas vezes o arco tangente hiperbólico de meio raiz de g sobre J. Para g pequeno, expandindo a cotangente como um sobre y mais y sobre três, k B T c é aproximadamente J menos g sobre doze. Perto de g c, usando cotangente aproximadamente um mais dois exponencial de menos dois y, a temperatura crítica vai a zero como dois J sobre log de quatro g c sobre g c menos g, só logaritmicamente.

**B17 — Magnetização e suscetibilidade quânticas**

A magnetização é a mesma expressão do caso clássico. Com o vínculo, m zero ao quadrado é um menos meio raiz de g sobre J vezes a cotangente. A T igual a zero, é um menos raiz de g sobre g c, que perto de g c é menos g menos g c sobre dois g c: beta g igual a meio.

Na fase desordenada, a T igual a zero, mi é g sobre oito, e chi é quatro sobre g menos g c: gama g igual a um. E para g indo a zero, mi é um sobre dois beta, e voltamos ao clássico.

**B18 — Entropia e calor específico quânticos**

Para cada oscilador, com x igual a beta ômega sobre dois, a entropia é menos log de dois seno hiperbólico de x mais x cotangente hiperbólica de x, que para x grande se comporta como um mais dois x vezes exponencial de menos dois x. O calor específico é x ao quadrado sobre seno hiperbólico de x ao quadrado, a forma de Einstein: vai a zero exponencialmente e tende a um a temperatura alta. E para g indo a zero, a entropia quântica tende à clássica mais a entropia dos momentos. Por isso os limites não comutam.

**B19 — Campos aleatórios**

Esta derivação é minha, seguindo o método do artigo, e conversa com a lista sete, problema um. Trocando o campo uniforme por campos aleatórios de média zero e variância delta ao quadrado, cada modo de Fourier vira um oscilador deslocado pelo seu campo. O vínculo ganha o termo da soma dos campos ao quadrado sobre quatro vezes mi menos meio J chapéu ao quadrado, que, para os modos com q diferente de zero e N grande, tende a delta ao quadrado sobre quatro mi ao quadrado.

Com mi igual a J sobre dois, a superfície crítica é: um igual a delta ao quadrado sobre J ao quadrado mais o termo térmico e quântico. Com g igual a zero, k B T c é J vezes um menos delta ao quadrado sobre J ao quadrado. A T igual a zero, meio raiz de g c sobre J é um menos delta ao quadrado sobre J ao quadrado. Isso deve ser conferido com Vojta e Schreiber.

**B20 — Erratas**

Por fim, a tabela de pequenas erratas do texto impresso. O fator dois na temperatura crítica do modelo gaussiano, que vem da definição de b. Na equação cinco, falta a linha em S r linha. Na seis, o expoente deve ser s vezes N menos a soma dos quadrados. Nas vinte e vinte e dois, o termo de campo tem N elevado a mais meio. Na vinte e um, o expoente é i q ponto h. Na vinte e seis, o produto não tem log. Nas trinta e um e trinta e três, o denominador do termo de campo é ao quadrado. A quarenta e um é a energia livre, não a entropia. Na cinquenta e três, a soma é em q. A cinquenta e oito dá o deslocamento de a zero. E na cinquenta e nove, o lado esquerdo é menos Q sobre beta. Nenhuma altera os resultados físicos, e todas as passagens estão nos slides B um a B dezoito.
