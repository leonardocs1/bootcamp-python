entrada = input("Digite uma palavra ou uma frase: ")
if isinstance(entrada, str):
    tratado = entrada.replace(" ", "").lower()
    if tratado == tratado[::-1]:
        print(f"{tratado} é um palíndromo!")
    else:
        print(f"{tratado} não é um palíndromo!")
else:
    print("Informe uma palavra ou frase válida!")