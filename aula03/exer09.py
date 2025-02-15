"""
9. Extração de Subconjuntos de Dados
Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.
"""

numeros = range(1, 11)

numeros_pares = [numero for numero in numeros if numero % 2 == 0]

print(numeros_pares)