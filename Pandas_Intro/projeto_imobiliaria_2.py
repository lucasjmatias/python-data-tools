import pandas as pd

arquivo = "aluguel.csv"

dtypes = {
    "Bairro": "category",
}

dados = pd.read_csv(arquivo, sep=";", dtype=dtypes)

dados.head()

dados["Valor_por_mes"] = dados.Valor + dados.Condominio

dados.head()

dados["Valor_por_ano"] = dados.Valor_por_mes * 12 + dados.IPTU

dados.head()

dados["Descricao"] = (
    dados["Tipo"]
    + " em "
    + dados["Bairro"].astype(str)
    + " com "
    + dados["Quartos"].astype(str)
    + " quarto(s) "
    + " e "
    + dados["Vagas"].astype(str)
    + " vaga(s) de garagem"
)

dados.head()

dados["Possui_suite"] = dados["Suites"].apply(lambda x: "Sim" if x > 0 else "Não")

dados.head()

dados.to_csv("dados_completos_dev.csv", index=False, sep=";")
