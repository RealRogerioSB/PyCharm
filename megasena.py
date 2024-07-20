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

minhas_apostas: tuple = (
    "05 15 26 27 46 53",  # aposta n.° 1
    "03 12 19 20 45 47",  # aposta n.° 2
    "01 10 17 41 42 56",  # aposta n.° 3
    "02 10 13 27 53 55",  # aposta n.° 4
    "06 07 08 11 43 56",  # aposta n.° 5
    "08 10 14 25 33 34",  # aposta n.° 6
    "05 11 16 40 43 57",  # aposta n.° 7
    "04 05 08 13 17 38",  # aposta n.° 8
    "13 24 32 49 51 60",  # aposta n.° 9
    "11 16 19 43 58 60",  # aposta n.° 10
    "03 05 10 20 35 46",  # aposta n.° 11
    "02 09 10 19 31 57",  # aposta n.° 12
    "04 18 20 21 39 57",  # aposta n.° 13
    "02 11 22 36 49 60",  # aposta n.° 14
    "02 21 39 48 52 57",  # aposta n.° 15
    "14 41 45 50 54 59",  # aposta n.° 16
    "13 20 22 25 28 39",  # aposta n.° 17
    "01 16 21 34 49 54",  # aposta n.° 18
)


def create() -> None:
    stmt: str = """
        CREATE TABLE IF NOT EXISTS megasena (
            concurso MEDIUMINT UNSIGNED NOT NULL,
            data DATE NOT NULL,
            bolas VARCHAR(17) NOT NULL,
            ganhou BOOLEAN NOT NULL DEFAULT FALSE,
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
    new: list[dict[str: int | str | bool]] = [
        {"concurso": 2743, "data": "2024-06-29", "bolas": "13 25 27 30 37 53", "ganhou": False},
    ]
    rows_inserted: int = pd.DataFrame(new).to_sql(name="megasena", con=engine, if_exists="append", index=False)
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
        print(" 2 - Incluir Novos Jogos...")
        print(" 3 - Exibir 25 Últimos Jogos...")
        print("-" * 50)

        option: str = input("Escolha a opção acima (ou tecla ENTER para sair) → ")

        match option:
            case "1": create()
            case "2": add()
            case "3": view()
            case _: break
