"""
6. Contagem de Palavras em Textos
Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
"""

texto = """
A tecnologia está mudando a forma como as empresas tomam decisões tornando os dados um ativo estratégico essencial
as ferramentas de análise permitem visualizar informações de maneira dinâmica e interativa a automação de processos 
reduz erros e melhora a eficiência a inteligência de dados ajuda a identificar oportunidades e riscos investir em dados 
é essencial para se manter competitivo no mercado
"""

texto_quebrado = texto.split(" ")
texto_contado = {}

for palavra in texto_quebrado:
    if palavra in texto_contado:
        texto_contado[palavra] += 1
    else:
        texto_contado[palavra] = 1

print(texto_contado)