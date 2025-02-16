'''
Divisão de Dados em Grupos
Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
'''
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in valores if num % 2 == 0]
impares = [num for num in valores if num % 2 != 0]
print("Pares: ", pares)
print("Impares: ", impares)