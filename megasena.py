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
        # {"concurso": 2751, "data": "2024-07-20", "bolas": "04 13 18 42 52 53", "ganhou": False},
    ]
    rows_inserted: int = pd.DataFrame(new).to_sql(name="megasena", con=engine, if_exists="append", index=False)
    print(f"Foi(ram) {rows_inserted} jogo(s) inserido(s) com sucesso.")


def view() -> None:
    df: pd.DataFrame = pd.read_sql(sql=sa.text("SELECT * FROM megasena"), con=engine)
    df["concurso"] = df["concurso"].astype(str).str.zfill(4)
    df["data"] = pd.to_datetime(df["data"]).dt.strftime("%x (%a)")
    df["ganhou"] = np.where(df["ganhou"], "Sim", "Não")
    df.columns = ["Concurso", "Data", "Bolas", "Ganhou?"]
    print(df.tail(25))


def mega_da_virada() -> None:
    stmt: str = ("SELECT * FROM megasena WHERE data IN (SELECT MAX(data) FROM "
                 "megasena GROUP BY YEAR(data) HAVING YEAR(data) <> YEAR(CURRENT_DATE))")

    df_mega_da_virada: pd.DataFrame = pd.read_sql(sql=sa.text(stmt), con=engine)
    df_mega_da_virada["concurso"] = df_mega_da_virada["concurso"].astype(str).str.zfill(4)
    df_mega_da_virada["data"] = pd.to_datetime(df_mega_da_virada["data"]).dt.strftime("%x (%a)")
    df_mega_da_virada["ganhou"] = np.where(df_mega_da_virada["ganhou"], "Alguém ganhou", "Ninguém ganhou")
    df_mega_da_virada.columns = ["Concurso", "Data", "Bolas", "Ganhou?"]
    print(df_mega_da_virada)


def acertei_minhas_apostas() -> None:
    mega: dict[str: list] = {"Concurso": [], "Data": [], "Bolas": [], "Aposta n.°": [], "Acertos": []}

    for row in pd.read_sql(sql=sa.text("SELECT * FROM megasena"), con=engine).itertuples(index=False, name=None):
        for aposta in minhas_apostas:
            bolas: list[str] = aposta.split()
            match: list[str] = []
            for x in range(6):
                if bolas[x] in row[2]:
                    match.append(bolas[x])
            if len(match) >= 4:
                mega["Concurso"].append(str(row[0]).zfill(4))
                mega["Data"].append(pd.to_datetime(row[1]).strftime("%x (%a)"))
                mega["Bolas"].append(" ".join(match))
                mega["Aposta n.°"].append(minhas_apostas.index(aposta) + 1)
                mega["Acertos"].append(len(match))

    print(pd.DataFrame(mega)) if len(pd.DataFrame(mega)) != 0 else print("Não houve nenhum acerto...\n")


def acertou_sua_aposta() -> None:
    sua_aposta: str = input("Sua aposta: ")

    mega: dict[str: list] = {"Concurso": [], "Data": [], "Bolas": [], "Acertos": []}

    for row in pd.read_sql(sql=sa.text("SELECT * FROM megasena"), con=engine).itertuples(index=False, name=None):
        match: list[str] = []
        for aposta in sua_aposta.split():
            if aposta in row[2]:
                match.append(aposta)
        if len(match) >= 4:
            mega["Concurso"].append(str(row[0]).zfill(4))
            mega["Data"].append(pd.to_datetime(row[1]).strftime("%x (%a)"))
            mega["Bolas"].append(row[2])
            mega["Acertos"].append(len(match))

    print(pd.DataFrame(mega)) if len(pd.DataFrame(mega)) != 0 else print("Não acertou nada da sua aposta...\n")


if __name__ == "__main__":
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("-" * 50)
        print(" 1 - Criar Nova Tabela...")
        print(" 2 - Incluir Novos Jogos...")
        print(" 3 - Exibir 25 Últimos Jogos...")
        print(" 4 - Exibir Os Jogos da Mega Da Virada...")
        print(" 5 - Ver Se Acertei Minhas Apostas...")
        print(" 6 - Ver Se Acertou Sua Aposta...")
        print("-" * 50)

        option: str = input("Escolha a opção acima (ou tecla ENTER para sair) → ")

        match option:
            case "1": create()
            case "2": add()
            case "3": view()
            case "4": mega_da_virada()
            case "5": acertei_minhas_apostas()
            case "6": acertou_sua_aposta()
            case _: break
