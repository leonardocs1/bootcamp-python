valor1 = input("Informe um valor lógico (True/False): ").strip()
valor2 = input("Informe outro valor lógico (True/False): ").strip()

# Convertendo as strings para booleanos corretamente
valor1 = valor1.lower() == "true"
valor2 = valor2.lower() == "true"

resultado = valor1 or valor2
print(f"{valor1} or {valor2} = {resultado}")