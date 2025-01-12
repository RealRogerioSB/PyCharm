import os

import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv

load_dotenv()

engine = sa.create_engine(os.getenv("URL_AIVEN"))

df_new = [
    # {"id_curso": 201034, "hr_curso": 8, "nm_curso": "Swagger parte 1: crie uma documentação APIs REST"},
    # {"id_curso": 201062, "hr_curso": 15, "nm_curso": "Swagger parte 2: customizando uma API gerada"},
    # {"id_curso": 203945, "hr_curso": 6, "nm_curso": "Engenharia de Prompt: criando prompts eficazes para IA Generativa"},
]

exp = pd.DataFrame(df_new).to_sql(name="unibb", con=engine, if_exists="append", index=False)

print(f"Exportou(aram) {exp} curso(s) para a tabela da AIVEN.")
