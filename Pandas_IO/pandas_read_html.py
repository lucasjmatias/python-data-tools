import pandas as pd

url = "https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o"

tabelas = pd.read_html(url)

len(tabelas)

tabelas[0]

populacao = tabelas[0]

populacao.drop('Unnamed: 0', axis='columns', inplace=True) 

populacao.to_html("populacao.html", index=False)

populacao.head()