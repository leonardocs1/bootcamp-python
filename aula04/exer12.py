'''
Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
'''
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}
dicionarios = dicionario1 | dicionario2
print(dicionarios)