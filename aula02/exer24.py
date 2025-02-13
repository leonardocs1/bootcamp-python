try:
    numero = int(input("Insira um número inteiro: "))
    if numero > 0:
        print("POSITIVO")
    elif numero < 0:
        print("NEGATIVO")
    else:
        print("ZERO")

    if numero % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")
except ValueError:
    print("Insira um número inteiro válido.")