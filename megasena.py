from dotenv import load_dotenv
import locale
import os
import numpy as np
import pandas as pd
import sqlalchemy as sa

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

pd.set_option("display.max_columns", 9)

load_dotenv()

engine = sa.create_engine(os.getenv("URL_MYSQL"))


def create():
    stmt = """
        CREATE TABLE IF NOT EXISTS megasena (
            concurso MEDIUMINT UNSIGNED NOT NULL,
            data DATE NOT NULL,
            bola1 TINYINT(2) UNSIGNED NOT NULL CHECK (bola1 >= 1 AND bola1 <= 60),
            bola2 TINYINT(2) UNSIGNED NOT NULL CHECK (bola2 >= 1 AND bola2 <= 60),
            bola3 TINYINT(2) UNSIGNED NOT NULL CHECK (bola3 >= 1 AND bola3 <= 60),
            bola4 TINYINT(2) UNSIGNED NOT NULL CHECK (bola4 >= 1 AND bola4 <= 60),
            bola5 TINYINT(2) UNSIGNED NOT NULL CHECK (bola5 >= 1 AND bola5 <= 60),
            bola6 TINYINT(2) UNSIGNED NOT NULL CHECK (bola6 >= 1 AND bola6 <= 60),
            ganhou TINYINT(1) NOT NULL DEFAULT 0,
            PRIMARY KEY (concurso, data)
        )
    """

    with engine.begin() as cnx:
        try:
            cnx.execute(sa.text(stmt))
        except sa.exc.OperationalError:
            print("Deu erro ao criar a tabela...")
        else:
            print("Tabela criada com sucesso.")


def add():
    new = [
        {"concurso": 2743,
         "data": "2024-06-29",
         "bola1": 13,
         "bola2": 25,
         "bola3": 27,
         "bola4": 30,
         "bola5": 37,
         "bola6": 53,
         "ganhou": False},
    ]
    df_new = pd.DataFrame(new)
    rows_inserted = df_new.to_sql(name="megasena", con=engine, if_exists="append", index=False)
    print(f"Foram {rows_inserted} jogos inseridos com sucesso.")


def view():
    df = pd.read_sql(sql=sa.text("SELECT * FROM megasena"), con=engine)
    df["concurso"] = df["concurso"].astype(str).str.zfill(4)
    df["data"] = pd.to_datetime(df["data"]).dt.strftime("%x (%a)")
    for x in ["bola1", "bola2", "bola3", "bola4", "bola5", "bola6"]:
        df[x] = df[x].apply(lambda y: str(y).zfill(2))
    df["ganhou"] = np.where(df["ganhou"], "Sim", "Não")
    df.columns = ["Concurso", "Data", "(1)", "(2)", "(3)", "(4)", "(5)", "(6)", "Ganhou?"]
    print(df.tail(25))


if __name__ == "__main__":
    while True:
        print("-" * 50)
        print(" 1 - Criar Nova Tabela...")
        print(" 2 - Adicionar Novos Registros...")
        print(" 3 - Visualizar 25 Últimos Registros...")
        print("-" * 50)

        option: str = input("Escolha a opção acima (ou tecla ENTER para sair) → ")

        match option:
            case "1": create()
            case "2": add()
            case "3": view()
            case _: break
