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
    print("Tabela criada com sucesso.")


def add() -> None:
    cursos: list[dict[str: int | str]] = [
        # {"id_curso": 0, "nm_curso": "", "hr_curso": 0},
    ]
    df_new: pd.DataFrame = pd.DataFrame(cursos)
    rows_inserted: int = df_new.to_sql(name="unibb", con=engine, if_exists="append", index=False)
    print(f"Foram {rows_inserted} cursos inseridos com sucesso.")


def view_unsorted() -> None:
    stmt: str = "SELECT id_curso AS Código, nm_curso AS Curso, hr_curso AS Horas FROM unibb"
    print(pd.read_sql(sql=sa.text(stmt), con=engine))


def view_sorted() -> None:
    stmt: str = "SELECT id_curso AS Código, nm_curso AS Curso, hr_curso AS Horas FROM unibb ORDER BY id_curso"
    print(pd.read_sql(sql=sa.text(stmt), con=engine))


if __name__ == "__main__":
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("-" * 50)
        print(" 1 - Criar Nova Tabela...")
        print(" 2 - Incluir Novos Cursos...")
        print(" 3 - Exibir Cursos Não Ordenados...")
        print(" 4 - Exibir Cursos Ordenados...")
        print("-" * 50)

        option: str = input("Escolha a opção acima (ou tecla ENTER para sair) → ")

        match option:
            case "1": create()
            case "2": add()
            case "3": view_unsorted()
            case "4": view_sorted()
            case _: break

        time.sleep(1.5)
