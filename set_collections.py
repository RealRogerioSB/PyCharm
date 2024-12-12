#%%
import collections as col

estoque = ["iphone", "iphone", "ipad", "airpod", "ipad", "iphone", "iphone"]
dict_counter = col.Counter(estoque)
print(dict_counter)
print(dict_counter["iphone"])
#%%
vendas = {"André": 1000, "João": 2000, "Lira": 500, "Amanda": 1500, "Carol": 3000, "Marcus": 200, "Camila": 400,
          "Andréia": 8000}
meta1 = 1000
meta2 = 2000

dic_bonus = col.defaultdict(list)
for vendedor in vendas:
    if vendas[vendedor] > meta2:
        dic_bonus["meta2"].append(vendedor)
    elif vendas[vendedor] > meta1:
        dic_bonus["meta1"].append(vendedor)
    else:
        dic_bonus["sem meta"].append(vendedor)

print(dic_bonus)
#%%
brinquedos = {"Lego": 30, "Banco Imobiliário": 10}
hardwares = {"Tablet": 5, "Mouse": 5, "Iphone": 15}
roupas = {"Jeans": 150, "Camisa": 100}

estoque = col.ChainMap(brinquedos, hardwares, roupas)
print(estoque)
print(estoque["Jeans"])
print(list(estoque.keys()))
#%%
fila = col.deque(["item1", "item2", "item3"])
print(fila)
fila.append("item4")
print(fila)
fila.appendleft("item5")
print(fila)
fila.pop()
print(fila)
fila.popleft()
print(fila)
#%%
Produto = col.namedtuple("Produto", ["nome", "preco", "tamanho"])

produto1 = Produto("camisa", 150, "M")
print(produto1.nome)
print(produto1[0])
print(produto1.preco)