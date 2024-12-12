# %%
import pandas as pd

# %%
df = pd.DataFrame({"nome": ["Rogério"], "salário": ["$8.500,00"]})
print(df)

df["moeda"] = df["salário"].str.replace("(\$\.)", "", regex=True).str.replace(",", ".").astype(float)
print(df)

print(df.info())

# %%
xml_ = pd.read_xml("./src/nfse_08644821002035_41462_41059_3_enviada.xml")

print(xml_)

# %%
from pandas.tseries.offsets import MonthBegin, MonthEnd

dt = pd.Timestamp.now().date()
print("Hoje é         ->", dt.strftime("%d/%m/%Y"))
print("MonthBegin(-1) ->", (dt + MonthBegin(-1)).strftime("%d/%m/%Y"))
print("MonthBegin(0)  ->", (dt + MonthBegin(0)).strftime("%d/%m/%Y"))
print("MonthBegin(1)  ->", (dt + MonthBegin(1)).strftime("%d/%m/%Y"))
print("MonthBegin(2)  ->", (dt + MonthBegin(2)).strftime("%d/%m/%Y"))
print("MonthEnd(-1)   ->", (dt + MonthEnd(-1)).strftime("%d/%m/%Y"))
print("MonthEnd(0)    ->", (dt + MonthEnd(0)).strftime("%d/%m/%Y"))
print("MonthEnd(1)    ->", (dt + MonthEnd(1)).strftime("%d/%m/%Y"))
print("MonthEnd(2)    ->", (dt + MonthEnd(2)).strftime("%d/%m/%Y"))

# %%
caixa = {
    "Informações": ["Loja A - 2000", "Loja B - 5000", "Loja Teste - 300", "Loja Nova - 250", "Loja Bolada - 10000"]
}

df = pd.DataFrame(caixa)
print(df)

df[["Loja", "Faturamento"]] = df["Informações"].str.split(" - ", expand=True)
df["Faturamento"] = df["Faturamento"].astype(float)
print(df)

# %%
df = pd.DataFrame(pd.date_range("2023-01-01", "2023-06-03"), columns=["Data"])

print(df)

print(df[df["Data"].isin(["2023-01-30", "2023-03-15", "2023-03-18"])])

print(df[df["Data"].dt.month.eq(1)])

print(df[df["Data"].dt.year.eq(2022)])

print(df[df["Data"].dt.month.eq(6) & df["Data"].dt.year.eq(2023)])

print(df[df["Data"].dt.month.eq(6) | df["Data"].dt.year.eq(2023)])

print(df[df["Data"].between("2023-03-01", "2023-03-18")])

print(df[df["Data"].dt.day_name().isin(["Saturday", "Monday"])])

print(df[df["Data"] >= pd.to_datetime("today") - pd.DateOffset(months=3)])

# %%
# exibe os nomes de abas
print(pd.ExcelFile("./src/<filename_xlsx>").sheet_names)

# %%
df = pd.DataFrame({"first_name": ["Rogério"], "birth_date": ["1972-01-30 06:30:00"]})
df["birth_date"] = pd.to_datetime(df["birth_date"], format="%Y-%m-%d %H:%M:%S")

df = df.assign(
    only_date=df["birth_date"].dt.date,
    only_time=df["birth_date"].dt.time,
    only_year=df["birth_date"].dt.year,
    only_quarter=df["birth_date"].dt.quarter,
    only_month=df["birth_date"].dt.month,
    only_day=df["birth_date"].dt.day,
    only_hour=df["birth_date"].dt.hour,
    only_minute=df["birth_date"].dt.minute,
    only_second=df["birth_date"].dt.second
)

df["only_year"] = df["only_year"].astype("int16")
df["only_quarter"] = df["only_quarter"].astype("int8")
df["only_month"] = df["only_month"].astype("int8")
df["only_day"] = df["only_day"].astype("int8")
df["only_hour"] = df["only_hour"].astype("int8")
df["only_minute"] = df["only_minute"].astype("int8")
df["only_second"] = df["only_second"].astype("int8")

print(df.info())

print(df)

# %%
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  ["cobra", "viper", "sidewinder"],
                  ["max_speed", "shield"])
df.columns.name = "Espécimes"

print("Exibindo 'df'...")
print(df)

print("Exibindo 'df.loc[viper]'...")
print(df.loc[["viper"]])

print("Exibindo 'df.loc[[viper, sidewinder]]'...")
print(df.loc[["viper", "sidewinder"]])

