"""
13. Consumo de API Simulado
Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
"""

total_paginas = 20
pagina_atual = 1
while pagina_atual <= total_paginas:
    print(f"Processando página {pagina_atual} de {total_paginas}")
    pagina_atual += 1
print("Todas as páginas processadas!")