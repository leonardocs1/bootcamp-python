"""
10. Agregação de Dados por Categoria
Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
"""

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

preco_categoria = {}

for venda in vendas:
    categoria = venda['categoria']
    preco = venda['valor']
    if categoria in preco_categoria:
        preco_categoria[categoria] += preco
    else:
        preco_categoria[categoria] = preco

print(preco_categoria)