print("Exibindo 'df.loc[cobra, shield]'...")
print(df.loc[["cobra", "shield"]])

print("Exibindo 'df.loc[cobra:viper, max_speed]'...")
print(df.loc["cobra":"viper", "max_speed"])

print("Exibindo 'df.loc[[False, False, True]]'...")
print(df.loc[[False, False, True]])

print("Exibindo 'df.loc[pd.Series([False, True, False], index=[viper, sidewinder, cobra])]'...")
print(df.loc[[pd.Series([False, True, False], index=["viper", "sidewinder", "cobra"])]])

print("Exibindo 'df.loc[pd.Index([cobra, viper], name=foo)]'...")
print(df.loc[[pd.Index(["cobra", "viper"], name="foo")]])

print("Exibindo 'df.loc[df[shield] > 6]'...")
print(df.loc[df["shield"] > 6])

print("Exibindo 'df.loc[df[shield] > 6, [max_speed]]'...")
print(df.loc[df["shield"] > 6, ["max_speed"]])

print("Exibindo 'df.loc[lambda x: x[shield] == 8]'...")
print(df.loc[lambda xx: xx["shield"] == 8])

# %%
from datetime import datetime, timedelta

start, end = datetime.now().date() - timedelta(days=360), datetime.now().date()

mondays = pd.date_range(start=start, end=end, freq="W-MON")
print(mondays)
print(f"Entre {start:%m/%Y} e {end:%m/%Y} existem {len(mondays)} segundas-feiras.")

hours = pd.date_range(start=start, end=end, freq="h")
print(hours)
print(f"{start:%B de %Y} possui um total de {len(hours) - 1} horas.")

month_ = pd.date_range(start=start.strftime("%Y-%m"), periods=31)
mes_ = pd.DataFrame(month_, columns=["Data"])

mes_["Dia do Ano"] = mes_["Data"].dt.dayofyear
mes_["Ano"] = mes_["Data"].dt.year
mes_["Mês"] = mes_["Data"].dt.month
mes_["Dia"] = mes_["Data"].dt.day
print(mes_)

# %%
import numpy as np

data = {
    "nome": ["Carmem", "Giovana", "Luiza", "Rogério"],
    "idade": [46, 16, 51, 78],
    "sexo": [False, False, False, True]
}

df = pd.DataFrame(data)

print(df.info())

# df["domínio"] = ["membro"] * (len(df) - 1) + ["admin"]
df["domínio"] = np.where(df["nome"].eq("Rogério"), "admin", "membro")

print(df)

# %%
dados = {
    "Nome": ["Rogério Balloussier", "Carmem Balloussier"],
    "Apelido": ["eusouRogerioSB", "CarmemMB"],
    "E-mail": ["rogerioballoussier@icloud.com", "carmemmb@icloud.com"],
    "Celular": ["(61)98358-1972", "(71)98224-5015"],
    "Sexo": [True, False],
    "DtNasc": [datetime(1972, 1, 30), datetime(1977, 10, 19)]
}

df = pd.DataFrame(dados)
print(df.info())
df["Sexo"] = df["Sexo"].map({False: "Feminino", True: "Masculino"})
df["DtNasc"] = df["DtNasc"].dt.strftime("%d/%m/%Y")
print(df)

# %% md
### Analise Financeira Simples
from datetime import date
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import yfinance as yf

yf.pdr_override()

# %%
data = wb.get_data_yahoo("BBAS3.SA", date(2020, 1, 1), date.today())

print(data.tail())

# %%
data["Resultado"] = data["Adj Close"] / data["Adj Close"].shift(1) - 1

print(data["Resultado"])

# %%
data["Resultado"].plot(figsize=(8, 5))
plt.show()

# %%
media_simples = data["Resultado"].mean()
print(media_simples)

# %%
media_anual = data["Resultado"].mean() * 250
print(media_anual)
print(str(round(media_anual, 5) * 100) + "%")

# %%
data["RetLogaritmico"] = np.log(data["Adj Close"] / data["Adj Close"].shift(1))
print(data["RetLogaritmico"])

# %%
data["RetLogaritmico"].plot(figsize=(8, 5))
plt.show()

# %%
media_log = data["RetLogaritmico"].mean() * 250
print(str(round(media_log, 5) * 100) + "%")

# %%
carteiras = ["^BVSP", "AAPL", "AAPL34.SA", "AMZO34.SA", "GOGL34.SA", "MSFT34.SA"]

database = pd.DataFrame()

