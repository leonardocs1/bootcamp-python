"""
Implemente uma função que receba dois argumentos: uma lista de números e um número. 
A função deve retornar todas as combinações de pares na lista que somem ao número dado.
"""
from itertools import combinations

def encontra_pares(lista: list, alvo: int) -> list:
    return [par for par in combinations(lista, 2) if sum(par) == alvo]

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6]
soma_alvo = 7
print(encontra_pares(numeros, soma_alvo))