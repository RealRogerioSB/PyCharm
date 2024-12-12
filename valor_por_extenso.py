while not ((x := input("Digite o número entre 0 e 100 a converter por extenso: ")).isdigit() and 0 <= int(x) <= 100):
    continue


def num_extenso(n):
    unidade = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dez_x = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezena = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa", "cem"]

    return dezena[n // 10] + " e " + unidade[n % 10] \
        if n >= 20 and n % 10 != 0 else dezena[n // 10] \
        if n >= 20 and n % 10 == 0 else dez_x[n % 10] \
        if 10 <= n < 20 and n % 10 == 0 else dez_x[n - 10] \
        if 10 <= n < 20 and n % 10 != 0 else unidade[n] \
        if n < 10 and n % 10 != 0 else unidade[0]


print(f"\nO número por extenso é {num_extenso(int(x))}.")
