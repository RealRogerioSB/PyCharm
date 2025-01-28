from string import Template

nomes = ["Ana", "Paulo", "Maria", "Rafael", "Patrícia"]

email = """
Olá, $nome!

Seja muito bem-vindo(a) ao curso Python!!

Abraço,
Rogério Balloussier
"""

template = Template(template=email)

for nome in nomes:
    print(template.substitute(nome=nome))
    print("-" * 42)
