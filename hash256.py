from hashlib import sha256

senha = "12345"
hash_senha = sha256(senha.encode())
print(hash_senha)

senha_armazenar = hash_senha.digest()
print(senha_armazenar)
print(len(senha_armazenar))

senha_armazenar = hash_senha.hexdigest()
print(senha_armazenar)
print(len(senha_armazenar))

login = input("Entre o seu login: ")

hash_login = sha256(login.encode()).hexdigest()
print(hash_login)

senha_login = input("Senha login: ")

if sha256(senha_login.encode()).hexdigest() == senha_armazenar:
    print("Senha login confirmado.")
else:
    print("senha inválida.")
