pergunta = "Digite uma palavra ou uma frase: "

frase = input(pergunta).replace(" ", "").upper()

print(f"{'É o palíndromo!!!' if frase == frase[::-1] else 'Não é palíndromo...'}")
