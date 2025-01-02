def verificar_acertos(escolhidas, sorteadas):
    acertos = set(sorteadas).intersection(escolhidas)

    if len(acertos) == 4:
        return f"Você acertou 4 números -> {sorted(acertos)}"
    elif len(acertos) == 5:
        return f"Você acertou 5 números -> {sorted(acertos)}"
    elif len(acertos) == 6:
        return f"Você acertou 6 números -> {sorted(acertos)}"
    else:
        return f"Você não acertou nem 4, 5 e 6 números..."


bolas_escolhidas = [6, 13, 25, 33, 42, 50]
bolas_sorteadas = [6, 13, 25, 33, 42, 50]

resultado = verificar_acertos(bolas_escolhidas, bolas_sorteadas)
print(resultado)
