# %%
import re

# ? → caractere alfanumérico facultativo
# * → ou zero, ou vários caracteres alfanumérico
# + →, ou um, ou vários caracteres alfanumérico obrigatório
# {n} → corresponde 'n' vezes o caractere alfanumérico
# {n,m} → corresponde 'n' vezes o caractere alfanumérico com m como máximo
# ^spam → corresponde a string exato inicial
# spam$ → corresponde a string exato final
# . → corresponde qualquer caractere exceto quebra de linha (para quaisquer basta re.DOTALL)
# \d → corresponde a um caractere numérico
# \D → corresponde a um caractere não numérico
# \w → corresponde a um caractere alfa
# \W → corresponde a um caractere não alfa
# \s → corresponde a um caractere de espaço
# \S → corresponde a um caractere que não seja espaço
# [abc] → corresponde a qualquer caractere que estiver dentro dos colchetes
# [^abc] → corresponde a qualquer caractere que não estiver dentro dos colchetes

phone_re = re.compile(r"((\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?)",
                      re.VERBOSE)
email_re = re.compile(r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))", re.VERBOSE)

# %%
# phone = re.compile(r"\d\d-\d\d\d\d\d-\d\d\d\d")
phone = re.compile(r"\d{2}-\d{5}-\d{4}")
mo = phone.search("Meu número é 61-98358-1972")
print(f"Número de celular localizado → {mo.group(0)}")

# %%
phone = re.compile(r"(\d{2})-(\d{5}-\d{4})")
mo = phone.search("Meu número é 61-98358-1972")
print(f"Número de celular: groups() → {mo.groups()}")
print(f"Número de celular: group(0) → {mo.group(0)}")
print(f"Número de celular: group(1) → {mo.group(1)}")
print(f"Número de celular: group(2) → {mo.group(2)}")

# %%
phone = re.compile(r"(\(\d{2}\))?(\d{5}-\d{4})")
mo = phone.search("Meu número é (61)98358-1972")
print(f"Número de celular: group(0) → {mo.group(0)}")
print(f"Número de celular: group(1) → {mo.group(1)}")
print(f"Número de celular: group(2) → {mo.group(2)}")
area, code = mo.groups()
print(f"Área do telefone   → {area}.")
print(f"Código do telefone → {code}.")

# %%
phone = re.compile(r"(\d{3}-)?\d{3}-\d{4}")
mo = phone.search("Meu número é 415-555-4242")
print(mo.group())
mo = phone.search("Meu número é 555-4242")
print(mo.group())

# %%
phone = re.compile(r"\(\d{2}\)\d{4,5}-\d{4}")
mo = phone.findall("Pessoal: (61)98358-1972 Trabalho: 3341-2214")
print(f"Localizados os números → {mo}")

# %%
word = re.findall(r"\bf[a-z]*", "which foot or hand fell fastest")
print(word)

# %%
peso = re.findall(r"(\w+)=(\d+)", "set width=20 and height=10")
print(peso)

# %%
hero = re.compile(r"Batman|Tina Fey")
mo = hero.search("Batman and Tina Fey")
print(f"Personagem: group() → {mo.group()}")
mo = hero.search("Tina Fey and Batman")
print(f"Personagem: group() → {mo.group()}")

# %%
batman = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batman.search("Batmobile lost a wheel")
print(mo.group())
print(mo.group(1))

# %%
batman = re.compile(r"Bat(wo)?man")
mo = batman.search("The Adventures of Batman")
print(mo.group())
mo = batman.search("The Adventures of Batwoman")
print(mo.group())

# %%
batman = re.compile(r"Bat(wo)*man")
mo = batman.search("The Adventures of Batman")
print(mo.group())
mo = batman.search("The Adventures of Batwoman")
print(mo.group())
mo = batman.search("The Adventures of Batwowowowowoman")
print(mo.group())

# %%
batman = re.compile(r"Bat(wo)+man")
mo = batman.search("The Adventures of Batwoman")
print(mo.group())
mo = batman.search("The Adventures of Batwowowowowoman")
print(mo.group())
mo = batman.search("The Adventures of Batman")
print(mo.group()) if mo else print("Não aparece...")

# %%
ha = re.compile(r"(ha){3}")
mo = ha.search("hahaha")
print(mo.group())
mo = ha.search("haha")
print(mo.group(), "\n") if mo else print("Não aparece...")

# %%
ha = re.compile(r"(ha){3,5}")
mo = ha.search("hahaha")
print(mo.group())
mo = ha.search("hahahaha")
print(mo.group())
mo = ha.search("hahahahaha")
print(mo.group())
mo = ha.search("haha")
print(mo.group(), "\n") if mo else print("Não aparece...")

