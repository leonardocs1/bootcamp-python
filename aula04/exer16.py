"""
Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
"""

def soma_lista(lista: list) -> int:
    return sum(lista)

lista_numeros = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
soma = soma_lista(lista_numeros)

print(soma)