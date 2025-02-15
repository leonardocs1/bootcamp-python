"""
Exercício 4: Validação de Dados de Entrada
Antes de processar os dados de usuários em um sistema de recomendação, 
você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
fornecido um email válido. Escreva um programa que valide essas 
condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.
"""
idade = int(input("Informe a idade: "))
email = input("Informe o e-mail: ")

if idade < 18 or idade > 65:
    print("Idade inválida!")
elif '.' not in email or '@' not in email:
    print('E-mail inválido!')
else:
    print('Dados de usuário válidos')