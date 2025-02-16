'''
Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
'''
idades = [22, 15, 30, 17, 18]
idades_maiores_18 = [idade for idade in idades if idade >= 18]
print(idades_maiores_18)