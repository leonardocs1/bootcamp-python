from etl import pipeline_calcular_kpi_de_vendas_consolidado

pasta = 'data'
formato_de_saida: list = ['csv']

pipeline_calcular_kpi_de_vendas_consolidado(formato_de_saida=formato_de_saida, pasta=pasta)