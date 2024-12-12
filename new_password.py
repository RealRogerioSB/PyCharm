import random
from string import digits
from string import punctuation
from string import ascii_letters

symbols = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()

password = int(input("Escolha o tamanho da senha: "))

print("".join(secure_random.choice(symbols) for _ in range(password)))
