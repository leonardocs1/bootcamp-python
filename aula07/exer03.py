from typing import List

def contar_valores_unicos(valores: List[int]) -> int:
    return len(set(valores))

valores = [1, 2, 2, 3, 4, 5, 6, 6]
print(contar_valores_unicos(valores=valores))