# Monitoramento de modelos de _machine learning_

## Projeto 1: API para avaliação de aderência e performance

Ciência de Dados é uma área multidisciplinar, bem o sabemos, envolvendo estatística, matemática, engenharia de software e conhecimento especialista de negócio. Para este projeto, o cientista de dados colocará o seu chapéu de desenvolvedor e **criará uma API para avaliação de aderência e performance de um modelo de machine learning**.

Você pode utilizar o esqueleto na pasta [../monitoring/app/](../monitoring/app) como ponto de partida para sua API. Para executá-la, crie um ambiente Python (Conda) novo e instale as dependências em [../monitoring/app/requirements.txt](../monitoring/app/requirements.txt) (e outras dependências que ache necessárias).

Entregáveis:
- O repositório no Github contendo sua API.
- Um Jupyter notebook, mostrando uma chamada a cada um dos 2 endpoints (dado que, no momento da execução do Notebook localmente, sua API esteja rodando localmente) e contendo o que se pede nos pontos *Como avaliar no Notebook*, das subseções 1.1 e 1.2 abaixo.

A API deve ser feita com FastAPI e Uvicorn, e deve conter os seguintes endpoints POST:

### 1.1 Performance e volumetria
O primeiro endpoint deve receber uma lista de *registros*, em que cada registro deve conter valores de variáveis usadas no modelo, além de uma data de referência e o valor do alvo para aquele registro. O "body" usado na requisição fica a seu critério. Exemplo de conteúdo do registro (aqui ele é representado como um simples dicionário, mas a forma como você vai organizar o "body" da requisição é livre, desde que fique clara na documentação de sua API):
```json
{
    "VAR2": "M",
    "IDADE": 43.893,
    "VAR5": "PR",
    "VAR6": -25.4955709,
    "VAR7": -49.2454987,
    "VAR8": "D",
    "VAR9": "E",
    "VAR10": "MEDIA",
    "VAR11": 1.0,
    "VAR12": 0.182,
    "VAR14": 0.597,
    "VAR15": 0.618,
    "VAR16": 0.25,
    "VAR18": 1.076712,
    "VAR19": 5.057534,
    "VAR22": 0.125,
    "VAR24": 0.069,
    "VAR25": 0.0969999999999999,
    "VAR32": "SALDO INEXISTENTE",
    "VAR39": 0.661039,
    "VAR40": 0.573539,
    "VAR41": 0.4793699999999999,
    "VAR42": 0.4440489999999999,
    "VAR47": 0.006,
    "VAR49": "S",
    "VAR50": "N",
    "VAR51": "N",
    "VAR52": "N",
    "VAR53": "N",
    "VAR54": "N",
    "VAR55": "N",
    "VAR56": "S",
    "VAR57": "S",
    "VAR58": "N",
    "VAR59": "N",
    "VAR60": "N",
    "VAR61": "N",
    "VAR62": "N",
    "VAR63": "N",
    "VAR64": "N",
    "VAR65": "N",
    "VAR66": "ALTISSIMA",
    "VAR67": "ALTA",
    "VAR68": "ALTISSIMA",
    "VAR69": "ALTISSIMA",
    "VAR70": "ALTISSIMA",
    "VAR71": "ALTA",
    "VAR72": "ALTISSIMA",
    "VAR73": "ALTISSIMA",
    "VAR74": "ALTISSIMA",
    "VAR75": "ALTISSIMA",
    "VAR76": "ALTA",
    "VAR77": "ALTISSIMA",
    "VAR78": "ALTISSIMA",
    "VAR79": "ALTISSIMA",
    "VAR80": "ALTA",
    "VAR81": "ALTA",
    "VAR82": "ALTISSIMA",
    "VAR83": "ALTISSIMA",
    "VAR84": "ALTA",
    "VAR85": "ALTA",
    "VAR86": "ALTA",
    "VAR87": "ALTISSIMA",
    "VAR88": "ALTA",
    "VAR89": "ALTISSIMA",
    "VAR90": "BAIXISSIMA",
    "VAR91": "ALTA",
    "VAR92": "ALTISSIMA",
    "VAR93": "ALTISSIMA",
    "VAR94": "ALTISSIMA",
    "VAR95": "ALTA",
    "VAR96": "ALTISSIMA",
    "VAR97": "ALTA",
    "VAR98": "ALTISSIMA",
    "VAR99": "ALTISSIMA",
    "VAR100": "BAIXISSIMA",
    "VAR101": "ALTA",
    "VAR102": "MEDIO",
    "VAR103": "MEDIO",
    "VAR104": "PROXIMO",
    "VAR105": "LONGE",
    "VAR106": "MEDIO",
    "VAR107": "MEDIO",
    "VAR108": "MEDIO",
    "VAR109": "MEDIO",
    "VAR110": "PROXIMO",
    "VAR111": "MEDIO",
    "VAR112": "MEDIO",
    "VAR113": "PROXIMO",
    "VAR114": "PROXIMO",
    "VAR115": "MEDIO",
    "VAR116": "LONGE",
    "VAR117": "MEDIO",
    "VAR118": "MEDIO",
    "VAR119": "LONGE",
    "VAR120": "MUITO LONGE",
    "VAR121": "MEDIO",
    "VAR122": "MEDIO",
    "VAR123": "MEDIO",
    "VAR124": "MEDIO",
    "VAR125": "PROXIMO",
    "VAR126": "MEDIO",
    "VAR127": "PROXIMO",
    "VAR128": "LONGE",
    "VAR129": "MEDIO",
    "VAR130": "MEDIO",
    "VAR131": "MEDIO",
    "VAR132": "PROXIMO",
    "VAR133": "MEDIO",
    "VAR134": "PROXIMO",
    "VAR135": "MEDIO",
    "VAR136": "MEDIO",
    "VAR137": "MEDIO",
    "VAR138": "MEDIO",
    "VAR139": "MEDIO",
    "VAR140": "MUITO PROXIMO",
    "VAR141": 3970.113648,
    "VAR142": "C",
    "REF_DATE": "2017-03-25 00:00:00+00:00",
    "TARGET": 1
}
```
A resposta da requisição POST deve conter:

