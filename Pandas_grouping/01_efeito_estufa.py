import pandas as pd

"""
Data source:
https://caelum-online-public.s3.amazonaws.com/2927-pandas-selecao-agrupamento-dados/pandas_selecao_e_agrupamento.ipynb
"""

emissao_gases = pd.read_excel(
    ".\\data\\1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx", sheet_name="GEE Estados"
)

emissao_gases.head()

emissao_gases.columns

emissao_gases.info()

emissao_gases.describe()
