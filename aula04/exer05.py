'''
Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
calcule o preço total da lista de compras.
'''
lista_produtos: list = ["maçã", "banana", "cereja"]
dicionarios_produtos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

preco_total: float = sum(dicionarios_produtos[produto] for produto in lista_produtos )
print(f"Preço total: {preco_total:.2f}")