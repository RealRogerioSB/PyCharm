import os

import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv

load_dotenv()

engine = sa.create_engine(os.getenv("URL_AIVEN"))

df_new = [
    {"id_curso": 202530, "hr_curso": 8, "nm_curso": "Git e GitHub: repositório, commit e versões"},
    {"id_curso": 201034, "hr_curso": 8, "nm_curso": "Swagger parte 1: crie uma documentação APIs REST"},
    {"id_curso": 201062, "hr_curso": 15, "nm_curso": "Swagger parte 2: customizando uma API gerada"},
    {"id_curso": 201694, "hr_curso": 8, "nm_curso": "Criação de valor: conhecendo os conceitos-chave para gerenciamento de serviços"},
    {"id_curso": 201696, "hr_curso": 6, "nm_curso": "Cadeia de valor de serviços: conhecendo as 4 dimensões"},
    {"id_curso": 202525, "hr_curso": 8, "nm_curso": "Estratégia Omnichannel: aumentando suas vendas"},
    {"id_curso": 203168, "hr_curso": 8, "nm_curso": "Gestão Ágil: explorando conceitos da agilidade"},
    {"id_curso": 203862, "hr_curso": 8, "nm_curso": "Aprendizado contínuo: desenvolvendo o perfil de lifelong learner"},
    {"id_curso": 203945, "hr_curso": 6, "nm_curso": "Engenharia de Prompt: criando prompts eficazes para IA Generativa"},
    {"id_curso": 204094, "hr_curso": 10, "nm_curso": "Segurança Psicológica: lidere e construa ambientes de confiança e inovação"},
]

exp = pd.DataFrame(df_new).to_sql(name="unibb", con=engine, if_exists="append", index=False)

print(f"Exportou {exp} cursos para a tabela AIVEN")
