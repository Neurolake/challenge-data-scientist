# Projetos para modelagem de risco em Crédito

## Projeto 1: desenvolver um modelo de concessão de crédito

Para este problema de negócio, o cientista de dados deverá desenvolver um modelo de concessão de crédito (classificação binária) usando as bases descritas na subseção `Dataset` abaixo.

O **projeto completo** (certos processos seletivos podem pedir apenas parte dele) compreende as seguintes atividades:

1. **Entendimento da base** e análise exploratória dos dados.
2. **Pré-processamento** das variáveis.
3. **Treinamento** de um modelo de classificação binária.
4. **Análise técnica** da performance do modelo, medida sobre a base de **Teste**.
5. **Análise financeira** do modelo. Para este ponto, observe a subseção `Análise financeira`.
6. **Escoragem da base Out-of-time**, para posterior avaliação da performance nessa base com o alvo detido pelo Prophet/Neurolake.

Artefato mínimo esperado ao fim do projeto:

1. Um Jupyter Notebook legível, contendo as etapas do projeto.

O cientista de dados pode livremente produzir outros artefatos que julgar relevantes para a apresentação do seu projeto. Alguns processos seletivos podem pedir a base Out-of-time escorada.

### Dataset
- A base contém **150** variáveis, a maioria das quais está mascarada. Utilize a coluna `ID` como uma _key_.

- A variável alvo é denominada **TARGET** e possui os seguintes valores:
    - 1: Mau Pagador, i.e. atraso > 60 dias em 2 meses.
    - 0: Bom Pagador, i.e. caso contrário.

- O score do modelo de classificação deve mapear a classe Bom Pagador.

- A base de dados está contida na pasta [../datasets/credit_01](../datasets/credit_01/) e é dividida em 3 partes:

    - **Treino**: base usada para treinamento contendo dados de janeiro a agosto de 2017;

    - **Teste**: base usada para testes contendo dados de janeiro a agosto de 2017;

    - **Out-of-time (oot)**: contém dados obtidos de setembro a novembro de 2017. A escoragem dessa base pode ser uma etapa do desafio, a depender das condições e requisitos combinados.

        - A base outoftime é considerada uma base "cega" por não possuir a variável `"TARGET"` (apenas a equipe do Prophet/Neurolake possui acesso a essa variável).

### Análise financeira

Considere que seu cliente já possui uma política de gestão de risco de crédito fictícia (que chamaremos de `AS-IS`), que consiste em reprovar qualquer pessoa que tenha **idade** igual ou inferior a 28 anos. Ou seja: se alguém nessa faixa etária solicita crédito à instituição financeira, sua solicitação é negada.

O score gerado pelo modelo de machine learning proposto pode ser utilizado para gerar uma segunda política, chamada `TO-BE`: uma vez que ele mapeia a propensão da pessoa honrar o empréstimo (classe Bom Pagador), o cliente pode substituir o ponto de corte em **Idade** por um novo ponto de corte no **Score**, de modo que as solicitações de crédito na política `TO-BE` serão reprovadas se e somente se o cliente tiver score abaixo deste ponto de corte.

Para realizar a análise financeira do seu modelo, **considere apenas o mês de agosto de 2017**. suponha que todas as pessoas da base de **Teste** solicitaram crédito à instituição financeira, na forma de um empréstimo de R$1000,00. Faça o seguinte:

1. Calcule qual o tamanho da carteira de crédito aprovado (i.e. quanto de dinheiro a Financeira emprestou) na base de Teste, pela Política AS-IS.

2. Calcule qual a dívida total (suponha que os inadimplentes não pagaram nenhuma parcela do empréstimo), pela Política AS-IS.

3. Calcule qual o **percentual** das pessoas da base de Teste que tiveram a solicitação negada. Agora **crie um ponto de corte** de seu Score que negaria o empréstimo para exatamente o mesmo **percentual** de pessoas. Essa é a Política TO-BE.

4. Calcule o novo tamanho da carteira de crédito aprovado e a dívida total na Política TO-BE. Calcule a economia gerada por seu modelo.


## Projeto 2: Desenvolver um modelo de recuperação de dívidas

Para este problema de negócio, o cientista de dados deverá desenvolver um modelo de recuperação de dívidas (classificação binária) usando as bases descritas na subseção `Dataset` abaixo.

O **projeto completo** (certos processos seletivos podem pedir apenas parte dele) é similar ao que descrito no Projeto 1, compreende as seguintes atividades:

1. **Entendimento da base** e análise exploratória dos dados.
2. **Pré-processamento** das variáveis.
3. **Treinamento** de um modelo de classificação binária.
4. **Análise técnica** da performance do modelo.
5. **Análise de negócio (Para Cientista I - OPCIONAL; A partir de Cientista II - Obrigatório)**, interpretando os números obtidos e indicando como o seu modelo de machine learning impactaria positivamente a empresa e seus clientes.

Artefato mínimo esperado ao fim do projeto:

1. Um Jupyter Notebook legível, contendo as etapas do projeto.

O cientista de dados pode livremente produzir outros artefatos que julgar relevantes para a apresentação do seu projeto.

2. Apenas a partir de Cientista II:

Uma apresentação, em Google Slides, Power Point ou algum software de sua preferência, com os principais aprendizados e recomendações da análise de negócios

### Dataset
- A base contém **203** variáveis, a maioria das quais está mascarada. Utilize a coluna `index` como uma _key_.

- A variável alvo possui os seguintes valores:
    - 1: Mau Pagador
    - 0: Bom Pagador

- O score do modelo de classificação deve mapear a classe Bom Pagador. **Você deve deixar claro quais foram os critérios utilizados no score para definição das classes de nível de Pagador**

- A base de dados está contida na pasta [../datasets/credit_02](../datasets/credit_02/)


## Projeto 3: desenvolver uma solução para Cobrança

Este desafio é mais *open-ended*. Na pasta [../datasets/credit_03](../datasets/credit_03/) você encontrará um dataset de nome `base_cobranca.gz`, com dados relacionados ao problema de cobrança de dívidas associadas a financiamento veicular, com 300000 linhas e 328 colunas, das quais 316 estão mascaradas.

A seguir você encontra as primeiras 3 linhas e 9 colunas:

| id         | documento | mes_pagamento | dias_atraso | segmento_veiculo | saldo_vencido | pagamento | divida_restante | per_pago |
|------------|-----------|---------------|-------------|------------------|---------------|-----------|-----------------|----------|
| 0x117651   | 0x722945  | 202301        | 18          | leves            | 1445.37       | 0.00      | 1445.37         | 0.000000 |
| 0x80136d   | 0x7fa1e8  | 202301        | 28          | motos            | 426.84        | 426.84    | 0.00            | 1.000000 |
| 0x839c27   | 0x724e31  | 202301        | 30          | leves            | 1381.98       | 1381.98   | 0.00            | 1.000000 |

A forma de ler o conteúdo da primeira linha é a seguinte: o cliente de ID 0x117651, no mês 202301, estava com 18 dias de atraso e com saldo devedor de R$1445,37, e não pagou nada da dívida. Já o segundo cliente, na segunda linha, pagou integralmente a dívida.

Obs.: para possibilitar a leitura da base `base_cobranca.gz`, considere que ela foi salva usando o caracter `\t` como separador.

**Objetivo**: seu objetivo neste desafio é criar uma solução que consiga melhorar a taxa de conversão de dívidas usando machine learning (seja com um modelo único, seja com um modelo por persona). Use os 4 últimos meses (na coluna `mes_pagamento`) como definição da base de validação "out of time".