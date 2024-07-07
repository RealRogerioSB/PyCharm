from dotenv import load_dotenv
import os
import pandas as pd
import sqlalchemy as sa
import time

load_dotenv()

engine = sa.engine.create_engine(os.getenv("URL_MYSQL"))


def create():
    stmt = """
        CREATE TABLE IF NOT EXISTS unibb (
            id_curso MEDIUMINT PRIMARY KEY,
            nm_curso VARCHAR(100) NOT NULL,
            hr_curso TINYINT UNSIGNED NOT NULL
        )
    """
    with engine.begin() as cnx:
        cnx.execute(sa.text(stmt))
    print("Tabela criada com sucesso.")


def add():
    cursos = [
        {"id_curso": 0, "nm_curso": "", "hr_curso": 0},
    ]
    df_new = pd.DataFrame(cursos)
    rows_inserted = df_new.to_sql(name="unibb", con=engine, if_exists="append", index=False)
    print(f"Foram {rows_inserted} cursos inseridos com sucesso.")


def view():
    print(pd.read_sql(sql="SELECT id_curso AS Código, nm_curso AS Curso, hr_curso AS Hora FROM unibb ORDER BY id_curso",
                      con=engine))


if __name__ == "__main__":
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("-" * 50)
        print(" 1 - Criar Nova Tabela...")
        print(" 2 - Adicionar Novos Registros...")
        print(" 3 - Visualizar Registros Selecionados...")
        print("-" * 50)
        option = input("Escolha a opção acima (ou tecla ENTER para sair) → ")
        match option:
            case "1": create()
            case "2": add()
            case "3": view()
            case _: break
        time.sleep(1.5)
