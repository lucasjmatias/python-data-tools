import pandas as pd
from sqlalchemy import create_engine, text as sql_text, inspect


url = "https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv"
dados = pd.read_csv(url)

engine = create_engine('sqlite:///:memory:')
conn = engine.connect()
dados.to_sql('clientes', conn, index=False)
query = sql_text("SELECT * FROM clientes WHERE Categoria_de_renda = 'Empregado'")
empregados = pd.read_sql(query, conn)
empregados.to_sql('empregados', conn, index=False)
conn.commit()
inspector = inspect(engine)
print(inspector.get_table_names())
print(pd.read_sql_table('empregados', conn, columns=['ID_Cliente', 'Grau_escolaridade', 'Rendimento_anual']))

clientes = pd.read_sql_table('clientes', conn)
clientes.head()

conn.close()

delete_query = sql_text("DELETE FROM clientes WHERE ID_Cliente = 5008804")
with engine.connect() as conn:
  conn.execute(delete_query)
  conn.commit()
