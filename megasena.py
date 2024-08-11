import locale
import os

from dotenv import load_dotenv
import numpy as np
import pandas as pd
import sqlalchemy as sa
# import streamlit as st

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

pd.set_option("display.float_format", lambda x: f"R$ {locale.currency(val=x, symbol=False, grouping=True)}")
pd.set_option("display.max_columns", None)

load_dotenv()

engine: sa.Engine = sa.create_engine(os.getenv("URL_MYSQL"))

# st.set_page_config(page_title="Mega-sena")

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
    df: pd.DataFrame = pd.read_excel("~/Downloads/Mega-Sena.xlsx")
    df["Data do Sorteio"] = pd.to_datetime(df["Data do Sorteio"], format="%d/%m/%Y")
    for col in df.columns[2:8]:
        df[col] = df[col].astype(str).str.zfill(2)
    df["bolas"] = df[df.columns[2:8]].apply(" ".join, axis=1)
    for col in ["Rateio 6 acertos", "Rateio 5 acertos", "Rateio 4 acertos"]:
        df[col] = df[col].astype(str).str.replace(r"\D", "", regex=True).astype(float) / 100
    df = df[["Concurso", "Data do Sorteio", "bolas", "Ganhadores 6 acertos", "Rateio 6 acertos",
             "Ganhadores 5 acertos", "Rateio 5 acertos", "Ganhadores 4 acertos", "Rateio 4 acertos"]]
    df.columns = ["concurso", "data", "bolas", "acerto_6", "rateio_6", "acerto_5", "rateio_5", "acerto_4", "rateio_4"]
    row_inserted: int = df.to_sql(name="megasena", con=engine, if_exists="replace", index=False)
    print(f"Foram {row_inserted} jogos inseridos com sucesso.")


def columns(table: pd.DataFrame) -> pd.DataFrame:
    table["concurso"] = table["concurso"].astype(str).str.zfill(4)
    table["data"] = pd.to_datetime(table["data"]).dt.strftime("%x (%a)")
    table["acerto_6"] = np.where(table["acerto_6"].ne(0), table["acerto_6"].astype(str), "Ninguém")
    table["acerto_5"] = np.where(table["acerto_5"].ne(0), table["acerto_5"].astype(str), "Ninguém")
    table["acerto_4"] = np.where(table["acerto_4"].ne(0), table["acerto_4"].astype(str), "Ninguém")
    table.columns = ["Concurso", "Data", "Bolas", "Acerto para 6", "Rateio para 6", "Acerto para 5",
                     "Rateio para 5", "Acerto para 4", "Rateio para 4"]
    return table


def view() -> None:
    print(columns(pd.read_sql(sql=sa.text("SELECT * FROM megasena"), con=engine)).tail(25))


def mega_da_virada() -> None:
    stmt: str = """
        SELECT * FROM megasena WHERE data IN (
            SELECT MAX(data) FROM megasena GROUP BY YEAR(data) HAVING YEAR(data) <> YEAR(CURRENT_DATE)
        )
    """
    print(columns(pd.read_sql(sql=sa.text(stmt), con=engine)))


def acertei_minhas_apostas() -> None:
    for r in range(6, 3, -1):
        mega: dict[str: list] = {"Concurso": [], "Data": [], "Bolas": [], "Aposta n.°": []}

        stmt: str = f"SELECT concurso, data, bolas, acerto_{r}, rateio_{r} FROM megasena"

        for row in pd.read_sql(sql=sa.text(stmt), con=engine).itertuples(index=False, name=None):
            for aposta in minhas_apostas:
                bolas: list[str] = aposta.split()
                match: list[str] = []

                for x in range(6):
                    if bolas[x] in row[2]:
                        match.append(bolas[x])

                if len(match) == r:
                    mega["Concurso"].append(str(row[0]).zfill(4))
                    mega["Data"].append(pd.to_datetime(row[1]).strftime("%x (%a)"))
                    mega["Bolas"].append(" ".join(match))
                    mega["Aposta n.°"].append(minhas_apostas.index(aposta) + 1)

        print(f"\nLista de {r} acertos:")
        print(pd.DataFrame(mega)) if len(pd.DataFrame(mega)) != 0 else print("Suas apostas não tiveram acertos...")


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

    print(pd.DataFrame(mega)) if len(pd.DataFrame(mega)) != 0 else print("Sua aposta não teve acertos...\n")


def quantas_bolas_acertas() -> None:
    apostas: dict[int: int] = {}

    for x in minhas_apostas:
        y: list[str] = x.split()
        for z in range(len(y)):
            try:
                apostas[int(y[z])] += 1
            except KeyError:
                apostas[int(y[z])] = 1

    apostas_ordenadas: dict[int: int] = {k: v for k, v in sorted(apostas.items(), key=lambda s: s[0])}

    acertos: pd.DataFrame = pd.DataFrame(data=apostas_ordenadas, index=["acertos"])
    acertos.index.name = "bolas"
    print(acertos)


if __name__ == "__main__":
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("-" * 80)
        print(" 1 - Criar Nova Tabela...")
        print(" 2 - Incluir Novos Jogos...")
        print(" 3 - Exibir 25 Últimos Jogos...")
        print(" 4 - Exibir Os Jogos da Mega Da Virada...")
        print(" 5 - Ver Se Acertei Minhas Apostas...")
        print(" 6 - Ver Se Acertou Sua Aposta...")
        print(" 7 - Ver Quantas Bolas Acertas...")
        print("-" * 80)

        option: str = input("Escolha a opção acima (ou tecla ENTER para sair) → ")

        match option:
            case "1":
                create()
            case "2":
                add()
            case "3":
                view()
            case "4":
                mega_da_virada()
            case "5":
                acertei_minhas_apostas()
            case "6":
                acertou_sua_aposta()
            case "7":
                quantas_bolas_acertas()
            case _:
                break
