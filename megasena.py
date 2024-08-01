import locale
import os

from dotenv import load_dotenv
import numpy as np
import pandas as pd
import sqlalchemy as sa

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

pd.set_option("display.float_format", lambda x: locale.currency(val=x, grouping=True))
pd.set_option("display.max_columns", None)

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
            concurso SMALLINT UNSIGNED NOT NULL,
            data DATE NOT NULL,
            bolas VARCHAR(17) NOT NULL,
            acerto_6 MEDIUMINT UNSIGNED NOT NULL,
            rateio_6 DOUBLE NOT NULL,
            acerto_5 MEDIUMINT UNSIGNED NOT NULL,
            rateio_5 DOUBLE NOT NULL,
            acerto_4 MEDIUMINT UNSIGNED NOT NULL,
            rateio_4 DOUBLE NOT NULL,
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
    df_new: pd.DataFrame = pd.read_csv("../src/megasena.csv", encoding="utf-8-sig")
    row_inserted: int = df_new.to_sql(name="megasena", con=engine, if_exists="append", index=False)
    print(f"Foi(ram) {row_inserted} jogo(s) inserido(s) com sucesso.")


def columns(table: pd.DataFrame) -> pd.DataFrame:
    table["concurso"] = table["concurso"].astype(str).str.zfill(4)
    table["data"] = pd.to_datetime(table["data"]).dt.strftime("%x (%a)")
    table["acerto_6"] = np.where(table["acerto_6"].ne(0), table["acerto_6"].astype(str), "Ninguém")
    table["acerto_5"] = np.where(table["acerto_5"].ne(0), table["acerto_5"].astype(str), "Ninguém")
    table["acerto_4"] = np.where(table["acerto_4"].ne(0), table["acerto_4"].astype(str), "Ninguém")
    table.columns = ["Concurso", "Data", "Bolas", "Acerto para 6", "Rateio para 6", "Acerto para 5",
                     "Rateio para 5", "Acerto para 4", "Rateio para 4", ]
    return table


def view() -> None:
    df: pd.DataFrame = columns(pd.read_sql(sql=sa.text("SELECT * FROM megasena"), con=engine))
    print(df.tail(25))


def mega_da_virada() -> None:
    stmt: str = """
        SELECT
            concurso AS Concurso,
            data AS Data,
            bolas AS Bolas,
            CASE acerto_6
                WHEN 0 THEN 'Ninguém acertou...'
                WHEN 1 THEN 'Só 1 acertou...'
                ELSE CONCAT('Só ', acerto_6, ' acertaram...')
            END AS 'Acertou?',
            rateio_6 AS Rateio
        FROM
            megasena
        WHERE
            data IN (
                SELECT MAX(data)
                FROM megasena
                GROUP BY YEAR(data)
                HAVING YEAR(data) <> YEAR(CURRENT_DATE)
            )
    """

    df_mega_da_virada: pd.DataFrame = pd.read_sql(sql=sa.text(stmt), con=engine)
    df_mega_da_virada["Concurso"] = df_mega_da_virada["Concurso"].astype(str).str.zfill(4)
    df_mega_da_virada["Data"] = pd.to_datetime(df_mega_da_virada["Data"]).dt.strftime("%x (%a)")
    print(df_mega_da_virada)


def acertei_minhas_apostas() -> None:
    mega: dict[str: list] = {"Concurso": [], "Data": [], "Bolas": [], "Aposta n.°": [], "Acertos": [], "Rateio": []}

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
                mega["Rateio"].append(row[4])

    print(pd.DataFrame(mega)) if len(pd.DataFrame(mega)) != 0 else print("Suas apostas não tiveram acertos...\n")


def acertou_sua_aposta() -> None:
    sua_aposta: str = input("Sua aposta: ")

    mega: dict[str: list] = {"Concurso": [], "Data": [], "Bolas": [], "Acertos": [], "Rateio": []}

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
            mega["Rateio"].append(row[4])

    print(pd.DataFrame(mega)) if len(pd.DataFrame(mega)) != 0 else print("Sua aposta não teve acertos...\n")


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
