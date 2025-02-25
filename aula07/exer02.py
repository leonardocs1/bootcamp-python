from typing import List

def filtra_acima(numeros: List[float], limite: float) -> List[float]:
    filtrados = [numero for numero in numeros if numero > limite]
    return filtrados

lista_numeros = [2, 77, 665, 44, 4, 0, 9 ,2, 334, 45]
numeros_filtrados = filtra_acima(lista_numeros, 50)

print(numeros_filtrados)