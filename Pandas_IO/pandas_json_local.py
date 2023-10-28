import pandas as pd

import json


with open('pacientes_2.json', 'r') as f:
    dados = json.loads(f.read())

df = pd.json_normalize(dados, record_path="Pacientes", meta=["Ano", "Pesquisa"])

df.head()
