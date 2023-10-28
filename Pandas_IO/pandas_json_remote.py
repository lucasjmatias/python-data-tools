import pandas as pd

import requests
import json

url = "https://raw.githubusercontent.com/alura-cursos/Pandas/main/pacientes_2.json"

req = requests.get(url)

dados = json.loads(req.text)

df = pd.json_normalize(dados, record_path="Pacientes", meta=["Ano", "Pesquisa"])

df.head()

