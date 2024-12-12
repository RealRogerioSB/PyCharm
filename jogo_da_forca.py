import random

def imprime_mensagem_abertura():
    print("*************************************")
    print("*    Bem vindo ao jogo da Forca!    *")
    print("*************************************\n")


def carrega_fruta_secreta():
    with open("./src/frutas.txt") as arq:
        fruta = [linha.strip() for linha in arq]
    return fruta[random.randrange(0, len(fruta))].upper()


def inicializa_letras_acertadas(palavra):
    return ["_" for _ in palavra]


def pede_chute():
    return input("Qual letra? ").strip().upper()


def marca_chute_correto(shoot, matches, secreta):
    index = 0
    for letra in secreta:
        if shoot == letra:
            matches[index] = letra
        index += 1


def imprime_mensagem_vencedor(errors):
    print(f"\nParabéns!! Você acertou e só teve {errors} erro(s).")


def imprime_mensagem_perdedor(secreta):
    print(f"\nPuxa, você foi enforcado! A palavra era {secreta}.")


imprime_mensagem_abertura()
fruta_secreta = carrega_fruta_secreta()

letras_acertadas = inicializa_letras_acertadas(fruta_secreta)
print(letras_acertadas)

enforcou = acertou = False
erros = 0

while not enforcou and not acertou:
    chute = pede_chute()

    if chute in fruta_secreta:
        marca_chute_correto(chute, letras_acertadas, fruta_secreta)
    else:
        erros += 1

    enforcou = erros == len(fruta_secreta)
    acertou = "_" not in letras_acertadas

    print(letras_acertadas)

imprime_mensagem_vencedor(erros) if acertou else imprime_mensagem_perdedor(fruta_secreta)

print("Fim do jogo!")
