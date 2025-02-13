try:
    c = float(input("Informe a temperatura em Celsius: "))
    f = c * 1.8 + 32
    print(f"{c:.2f}°C = {f:.2f}°F")
except:
    print("Por favor, digite um número válido para a temperatura.")