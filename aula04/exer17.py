"""
Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
"""
def verifica_numero_primo(numero: float) -> bool:
    qtd_divisores = 0
    for divisor in range(1, numero+1):
        if numero % divisor == 0:
            qtd_divisores += 1
        
    return qtd_divisores == 2

print("1: ", verifica_numero_primo(1))
print("2: ", verifica_numero_primo(2))
print("3: ", verifica_numero_primo(3))
print("4: ", verifica_numero_primo(4))
print("5: ", verifica_numero_primo(5))
print("7: ", verifica_numero_primo(7))
print("11: ", verifica_numero_primo(11))

