URL_LOGIN = "https://portal.easynvest.com.br/autenticacao/login"
URL_RENDA_FIXA = "https://portal.easynvest.com.br/financascustodia/rendafixa/"

RENDA_FIXA = "renda_fixa"

COLUMNS_RENDA_FIXA = {
    "nome": "./td[1]/a/text()",
    "emissor": "./td[2]/text()",
    "quantidade": "./td[3]/text()",
    "investimento": "./td[4]/text()",
    "vencimento": "./td[5]/text()",
    "taxa_negociada": "./td[6]/text()",
    "ir_iof_taxa": "./td[7]/text()",
    "valor": "./td[8]/text()"
}
