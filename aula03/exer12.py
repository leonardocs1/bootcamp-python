numero = int(input("Informe um número na faixa de 1 a 100: "))
while numero < 1 or numero > 100:
    print(f"{numero} fora da faixa!")
    numero = int(input("Informe um número na faixa de 1 a 100: "))
print(f"{numero} válido!")