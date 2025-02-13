entrada = input("Informe uma sequência de números inteiros separados por virgula: ")
numeros_str = entrada.split(",")
numeros_int = []
try:
    for numero in numeros_str:
        numeros_int.append(int(numero.strip()))
    print("Lista de números interos: ", numeros_int)
except ValueError:
    print("Certifique-se que todos os números digitados são inteiros")
