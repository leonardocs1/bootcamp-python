valor = input("Informe um valor lógico (True/False): ").strip()
valor = not valor.lower() == "true"
print(f"Resultado investido: {valor}")