(a) A volumetria (quantidade de registros) para cada mês presente na lista de registros (lembre que temos uma entrada no dicionário que contém uma data de referência),

(b) A performance do modelo pré-treinado [../monitoring/model.pkl](../monitoring/model.pkl) neste conjunto de registros, indicada pelo valor da área sob a curva ROC. Para rodar o modelo, é necessário um ambiente Python com estas dependências mínimas: [../monitoring/requirements.txt](../monitoring/requirements.txt).

**Como avaliar no Notebook**:
Utilize a lista de registros presente no JSON [../monitoring/batch_records.json](../monitoring/batch_records.json) e faça uma requisição POST ao seu endpoint com essa lista. Deixe visível no seu notebook o retorno da requisição, contendo os itens (a) e (b) descritos acima.

Para calcular o item (b), i.e. a performance do modelo, você precisará transformar a lista de registros no JSON [../monitoring/batch_records.json](../monitoring/batch_records.json) em um Pandas DataFrame, tomar o cuidado de substituir os valores nulos das variáveis pelo valor NaN do Numpy, `np.nan`, e ler o modelo em formato Pickle [../monitoring/model.pkl](../monitoring/model.pkl).


### 1.2 Aderência

Neste endpoint, espera-se que você indique o quanto a distribuição de scores em uma certa base está distante, ou diferente, da distribuição vista na base de Teste, da modelagem. Utilize o teste estatístico de Kolmogorov-Smirnov (KS) como métrica que quantifica essa distância entre as distribuições, podendo opcionalmente também incluir outras métricas de sua escolha, desde que justificando a escolha.

No "body" da requisição, você deve indicar o caminho para um dataset armazenado localmente, e a API irá lê-lo e utilizar o modelo pré-treinado [../monitoring/model.pkl](../monitoring/model.pkl) para escorar esta base (i.e. criar uma coluna com o score, a probabilidade do registro pertencer à classe 1 do Alvo). Depois, a API deve calcular a métrica de distância de distribuições de score entre a **base fornecida como input** da requisição e a **base de [../datasets/credit_01/test.gz](Teste)**, e colocá-la no retorno do endpoint.

**Como avaliar no Notebook**:
Teste seu endpoint com duas bases:

(a) a base de [../datasets/credit_01/train.gz](Treino),
(b) a base [../datasets/credit_01/oot.gz](Out-of-time), contendo registros (sem alvo) coletados em meses subsequentes aos meses de Treino e Teste.
