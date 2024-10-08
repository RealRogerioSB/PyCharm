from datetime import datetime
import locale
import os
import time

from dotenv import load_dotenv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sqlalchemy as sa

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

pd.set_option("display.float_format", lambda x: locale.currency(val=x, symbol=False, grouping=True))

load_dotenv()

engine: sa.Engine = sa.create_engine(os.getenv("URL_MYSQL"))

sqls: list[str] = [
    """
        CREATE TABLE IF NOT EXISTS lançamento (
            id_lançamento TINYINT AUTO_INCREMENT PRIMARY KEY,
            lançamento VARCHAR(60) NOT NULL
        )
    """,
    """
        CREATE TABLE IF NOT EXISTS espelho (
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            id_lançamento TINYINT NOT NULL,
            período MEDIUMINT NOT NULL,
            acerto BOOLEAN NOT NULL DEFAULT FALSE,
            valor DOUBLE NOT NULL
        )
    """,
    """
        SELECT id_lançamento AS Código, lançamento AS Lançamento FROM lançamento
    """,
    """
        SELECT id_lançamento AS Código, período AS Período, acerto AS Acerto, valor AS Valor FROM espelho
    """,
    """
        SELECT y.lançamento AS Lançamento, x.período AS Período, IF(x.acerto = 1, 'A', 'M') AS Acerto, x.valor AS Valor
        FROM espelho x LEFT JOIN lançamento y ON x.id_lançamento = y.id_lançamento
        WHERE x.período = YEAR(CURRENT_DATE()) * 100 + MONTH(CURRENT_DATE())
    """,
    """
        SELECT SUM(valor) AS Total FROM espelho WHERE período = YEAR(CURRENT_DATE()) * 100 + MONTH(CURRENT_DATE())
    """,
    """
        SELECT período AS Período, SUM(valor) AS Total
        FROM espelho
        WHERE SUBSTR(período, 1, 4) = YEAR(CURRENT_DATE())
        GROUP BY período
    """
]


def create(stmt: str) -> None:
    with engine.begin() as cnx:
        cnx.execute(sa.text(stmt))
    print("Tabela criada com sucesso!")


def add() -> None:
    df_new: pd.DataFrame = pd.read_csv("./src/espelho.csv", sep=",", encoding="utf-8-sig")
    row_inserted: int = df_new.to_sql(name="espelho", con=engine, if_exists="append", index=False)
    print(f"Foram {row_inserted} lançamentos inseridos com sucesso.")


def view(stmt: str) -> None:
    print(pd.read_sql(sql=sa.text(stmt), con=engine))


def visualizar() -> None:
    year: int = int(input("Em que ano quer visualizar o gráfico (a partir de 2005)? "))
    if 2005 <= year <= datetime.now().year:
        stmt: str = f"""
            SELECT
                SUBSTR(período, 1, 4) AS ano,
                CONCAT('mês ', SUBSTR(período, 5)) AS mes,
                SUM(valor) AS valor
            FROM
                espelho
            GROUP BY
                ano,
                mes
        """
        df_anual: pd.DataFrame = pd.read_sql(sql=sa.text(stmt), con=engine)
        df_anual = df_anual.pivot(columns=["mes"], index=["ano"], values=["valor"])
        df_anual.columns = df_anual.columns.droplevel(level=0)
        df_anual.reset_index(inplace=True)
        df_anual["ano"] = df_anual["ano"].astype(int)
        df_anual.set_index(["ano"], inplace=True)
        df_anual.fillna(0, inplace=True)
        df_anual["média"] = df_anual.mean(axis=1)
        df_anual["total"] = df_anual[df_anual.columns[:-1]].sum(axis=1)
        df_anual.columns = ["jan", "fev", "mar", "abr", "mai", "jun", "jul",
                            "ago", "set", "out", "nov", "dez", "média", "total"]

        plt.figure(figsize=(16, 4))
        plt.style.use("ggplot")

        ax: plt.Axes = sns.barplot(data=df_anual.loc[[year], df_anual.columns[:-2]])
        ax.set_title(f"Espelho {year}", loc="center", fontweight="bold", fontsize=12)
        ax.set(xlabel="", ylabel="", yticks=[])

        for mes in range(12):
            ax.bar_label(
                ax.containers[mes],
                fmt=lambda i: locale.currency(val=i, symbol=False, grouping=True),
                fontsize=10
            )

        plt.show()
    else:
        print(f"Não consta o contracheque do ano {year}.")


if __name__ == '__main__':
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("-" * 50)
        print(" 1 - CREATE")
        print(" 2 - CREATE")
        print(" 3 - ADD")
        print(" 4 - VIEW")
        print(" 5 - VIEW")
        print(" 6 - VIEW")
        print(" 7 - VIEW")
        print(" 8 - VIEW")
        print("-" * 50)

        option: str = input("Escolha a opção acima (ou tecla ENTER para sair) → ")

        match option:
            case "1": create(stmt=sqls[0])
            case "2": create(stmt=sqls[1])
            case "3": add()
            case "4": view(stmt=sqls[2])
            case "5": view(stmt=sqls[3])
            case "6": view(stmt=sqls[4])
            case "7": view(stmt=sqls[5])
            case "8": view(stmt=sqls[6])
            case "v": visualizar()
            case _: break

        time.sleep(2.5)
