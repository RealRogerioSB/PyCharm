import math


def fatorial(x1):
    return 1 if x1 == 1 else x1 * fatorial(x1 - 1)


x2 = int(input("Para o fatorial da função, digite um número: "))

print(f"O fatorial de {x2} é {fatorial(x2)}")

x = int(input("Para o fatorial de math, digite um número: "))

print(f"O fatorial de {x} é {math.factorial(x)}")
