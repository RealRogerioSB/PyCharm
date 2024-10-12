#%%
from datetime import datetime
import locale
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sqlalchemy as sa

load_dotenv()

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

pd.set_option("display.float_format", lambda val: locale.currency(val=val, symbol=False, grouping=True))

engine: sa.Engine = sa.engine.create_engine(os.getenv("URL_MYSQL"))

#%%
stmt: str = """
    CREATE TABLE IF NOT EXISTS lançamento (
        id_lançamento TINYINT AUTO_INCREMENT PRIMARY KEY,
        lançamento VARCHAR(60) NOT NULL
    )
"""

with engine.begin() as cnx:
    cnx.execute(sa.text(stmt))

print("Tabela 'lançamento' criada com sucesso!")

#%%
# exibir a tabela lançamento
print(pd.read_sql(sql=sa.text("SELECT id_lançamento AS Código, lançamento AS Lançamento FROM lançamento"), con=engine))

#%%
stmt: str = """
    CREATE TABLE IF NOT EXISTS espelho (
        id INTEGER AUTO_INCREMENT PRIMARY KEY,
        id_lançamento TINYINT NOT NULL,
        período MEDIUMINT NOT NULL,
        acerto BOOLEAN NOT NULL DEFAULT FALSE,
        valor DOUBLE NOT NULL
    )
"""

with engine.begin() as cnx:
    cnx.execute(sa.text(stmt))

print("Tabela 'espelho' criada com sucesso!")

#%%
# inserir novos registros para a tabela espelho
df_new: pd.DataFrame = pd.read_csv("./src/espelho.csv", sep=",", encoding="utf-8-sig")
row_inserted: int = df_new.to_sql(name="espelho", con=engine, if_exists="append", index=False)

print(f"Foram {row_inserted} lançamentos inseridos com sucesso.")

#%%
# exibir a tabela espelho do mês atual
stmt: str = """
    SELECT y.lançamento AS Lançamento, x.período AS Período, IF(x.acerto = 1, 'Acerto', 'Mês') AS Acerto, x.valor AS Valor
    FROM espelho x LEFT JOIN lançamento y ON x.id_lançamento = y.id_lançamento
    WHERE x.período = YEAR(CURRENT_DATE()) * 100 + MONTH(CURRENT_DATE())
    ORDER BY Acerto, Valor DESC
"""

print(pd.read_sql(sql=sa.text(stmt), con=engine))

#%%
# exibir os períodos com seus valores totais do ano anual
stmt: str = """
    SELECT período AS Período, SUM(valor) AS Total
    FROM espelho
    WHERE SUBSTR(período, 1, 4) = YEAR(CURRENT_DATE())
    GROUP BY período
"""

print(pd.read_sql(sql=sa.text(stmt), con=engine))

#%%
# exibir a tabela espelho para o mês atual
period: int = datetime.now().year*100 + datetime.now().month

stmt: str = f"""
    SELECT
        l.lançamento,
        e.período,
        IF(e.acerto, 'acerto', 'mês') AS espelho,
        e.valor
    FROM
        espelho e
        INNER JOIN lançamento l ON e.id_lançamento = l.id_lançamento
    WHERE
        e.período = {period}
    ORDER BY
        e.acerto DESC
"""

df_mes: pd.DataFrame = pd.read_sql(sql=sa.text(stmt), con=engine)
df_mes["período"] = pd.to_datetime(df_mes["período"], format="%Y%m").dt.strftime("%B de %Y")

print(df_mes)

#%%
# exibir o gráfico do total de mês a mês para o ano atual
year: int = datetime.now().year

stmt: str = f"""
    SELECT
        l.lançamento,
        e.período,
        IF(e.acerto = 1, 'acerto', 'mês') AS acerto,
        e.valor
    FROM
        espelho e
        INNER JOIN lançamento l ON e.id_lançamento = l.id_lançamento
    WHERE
        e.período LIKE '{year}%'
"""

df_ano: pd.DataFrame = pd.read_sql(sql=sa.text(stmt), con=engine)
df_ano = df_ano.pivot(values=["valor"], index=["lançamento", "acerto"], columns=["período"])
df_ano.columns = df_ano.columns.droplevel(level=0)
df_ano.reset_index(inplace=True)
df_ano.fillna(value=0, inplace=True)
df_ano.sort_values(["acerto"], inplace=True, ignore_index=True)
df_ano.columns.rename("", inplace=True)
df_ano["média"] = df_ano.mean(axis=1, numeric_only=True)
df_ano["total"] = df_ano[df_ano.columns[:-1]].sum(axis=1, numeric_only=True)
df_ano.loc["sumário"] = df_ano.sum(numeric_only=True)
df_ano.fillna(value="", inplace=True)
df_ano.iloc[-1, 0] = "Sumário"
df_ano.iloc[-1, 1] = "----------"
df_ano.set_index(["lançamento", "acerto"], inplace=True)
df_ano.rename(columns={
    year*100 + 1: "jan", year*100 + 2: "fev", year*100 + 3: "mar", year*100 + 4: "abr",
    year*100 + 5: "mai", year*100 + 6: "jun", year*100 + 7: "jul", year*100 + 8: "ago",
    year*100 + 9: "set", year*100 + 10: "out", year*100 + 11: "nov", year*100 + 12: "dez",
}, inplace=True)

print(df_ano)

#%%
# resumos totais anuais
stmt: str = """
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

df_anuais: pd.DataFrame = pd.read_sql(sql=stmt, con=engine)
df_anuais = df_anuais.pivot(columns=["mes"], index=["ano"], values=["valor"])
df_anuais.columns = df_anuais.columns.droplevel(level=0)
df_anuais.reset_index(inplace=True)
df_anuais["ano"] = df_anuais["ano"].astype(int)
df_anuais.set_index(["ano"], inplace=True)
df_anuais.fillna(0, inplace=True)
df_anuais["média"] = df_anuais.mean(axis=1)
df_anuais["total"] = df_anuais[df_anuais.columns[:-1]].sum(axis=1)
df_anuais.columns = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez", "média", "total"]

print(df_anuais)

#%%
# exibir o gráfico do total de mês a mês para o ano atual
year: int = datetime.now().year

plt.figure(figsize=(16, 6))
plt.style.use("ggplot")

ax: plt.Axes = sns.barplot(data=df_anuais.loc[[year], df_anuais.columns[:-2]])
ax.set_title(f"Espelho {year}", loc="center", fontweight="bold", fontsize=12)
ax.set(xlabel="", ylabel="", yticks=[])

for mes in range(12):
    ax.bar_label(ax.containers[mes], fmt=lambda i: locale.currency(val=i, symbol=False, grouping=True), fontsize=10)

plt.show()

#%%
# exibir o gráfico do total de mês a mês para o ano escolhido
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
    df_anual.columns = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez", "média", "total"]

    plt.figure(figsize=(16, 6))
    plt.style.use("ggplot")

    ax: plt.Axes = sns.barplot(data=df_anual.loc[[year], df_anual.columns[:-2]])
    ax.set_title(f"Espelho {year}", loc="center", fontweight="bold", fontsize=12)
    ax.set(xlabel="", ylabel="", yticks=[])

    for mes in range(12):
        ax.bar_label(ax.containers[mes], fmt=lambda i: locale.currency(val=i, symbol=False, grouping=True), fontsize=10)

    plt.show()
else:
    print(f"Não consta o contracheque do ano {year}.")
