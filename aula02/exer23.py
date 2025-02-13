operadores = ['+', '-', '*', '/']
resultado = 0.0
try:
    num1 = float(input("Informe um número: "))
    num2 = float(input("Informe outro número: "))
    operador = input("Informe o operador (+, -, * /): ")
    if operador in operadores:
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        else:
            resultado = num1 / num2
        
        print(f"{num1} {operador} {num2} = {resultado}")
    else:
        print("Operador inválido!")
except ZeroDivisionError:
    print("Divisão por zero!")
except ValueError:
    print("Valor inválido digitado!")
