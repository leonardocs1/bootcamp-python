'''
Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
'''
texto: str ="""
O sol nascia no horizonte, pintando o céu com tons de laranja e dourado. 
O som das ondas quebrando suavemente na areia misturava-se com o canto dos pássaros, 
criando uma melodia tranquila. Caminhando pela praia, sentia a brisa fresca tocar o rosto, 
trazendo consigo o cheiro do mar e a promessa de um novo dia cheio de possibilidades. 
Cada pegada deixada na areia era apagada lentamente pela maré, 
lembrando que tudo na vida é passageiro, mas cada momento vivido pode ser inesquecível.
"""

texto_limpo: str = texto.replace(".","").replace(",","")
lista_palavras: list = texto_limpo.split(" ")
ocorrencias: dict = {}

for palavra in lista_palavras:
    if palavra not in ocorrencias:
        ocorrencias[palavra] = 1
    else:
        ocorrencias[palavra] += 1

print(ocorrencias)
