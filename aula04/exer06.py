'''
Eliminação de Duplicatas
Objetivo: Dada uma lista de emails, remover todos os duplicados.
'''
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_nao_duplicados = list(set(emails))
print(emails_nao_duplicados)