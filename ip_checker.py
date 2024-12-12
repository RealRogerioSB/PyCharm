import requests

# faz uma requisição GET ao site ipify
response = requests.get("https://www.google.com/")

# obtém o endereço de IP com estado de resposta
print(f"O status do endereço de IP é {response.status_code}.")
