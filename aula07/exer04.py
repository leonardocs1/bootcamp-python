from typing import List

def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    temperaturas_fahrenheit = [(c * 9/5) + 32 for c in temperaturas_celsius]
    return temperaturas_fahrenheit

lista_celsius = [67.5, 43.7, 100, 45.8, 80]

print(celsius_para_fahrenheit(lista_celsius))