for i in carteiras:
    database[i] = wb.get_data_yahoo(i, "2020-01-01")["Adj Close"]

# %%
database.info()

# %%
database.head()

# %%
database.tail()

# %%
database.iloc[0]

# %%
(database / database.iloc[0] * 100).plot(figsize=(8, 5))
plt.show()

# %%
ret_carteiras = (database / database.shift(1)) - 1
print(ret_carteiras.head())

# %%
pesos = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
print(np.dot(ret_carteiras, pesos))

# %%
mediacarteiras = ret_carteiras.mean() * 100
print(mediacarteiras)

# %%
mediaretornoanual = ret_carteiras.mean() * 250
print(mediaretornoanual)
mediacarteiras = ret_carteiras.mean() * 250

# %%
print(np.dot(mediaretornoanual, pesos))

# %%
portfolio = str(round(np.dot(mediaretornoanual, pesos), 5) * 100) + "%"
print(portfolio)

# %%
pesos2 = np.array([0.3, 0.3, 0.15, 0.05, 0.2])
portfolio2 = str(round(np.dot(mediaretornoanual, pesos2), 5) * 100) + "%"
print(portfolio2)

# %%
ind_carteiras = ["^GSPC", "^IXIC", "^GDAXI"]
indicadores = pd.DataFrame()

for t in ind_carteiras:
    indicadores[t] = wb.get_data_yahoo(t, "2000-01-01")["Adj Close"]

# %%
print(indicadores.head())

# %%
print(indicadores.tail())

# %%
(indicadores / indicadores.iloc[0] * 100).plot(figsize=(8, 5))
plt.show()

# %%
retindicadores = (indicadores / indicadores.shift(1)) - 1
print(retindicadores.tail())

# %%
retindicadoresanuais = retindicadores.mean() * 250
print(retindicadoresanuais)

# %%
carteiras = ["^BVSP", "AAPL"]
database = pd.DataFrame()

for i in carteiras:
    database[i] = wb.get_data_yahoo(i, "2010-01-01")["Adj Close"]

print(database.tail())

# %%
retorno = np.log(database / database.shift(periods=1))
print(retorno)

# %%
print(retorno["^BVSP"].mean())

# %%
print(retorno["^BVSP"].mean() * 250)

# %%
print(retorno["^BVSP"].std())

# %%
print(retorno["^BVSP"].std() * 250 ** 0.5)

# %%
print(retorno["AAPL"].mean())

# %%
print(retorno["AAPL"].mean() * 250)

# %%
print(retorno["AAPL"].std())

# %%
print(retorno["AAPL"].std() * 250 ** 0.5)

# %%
print(f"Média ^BVSP", retorno["^BVSP"].mean() * 250)

# %%
print(f"Média AAPL", retorno["AAPL"].mean() * 250)

# %%
print(f"Média entre ^BVSP e AAPL", retorno[["^BVSP", "AAPL"]].mean() * 250)

# %%
print(f"Desvio Padrão entre ^BVSP e AAPL", retorno[["^BVSP", "AAPL"]].std() * 250 ** 0.5)

# %% md
### Cotação de Ações
ticker = input("Digite o código da ação desejada: ")  # ^BVSP (IBOVESPA), BBAS3.SA (Banco do Brasil S.A), ...

dados = yf.Ticker(ticker)

print()

for k, v in dados.info.items():
    print(f"{k.capitalize()}: {v}")

# %%
df = pd.DataFrame(dados.history(period="max"))

# colunas: Date, Open, High, Low, Close, Volume, Dividends e Stock Splits
print(df)

# %%
# opções válidos para period: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y e ytd
tabela = dados.history(period="6mo")

close = tabela.Close

close.plot(figsize=(20, 4))
plt.show()

# %%
print(close)

# %%
# máximo e mínimo de cotação
print(close.max(), close.min())

# %%
# primeira e última linha do Close
print(close[0], close[-1])

# %%
iniData = datetime(2007, 2, 27)
fimData = datetime.now()

print(pd.DataFrame(dados.history(start=iniData, end=fimData)))

# %%
df: dict[str: list[int | str | float]] = {
    "id": [1, 2, 3],
    "nome": ["Rogério", "Carmem", "Giovana"],
    "curso": ["Delphi;Python;SQL;SAS", "Microsoft Office", "Word;Excel"],
    "salário": [8000.0, 1000.0, 500.0]
}

df = pd.DataFrame(df)
print(df)

print(df["curso"].str.len())

print(df[df["curso"].str.contains("Python")])

