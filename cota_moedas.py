import requests

get_cota_us = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL").json()
get_cota_eu = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL").json()
get_cota_gb = requests.get("https://economia.awesomeapi.com.br/last/GBP-BRL").json()

print(" Cotação do Dólar ".center(43, "#"))
print(f"Moeda $   : {get_cota_us["USDBRL"]["name"]}")
print(f"Data/Hora : {get_cota_us["USDBRL"]["create_date"]}")
print(f"Valor (R$): {get_cota_us["USDBRL"]["bid"].replace(".", ",")}")

print(" Cotação do Euro ".center(43, "#"))
print(f"Moeda $   : {get_cota_eu["EURBRL"]["name"]}")
print(f"Data/Hora : {get_cota_eu["EURBRL"]["create_date"]}")
print(f"Valor (R$): {get_cota_eu["EURBRL"]["bid"].replace(".", ",")}")

print(" Cotação do Libras ".center(43, "#"))
print(f"Moeda $   : {get_cota_gb["GBPBRL"]["name"]}")
print(f"Data/Hora : {get_cota_gb["GBPBRL"]["create_date"]}")
print(f"Valor (R$): {get_cota_gb["GBPBRL"]["bid"].replace(".", ",")}")
