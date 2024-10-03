#%%
import holidays
import pandas_market_calendars as pmc

feriados_br = holidays.country_holidays("BR")
feriados_2025 = feriados_br["2025-01-01":"2025-12-31"]

for feriado in feriados_2025:
    print(feriado)

#%%
feriados_df = holidays.country_holidays("BR", "DF")
for feriado in feriados_df["2024-01-01":"2024-12-31"]:
    print(feriado)

#%%
anual = pmc.get_calendar("BMF")
dias_2025 = anual.schedule(start_date="2025-01-01", end_date="2025-12-31")
print(dias_2025)
