import locale
import os

from dotenv import load_dotenv
import numpy as np
import pandas as pd
import sqlalchemy as sa

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

pd.set_option("display.max_columns", 9)

load_dotenv()

engine: sa.Engine = sa.create_engine(os.getenv("URL_MYSQL"))


def create() -> None:
    stmt: str = """
        CREATE TABLE IF NOT EXISTS megasena (
            concurso MEDIUMINT UNSIGNED NOT NULL,
            data DATE NOT NULL,
            bolas VARCHAR(17) NOT NULL,
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


def add() -> None:
    new: list[dict] = [{"concurso": 2743, "data": "2024-06-29", "bolas": "13 25 27 30 37 53", "ganhou": False},]

    df_new: pd.DataFrame = pd.DataFrame(new)

    rows_inserted: int = df_new.to_sql(name="megasena", con=engine, if_exists="append", index=False)
    print(f"Foram {rows_inserted} jogos inseridos com sucesso.")


def view() -> None:
    df: pd.DataFrame = pd.read_sql(sql=sa.text("SELECT * FROM megasena"), con=engine)

    df["concurso"] = df["concurso"].astype(str).str.zfill(4)
    df["data"] = pd.to_datetime(df["data"]).dt.strftime("%x (%a)")
    df["ganhou"] = np.where(df["ganhou"], "Sim", "Não")
    df.columns = ["Concurso", "Data", "Bolas", "Ganhou?"]

    print(df.tail(25))


if __name__ == "__main__":
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("-" * 50)
        print(" 1 - Criar Nova Tabela...")
        print(" 2 - Adicionar Novas Apostas...")
        print(" 3 - Visualizar 25 Últimas Apostas...")
        print("-" * 50)

        option: str = input("Escolha a opção acima (ou tecla ENTER para sair) → ")

        match option:
            case "1": create()
            case "2": add()
            case "3": view()
            case _: break