# %% md
### Teste sobre 'str'
data = {
    "id": [1, 2],
    "nome": ["Rogério", "Carmem"],
    "data": ["1972-01-30", "1977-10-19"],
    "kyc": ["testar     áudio578afaMÉDIO   data:30/01/1972", "dfd   ALTO5678datação    data:19/10/1977"],
    "trim": [" df~fm~trim~ ~trim xícara chá g12h   ", "  dgf;trim~trim~g  ~gk gf s~trim~trim ~t34m    "]
}

data = pd.DataFrame(data)
# %%
data["data"] = pd.to_datetime(data["data"])
data["idade"] = data["data"].apply(lambda x: pd.to_datetime("today").year - x.year)
print(data["idade"])

# %%
print(data[data["idade"].le(52)])

# %%
print(data[data["idade"].lt(52)])

# %%
print(data[data["idade"].le(50)])

# %%
print(pd.to_datetime(data["data"].astype(str) + " 11:59:59"))

# %%
print(pd.to_datetime(pd.to_datetime(data["data"].astype(str) + " 11:59:59").astype(str).str[:10] + " 23:59:59"))

# %%
print(data["kyc"].str[16:20].isin(["578a", "578y"]))

# %%
print(data["kyc"].str.find("MÉDIO"))

# %%
print(data[data["kyc"].str.find("MÉDIO").ne(-1)])

# %%
print(data["kyc"].str.len())

# %%
print(data["kyc"].str.count(r"\d"))

# %%
print(data["kyc"].str.count(r"\D"))

# %%
print(data["kyc"].str.count(r"\w"))

# %%
print(data["kyc"].str.count(r"\W"))

# %%
print(np.where(data["kyc"].str.find("data:1").eq(-1), False, True))

# %%
print(data["idade"].astype(str).str.contains(r"\d"))

# %%
data["data capturada 1"] = data["kyc"].str.extract(r"(\d{2}\/\d{2}\/\d{4})")  # str.extract sempre precisa de parênteses
data["data capturada 1"] = pd.to_datetime(data["data capturada 1"], format="%d/%m/%Y")
print(data["data capturada 1"])

# %%
print(data["kyc"].str.contains(r"\d{2}\/\d{2}\/\d{4}", case=False))  # str.extract sempre precisa de parênteses

# %%
print(data["kyc"].str.extract(r"(\d+)").astype(float) / 100)

# %%
print(data["trim"].replace(r"\w", "", regex=True))

# %%
print(data["trim"].replace(r"\W", "", regex=True))

# %%
print(data["trim"].str.extract(r"(\d+)"))

"""
ore["REFERENCIA"] = ore["X_FNLD_PGTO"].str.extract(r"0(.{,11})")
ore["REFERENCIA"] = ore["REFERENCIA"].str.extract(r"0(\d+)")

ore["CD_REF_DIGITOS"] = ore.apply(lambda x: sum(c.isdigit() for c in x["CD_REF"], axis=1)
ou
ore["CD_REF_DIGITOS"] = ore["CD_REF"].str.count(r"\d")

ore["VALA"] = ore.apply(lambda x: 6 if not x["CD_REF"].isdigit() or x["CD_REF_DIGITOS"] > 11 else 9, axis=1)
ou
ore["VALA"] = np.where(~ore["CD_REF"].isdigit() | ore["CD_REF_DIGITOS"].gt(11), 6, 9)

ore["REFERENCIA"] = ore.apply(lambda x: str(ore["REFERENCIA"].zfill(11) if x["REF_DIGITOS"] >= 10 else np.nan, axis=1)
ou
ore["REFERENCIA"] = np.where(ore["REF_DIGITOS"].ge(10), ore["REFERENCIA"].astype(str).str.zfill(11), np.nan)

lista_mci = tuple(ore["COD_MCI"].drop_duplicates().astype(int))

ore["CD_CCL_EXTO_BANQ"] = ore["CD_CCL_EXTO_BANQ"].astype(str).str.strip().str.zfill(11)

ore["SMT_REF"] = np.where(ore["DATA_REF"].dt.quarter.gt(2), 2, 1).astype(str)

ore["DT_ENTD"] = pd.to_datetime(ore.fillna({"DT_ENTD": "2099-12-31"}))

ore["tempo_atend"] = round(((ore["tempo_atend"] / np.timedelta64(1, 'h')) * 100), 0)

ore["MES"] = pd.to_datetime(ore["ts_abtr_ptl"]).dt.to_period('M').dt.to_timestamp()
"""
