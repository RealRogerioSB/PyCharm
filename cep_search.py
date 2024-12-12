# %%
import requests

cep = "41098040"
url_cep = f"https://viacep.com.br/ws/{cep}/json/"
request_cep = requests.get(url_cep)
dic_request_cep = request_cep.json()

for k, v in dic_request_cep.items():
    print(k, v)

print("-------------------------------------------------------------")

# %%
uf = "BA"
cidade = "Salvador"
logradouro = "Rua Thomaz Gonzaga"
url_log = f"https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/"
request_log = requests.get(url_log)
dic_request_log = request_log.json()

for x in dic_request_log:
    for k, v in x.items():
        print(k, v)
    print("-------------------------------------------------------------")
