import os

import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv

load_dotenv()

engine = sa.create_engine(os.getenv("URL_AIVEN"))

df_new = [
    {"id_curso": 201694, "nm_curso": "Criação de valor: conhecendo os conceitos-chave para gerenciamento de serviços", "hr_curso": 8},
    {"id_curso": 201696, "nm_curso": "Cadeia de valor de serviços: conhecendo as 4 dimensões", "hr_curso": 6},
    {"id_curso": 202525, "nm_curso": "Estratégia Omnichannel: aumentando suas vendas", "hr_curso": 8},
    {"id_curso": 203168, "nm_curso": "Gestão Ágil: explorando conceitos da agilidade", "hr_curso": 8},
    {"id_curso": 203862, "nm_curso": "Aprendizado contínuo: desenvolvendo o perfil de lifelong learner", "hr_curso": 8},
    {"id_curso": 203945, "nm_curso": "Engenharia de Prompt: criando prompts eficazes para IA Generativa", "hr_curso": 6},
    {"id_curso": 204094, "nm_curso": "Segurança Psicológica: lidere e construa ambientes de confiança e inovação", "hr_curso": 10},
]

exp = pd.DataFrame(df_new).to_sql(name="unibb", con=engine, if_exists="append", index=False)

print(f"Exportou {exp} cursos para a tabela AIVEN")
