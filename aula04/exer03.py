'''
Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
'''
livro_01 = {
    "titulo": "Livro 01",
    "autor": "Autor 01",
    "ano": 2025
}

livro_02 = {
    "titulo": "Livro 02",
    "autor": "Autor 02",
    "ano": 2024
}

livro_03 = {
    "titulo": "Livro 03",
    "autor": "Autor 03",
    "ano": 2023
}

livros = []
livros.append(livro_01)
livros.append(livro_02)
livros.append(livro_03)

for livro in livros:
    print(f"\nTítulo: {livro["titulo"]}")
    print(f"Autor: {livro["autor"]}")
    print(f"Ano publicação: {livro["ano"]}")
    print(15*"-")