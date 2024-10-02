def fibonacci_of(n):
    return n if n in [0, 1] else fibonacci_of(n - 1) + fibonacci_of(n - 2)


num = int(input("Escolha um número para gerar série de Fibonacci: "))

print(f"Série de Fibonacci >> {[fibonacci_of(n) for n in range(num)]}")
