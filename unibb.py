# %%
import os

from dotenv import load_dotenv
import pandas as pd
import sqlalchemy as sa

load_dotenv()

engine: sa.Engine = sa.engine.create_engine(os.getenv("URL_MYSQL"))
# engine: sa.Engine = sa.engine.create_engine(os.getenv("URL_SQLITE"))

# %%
stmt: str = """
    CREATE TABLE IF NOT EXISTS unibb (
        id INTEGER AUTO_INCREMENT PRIMARY KEY,
        id_curso INTEGER NOT NULL,
        nm_curso TEXT NOT NULL,
        hr_curso INTEGER NOT NULL
    )
"""
with engine.begin() as cnx:
    cnx.execute(sa.text(stmt))
print("Tabela criada com sucesso.\n")

# %%
try:
    df_new: pd.DataFrame = pd.read_csv("./src/unibb.csv", encoding="utf-8-sig")
    df_new = df_new[df_new["save"].eq(1)][["id_curso", "nm_curso", "hr_curso"]]
    rows_inserted: int = df_new.to_sql(name="unibb", con=engine, if_exists="append", index=False)
    print(f"Foram {rows_inserted} cursos inseridos com sucesso.")
except FileNotFoundError:
    print("Erro ao localizar o arquivo .CSV...")
except UnicodeEncodeError:
    print("Erro ao decodificar o arquivo .CSV...")
else:
    df_deleted: pd.DataFrame = pd.read_csv("./src/unibb.csv", encoding="utf-8-sig")
    df_deleted[df_deleted["save"].ne(1)].to_csv("./src/unibb.csv", index=False, encoding="utf-8-sig")
    print("Cursos atualizados com sucesso.\n")

# %% lista de cursos com id ordenado
stmt: str = "SELECT id_curso AS Código, nm_curso AS Curso, hr_curso AS Horas FROM unibb ORDER BY id"
print(pd.read_sql_query(sql=sa.text(stmt), con=engine))

# %% lista de cursos com id_curso ordenado
stmt: str = "SELECT id_curso AS Código, nm_curso AS Curso, hr_curso AS Horas FROM unibb ORDER BY id_curso"
print(pd.read_sql_query(sql=sa.text(stmt), con=engine))

# %% lista de cursos duplicados
stmt: str = """
    SELECT id_curso AS Código, nm_curso AS Curso, hr_curso AS Horas FROM unibb WHERE nm_curso IN (
        SELECT nm_curso FROM unibb GROUP BY nm_curso HAVING COUNT(nm_curso) > 1
    ) ORDER BY nm_curso, id_curso
"""
print(pd.read_sql_query(sql=sa.text(stmt), con=engine))