# %%
xmas = re.compile(r"\d+\s\w+")
mo = xmas.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, ceroulas 8, 7 swans, 5 rings, 4 birds, 3 hens")
print(mo)

# %%
vogais = re.compile(r"[aeiouAEIOU]")
mo = vogais.findall("Robocop esats baby food. BABY FOOD.")
print(mo)

no_vogais = re.compile(r"[^aeiouAEIOU]")
mo = no_vogais.findall("Robocop esats baby food. BABY FOOD.")
print(mo)

# %%
begins = re.compile(r"^Hello")
mo = begins.search("Hello, World!")
print(mo) if mo else print("Não localizado...")
mo = begins.search("He said hello")
print(mo) if mo else print("Não localizado...")

ends = re.compile(r"\d{2}$")
mo = ends.search("Your number is 42")
print(mo) if mo else print("Não localizado...")
mo = ends.search("Your number is forty two")
print(mo) if mo else print("Não localizado...")

# %%
wholes = re.compile(r"^\d+$")
mo = wholes.search("1234567890")
print(mo) if mo else print("Não localizado...")
mo = wholes.search("12345xyw67890")
print(mo) if mo else print("Não localizado...")

ats = re.compile(r".at")
mo = ats.findall("The cat in the hat sat on the flat mat.")
print(mo)

# %%
names = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = names.search("First Name: Al Last Name: Sweigart")
print(mo.group(), " - ", mo.group(1), " - ", mo.group(2))

non = re.compile(r"<.*?>")
mo = non.search("<To serve man> for dinner.>")
print(mo.group())

non = re.compile(r"<.*>")
mo = non.search("<To serve man> for dinner.>")
print(mo.group())

# %%
no_newline = re.compile(".*")
mo = no_newline.search("Serve the public trust.\nProtect the innocent.\nUphold the law.")
print(mo.group())

yes_newline = re.compile(".*", re.DOTALL)
mo = yes_newline.search("Serve the public trust.\nProtect the innocent.\nUphold the law.")
print(mo.group())

# %%
robocop = re.compile(r"robocop", re.I)
mo = robocop.search("RoboCop is part man, part machine, all cop.")
print(mo.group())
mo = robocop.search("ROBOCOP protects the innocent.")
print(mo.group())
mo = robocop.search("Al, why does your programming book talk about robocop so much?.")
print(mo.group())

# %%
names = re.compile(r"Agent \w+")
mo = names.sub("'CENSURADO'", "Agent Alice gave the secret documents to Bob.")
print(mo)

names = re.compile(r"Agent (\w)\w+")
mo = names.sub(r"\1***", "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.")
print(mo)

# %%
conj = "purple alice@google.com, blah monkey bob@abc.com blah dishwasher"
print(conj)

# re.sub(pat, replacement, str) -- returns new string with all replacements,
# \1 is group(1), \2 group(2) in the replacement
print("→", re.sub(r"([\w.-]+)@([\w.-]+)", r"\1@yo-yo-dyne.com", conj))

# %%
yeah = re.search(r"word:\w\w\w", "an example word:cat!!")
print(f"{'localizado' if yeah else 'não localizado'} -→ {yeah.group()}")

# %%
yeah = re.search(r"pi+", "piiig")
print(r"'piiig' com 'pi+' →", yeah.group(0))
yeah = re.search(r"i+", "piigiiii")
print(r"'piigiiii' com 'i+' →", yeah.group(0))
yeah = re.search(r"..g", "piiig")
print(r"'piiig' com '..g' →", yeah.group())
yeah = re.search(r"\d\s*\d\s*\d", "xx1 2   3xx")
print(r"'xx1 2   3xx' com '\d\s*\d\s*\d' →", yeah.group(0))
yeah = re.search(r"\d\s*\d\s*\d", "xx12  3xx")
print(r"'xx12  3xx' com '\d\s*\d\s*\d' →", yeah.group(0))
yeah = re.search(r"\d\s*\d\s*\d", "xx123xx")
print(r"'xx123xx' com '\d\s*\d\s*\d' →", yeah.group(0))
yeah = re.search(r"^b\w+", "foobar")
print(r"'foobar' com '^b\w+' →", yeah.group(0)) if yeah else print(r"'foobar' com '^b\w+' → not match")
yeah = re.search(r"b\w+", "foobar")
print(r"'foobar' com 'b\w+' →", yeah.group(0))

# %%
texto = """Prezados,

Segue a lista de produtos à venda.
1) pão francês → R$1,35
2) leite integral líquido 1 l → R$7,49
Estou à disposição para negociar.

At.te,
"""

valores = re.findall(r"R\$\d+,\d+", texto)
print(valores)
