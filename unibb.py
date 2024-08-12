import os
import time

from dotenv import load_dotenv
import pandas as pd
import sqlalchemy as sa

load_dotenv()

engine: sa.Engine = sa.engine.create_engine(os.getenv("URL_MYSQL"))


def create() -> None:
    stmt: str = """
        CREATE TABLE IF NOT EXISTS unibb (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_curso INT NOT NULL,
            nm_curso VARCHAR(100) NOT NULL,
            hr_curso TINYINT UNSIGNED NOT NULL
        )
    """
    with engine.begin() as cnx:
        cnx.execute(sa.text(stmt))
    print("Tabela criada com sucesso.\n")


def add() -> None:
    try:
        df_new: pd.DataFrame = pd.read_csv("./src/unibb.csv", sep=",", encoding="utf-8-sig")
        df_new = df_new[df_new["save"].eq(1)]
        df_new = df_new[["id_curso", "nm_curso", "hr_curso"]]
        rows_inserted: int = df_new.to_sql(name="unibb", con=engine, if_exists="append", index=False)
        print(f"Foram {rows_inserted} cursos inseridos com sucesso.")
    except FileNotFoundError:
        print("Erro ao localizar o arquivo .CSV...")
    except UnicodeEncodeError:
        print("Erro ao decodificar o arquivo .CSV...")
    else:
        df_deleted: pd.DataFrame = pd.read_csv("./src/unibb.csv", sep=",", encoding="utf-8-sig")
        df_deleted[df_deleted["save"].ne(1)].to_csv("./src/unibb.csv", index=False, sep=",", encoding="utf-8-sig")
        print("Cursos atualizados com sucesso.\n")


def view_unsorted() -> None:
    stmt: str = "SELECT id_curso AS Código, nm_curso AS Curso, hr_curso AS Horas FROM unibb ORDER BY id"
    print(pd.read_sql(sql=sa.text(stmt), con=engine))


def view_sorted() -> None:
    stmt: str = "SELECT id_curso AS Código, nm_curso AS Curso, hr_curso AS Horas FROM unibb ORDER BY id_curso"
    print(pd.read_sql(sql=sa.text(stmt), con=engine))


def duplicate_courses() -> None:
    stmt: str = """
        SELECT id_curso AS Código, nm_curso AS Curso, hr_curso AS Horas FROM unibb WHERE nm_curso IN (
            SELECT nm_curso FROM unibb GROUP BY nm_curso HAVING COUNT(nm_curso) > 1
        ) ORDER BY nm_curso, id_curso
    """
    print(pd.read_sql(sql=sa.text(stmt), con=engine))


if __name__ == "__main__":
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("-" * 80)
        print(" 1 - Criar Nova Tabela...")
        print(" 2 - Incluir Novos Cursos...")
        print(" 3 - Exibir Cursos Não Ordenados...")
        print(" 4 - Exibir Cursos Ordenados...")
        print(" 5 - Exibir Cursos Duplicados...")
        print("-" * 80)

        option: str = input("\nEscolha a opção acima (ou tecla ENTER para sair) → ")

        match option:
            case "1": create()
            case "2": add()
            case "3": view_unsorted()
            case "4": view_sorted()
            case "5": duplicate_courses()
            case _: break

        time.sleep(1.5)
