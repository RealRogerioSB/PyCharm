import random
from string import ascii_letters, digits, punctuation

symbols = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()

password = int(input("Escolha o tamanho da senha: "))

print("".join(secure_random.choice(symbols) for _ in range(password)))
