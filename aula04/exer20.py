"""
Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
"""
def ordena_chaves(dicionario: dict) -> list:
    chaves_ordenadas = sorted(dicionario.keys())
    return chaves_ordenadas

dicionario = {
    "nome": "Leonardo",
    "idade": 30,
    "cidade": "São Paulo",
    "profissao": "Desenvolvedor",
    "habilidades": ["Python", "SQL", "Power BI"]
}

print(ordena_chaves(dicionario))