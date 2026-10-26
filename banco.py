import json
import os


arquivo = os.path.join(
    os.path.dirname(__file__),
    "dados.json"
)


def carregar_dados():

    if not os.path.exists(arquivo):

        dados = {
            "alunos": [],
            "pagamentos": []
        }

        salvar_dados(dados)

        return dados


    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)



def salvar_dados(dados):

    with open(arquivo, "w", encoding="utf-8") as f:

        json.dump(
            dados,
            f,
            indent=4,
            ensure_ascii=False
        )