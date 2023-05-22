# Modelos preditivos para a área da Saúde

## Projeto 1: propensão a condição crítica de saúde

Uma empresa do ramo de saúde quer prever uma situação de saúde crítica de seus clientes no futuro, de modo a atuar de maneira preventiva com grupos de pessoas que possuem maior risco de desenvolver essa condição crítica. Seu trabalho enquanto cientista de dados será implementar um modelo de machine learning para resolver o problema.

### Dados e objetivo

Para isso foi disponibilizada uma base de dados com 50 mil casos, mil variáveis e um alvo (situação crítica 1, não crítica 0). Os dados estão divididos em uma base de [**Treino**](https://drive.google.com/file/d/1cBiizQ0ftP16dxqSQ8XVcf5oYIwEHkIU/view?usp=sharing) e outra de [**Teste**](https://drive.google.com/file/d/13AoBow1bEiAmmw9fqi0sv-QaoTciLiid/view?usp=sharing). Para resolver o desafio, é necessário desenvolver um modelo de classificação para prever a situação crítica de saúde, selecionando as variáveis que possuem maior relevância para o problema, de modo que só entrem em produção até 100 variáveis no máximo.

### Avaliação

Avalie seu modelo nas bases de treino e de teste, trazendo as métricas de Área Sob a Curva ROC, Matriz de Confusão, Taxa do Alvo no Decil 10 e Taxa do Alvo no Percentil 100 (ordene a base de teste pelo score, some o alvo real e divida pela quantidade de casos de acordo com o top 10% e top 1%, respectivamente). Além da análise técnica, faça uma avaliação de negócio, interpretando os números obtidos e indicando como o seu modelo de machine learning impactaria positivamente a empresa de saúde e seus clientes.