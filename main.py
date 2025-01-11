import os

import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv

load_dotenv()

engine = sa.create_engine(os.getenv("URL_AIVEN"))

df_new = [
    {"id_curso": 202405, "nm_curso": "Flask: crie uma webapp com Python", "hr_curso": 10},
    {"id_curso": 202471, "nm_curso": "Flask: avançando no desenvolvimento web com Python", "hr_curso": 10},
    {"id_curso": 202530, "nm_curso": "Git e GitHub: repositório, commit e versões", "hr_curso": 8},
    {"id_curso": 201034, "nm_curso": "Swagger parte 1: crie uma documentação APIs REST", "hr_curso": 8},
    {"id_curso": 201062, "nm_curso": "Swagger parte 2: customizando uma API gerada", "hr_curso": 15},
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
