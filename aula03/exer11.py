"""
11. Leitura de Dados até Flag
Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
"""

entrada = ""
while True:
    entrada = input("Digite um valor (ou 'sair' para terminar): ")
    if entrada.strip().lower() == 'sair':
        break