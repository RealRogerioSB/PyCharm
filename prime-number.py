num = int(input("Digite um número: "))
divs = 0

for i in range(1, num + 1):
    if num % i == 0:
        divs += 1

print(f"\n{num} {'é' if divs == 2 else 'não é'} primo!!!")
print(f"{num} é divisível por 1 ou por si mesmo." if divs == 2 else f"{num} é divisível por {divs} vez(es)...")
