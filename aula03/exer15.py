"""
15. Processamento de Dados com Condição de Parada
Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada.
"""
itens = [1, 2, 3, "parar", 4, 5]
i = 0
while i < len(itens):
    if itens[i] == 'parar':
        print("Processamento encerrado")
        break
    print(f"processando item: {itens[i]}")
    i += 1