# **Van Gogh - se**
 
## **Motivação**

Apresentar tarefas que podem ser arquivadas por redes neurais de forma simples e palpável para que as pessoas consigam interagir e compreender o mundo de possibilidades que essa área de estudo promete.

## **Ideia**

Para apresentar uma capacidade de redes neurais, eu pensei em fazer um projeto que pode gerar curiosidade para as pessoas e que traga um pouco mais de cultura também e foi daí que surgiu o projeto Van Gogh - se.

Esse projeto tem como ideia usar uma rede neural para que quando uma pessoa submeter uma foto a rede neural, essa foto adquira características de uma pintura do Van Gogh e este resultado seja mostrado para a pessoa que submeteu.

Com isso, mostramos uma funcionalidade e geramos algo que as pessoas podem usar para se divertir e brincar com seus conhecidos e amigos e, além disso tudo, conhecer pinturas e até mesmo as que não são tão famosas.

Por que Van Gogh? Eu simplesmente me tornei um grande fã do artista desde que eu tive o primeiro contato com as obras dele quando estava cursando o 6º ano do ensino fundamental com aulas de história da arte.

## **Como o trabalho foi elaborado**

Como a ideia era termos um resultado rápido para levarmos essa tecnologia para o público, focamos em usar o máximo de códigos e bancos de dados prontos possíveis.

Logo, para fazer o script base para o notebook final foram usados os seguintes dados:

### **Dataset**
- https://www.kaggle.com/gfolego/vangogh
- https://www.kaggle.com/delayedkarma/impressionist-classifier-data (Apenas Van Gogh)

Depois foi apenas deixado as pinturas com as pinceladas fortes do Van Gogh, que são bem mais facilmente reconhecidas pelas pessoas. Mas, nada impede de usar toda a gama de quadros e desenhos já feito pelo Van Gogh.

### **Código**
- https://keras.io/examples/neural_style_transfer/

Usamos a biblioteca keras, que é uma biblioteca muito conhecida para trabalhar com inteligência artificial. Para a nossa felicidade, na página de exemplos existia um código para transferência de estilo que, como o próprio nome diz, extrai o estilo de uma imagem ( no nosso caso as pinturas do Van Gogh) e aplica em uma outra imagem ( no nosso caso as fotos enviadas pelo usuário) e gera uma terceira imagem que é a mescla destas duas.

Não estou entrando nas explicações técnicas porque o público alvo em sua maioria não são desenvolvedores. O que não impede que as pessoas mais curiosas queiram entrar nesse maravilhoso mundo. Para essas pessoas disponibilizaremos alguns links sobre esta técnica para que consigam uma introdução mais aprofundada sobre o assunto.


Neste script eu fiz umas pequenas modificações para tornar mais interessante a experiência do usuário, entre elas estão a seleção de uma imagem de estilo aleatória que permite que tenhamos para uma foto base diversas possibilidades a cada execução do código e a mudança dos modelos de VGG 19 para VGG 16 que permite um resultado mais rápido da rede porque diminuímos a quantidade de layers pelo qual a imagem passará.

### **Jupyter Notebook**

O que é um Jupyter Notebook? Não, não é um notebook em Júpiter ~~( o que seria bem interessante falar que estamos programando em Júpiter  )~~, mas um computador virtual que consegue ler códigos na linguagem python e escrever blocos de textos.

Por que usar esse notebook? Bom, primeiro que ele é ótimo para demonstrações, dado que podemos ter blocos de texto ( em markdown e html ) e blocos de código para serem executados. Em segundo, porque pensando na utilização deste script que utiliza muito hardware de um computador e muitas vezes mais hardware que a maioria das pessoas tem disponível, usaremos os notebooks hosteados pelo google na plataforma [**Google Colab**](https://colab.research.google.com/).

## **Conclusão**

Espero que os resultados da experiência tenha sido proveitosa, vocês tenham conseguido aprender mais sobre o artista e principalmente conhecer uma das capacidades da utilização de inteligência artificial.
