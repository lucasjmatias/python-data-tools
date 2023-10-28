import pandas as pd

arquivo = "aluguel.csv"

dtypes = {
    "Bairro": "category",
}

dados = pd.read_csv(arquivo, sep=";", dtype=dtypes)

dados.head()

dados.tail()

type(dados)


dados.shape

dados.columns

dados.info()

dados["Tipo"]

dados[["Tipo", "Vagas"]]

dados[["Quartos", "Valor"]]


# Valor médio de aluguel por tipo de imóvel

dados[["Tipo", "Valor"]]

dados["Valor"].mean()

dados.groupby("Tipo").mean(numeric_only=True)


df_preco_tipo = dados.groupby("Tipo")[["Valor"]].mean().sort_values("Valor")

df_preco_tipo.plot(kind="barh", figsize=(14, 10), color="purple")

imoveis_comerciais = [
    "Conjunto Comercial/Sala",
    "Prédio Inteiro",
    "Loja/Salão",
    "Galpão/Depósito/Armazém",
    "Casa Comercial",
    "Terreno Padrão",
    "Loja Shopping/ Ct Comercial",
    "Box/Garagem",
    "Chácara",
    "Loteamento/Condomínio",
    "Sítio",
    "Pousada/Chalé",
    "Hotel",
    "Indústria",
]

dados_imoveis_residenciais = dados.query("@imoveis_comerciais not in Tipo")

dados_imoveis_residenciais.Tipo.unique()

df_preco_tipo_ir = (
    dados_imoveis_residenciais.groupby("Tipo")[["Valor"]].mean().sort_values("Valor")
)
df_preco_tipo_ir.plot(kind="barh", figsize=(14, 10), color="purple")

dados_imoveis_residenciais.Tipo.unique()

dados_imoveis_residenciais.Tipo.value_counts()

dados_imoveis_residenciais.Tipo.value_counts(normalize=True)

dados_imoveis_residenciais.Tipo.value_counts(normalize=True).plot(kind="pie")

df_percentual_tipo = (
    dados_imoveis_residenciais.Tipo.value_counts(normalize=True)
    .to_frame()
    .sort_values("proportion")
)

df_percentual_tipo.plot(
    kind="bar", figsize=(14, 10), color="green", xlabel="Tipos", ylabel="Percentual"
)

df_apartamentos = dados_imoveis_residenciais.query("Tipo == 'Apartamento'")

df_apartamentos.head

df_apartamentos.isnull().sum()

df_apartamentos.Valor = df_apartamentos.Valor.fillna(0)
df_apartamentos.Condominio = df_apartamentos.Condominio.fillna(0)
df_apartamentos.IPTU = df_apartamentos.IPTU.fillna(0)

df_apartamentos.isnull().sum()

registros_a_remover = df_apartamentos.query("Valor == 0 | Condominio == 0").index

df_apartamentos.drop(registros_a_remover, axis=0, inplace=True)

df_apartamentos.query("Valor == 0 | Condominio == 0")

df_apartamentos.Tipo.unique()

df_apartamentos.drop("Tipo", axis=1, inplace=True)

df_apartamentos["Quartos"] == 1

selecao1 = df_apartamentos["Quartos"] == 1

df_apartamentos[selecao1]

selecao2 = df_apartamentos["Valor"] < 1200

df_apartamentos[selecao2]

selecao_final = selecao1 & selecao2

df_1 = df_apartamentos[selecao_final]


selecao = (
    (df_apartamentos.Quartos >= 2)
    & (df_apartamentos.Valor < 3000)
    & (df_apartamentos.Area > 70)
)

df_2 = df_apartamentos[selecao]

df_2.to_csv("dados_apartamentos.csv", index=False)
df_2.to_markdown("dados_apartamentos.md")

df_2.to_csv("dados_apartamentos.csv", sep=";", index=False)
