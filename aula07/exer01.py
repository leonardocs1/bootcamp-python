from typing import List

def calcular_media(lista: List[float]) -> float:
    """
    Calcula a média de uma lista de float
    """
    return sum(lista) / len(lista)

lista_numeros = [1, 2, 3, 5.6, 8.4]
media = calcular_media(lista_numeros)

print(media)