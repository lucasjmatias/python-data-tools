import pandas as pd
from sqlalchemy import create_engine, text as sql_text, inspect


url = "https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv"
dados = pd.read_csv(url)

"""
In order to present both ways 
"""
autoCommit = False

engine = create_engine('sqlite:///:memory:')
with engine.connect() as conn:
    if autoCommit:
        conn.execution_options(isolation_level="AUTOCOMMIT")
    with conn.begin():
        dados.to_sql('clientes', con=conn, index=False)
        query = sql_text("SELECT * FROM clientes WHERE Categoria_de_renda = 'Empregado'")
        empregados = pd.read_sql(query, conn)
        empregados.to_sql('empregados', con=conn, index=False)
        if not autoCommit:
            conn.commit()
    with conn.begin():
        inspector = inspect(engine)
        print(inspector.get_table_names())
        print(pd.read_sql_table('empregados', con=conn))
    with conn.begin():
        print(pd.read_sql_table('empregados', con=conn))
        delete_query = sql_text("DELETE FROM clientes WHERE ID_Cliente = 5008804")
        conn.execute(delete_query)
        if not autoCommit:
            conn.commit()
