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
    - 1: Bom Pagador, i.e. pagou todo o empréstimo.
    - 0: Mau Pagador, i.e. não pagou o crédito concedido.

- O score do modelo de classificação deve mapear a classe Bom Pagador.

- A base de dados está contida na pasta [../datasets/credit_01](../datasets/credit_01/) e é dividida em 3 partes:

    - **Treino**: base usada para treinamento contendo dados de janeiro a agosto de 2017;

    - **Teste**: base usada para testes contendo dados de janeiro a agosto de 2017;

    - **Out-of-time (oot)**: contém dados obtidos de setembro a novembro de 2017. A escoragem dessa base pode ser uma etapa do desafio, a depender das condições e requisitos combinados.

        - A base outoftime é considerada uma base "cega" por não possuir a variável `"TARGET"` (apenas a equipe do Prophet/Neurolake possui acesso a essa variável).

### Análise financeira

Considere que seu cliente já possui uma política de gestão de risco de crédito (que chamaremos de `AS-IS`), que consiste em reprovar qualquer pessoa que tenha **idade** igual ou inferior a 28 anos. Ou seja: se alguém nessa faixa etária solicita crédito à instituição financeira, sua solicitação é negada.

O score gerado pelo modelo de machine learning proposto pode ser utilizado para gerar uma segunda política, chamada `TO-BE`: uma vez que ele mapeia a confiança de que a pessoa irá honrar o empréstimo, o cliente pode substituir o ponto de corte em **Idade** para um ponto de corte no **Score**.

Para realizar a análise financeira do seu modelo, suponha que todas as pessoas da base de **Teste** solicitaram crédito à instituição financeira, na forma de um empréstimo de R$1000,00. Faça o seguinte:

1. Calcule qual o tamanho da carteira de crédito aprovado (i.e. quanto de dinheiro a Financeira emprestou) na base de Teste, pela Política AS-IS.

2. Calcule qual a dívida total (suponha que os inadimplentes não pagaram nenhuma parcela do empréstimo), pela Política AS-IS.

3. Calcule qual o **percentual** das pessoas da base de Teste que tiveram a solicitação negada. Agora **crie um ponto de corte** de seu Score que nega o empréstimo para exatamente o mesmo **percentual** de pessoas (i.e. o empréstimo será negado para quem tiver o Score igual ou inferior ao ponto de corte). Essa é a Política TO-BE.

4. Calcule o novo tamanho da carteira de crédito aprovado e a dívida total na Política TO-BE.
