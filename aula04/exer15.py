'''
Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
'''
texto = "engenharia de dados"
frequencia = {}

for letra in texto:
    if letra in frequencia:
        frequencia[letra] += 1
    else:
        frequencia[letra] = 1
print(frequencia)