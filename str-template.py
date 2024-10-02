from string import Template

nomes = ["Ana", "Paulo", "Maria", "Rafael", "Patrícia"]

email = """
Olá, $nome!

Seja muito bem_vindo(a) ao curso Python!!

Abraço,
Rogério Balloussier
"""

template = Template(template=email)

for i in nomes:
    print(template.substitute(nome=i))
    print("-" * 42)
