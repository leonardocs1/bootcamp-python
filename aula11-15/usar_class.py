from src.interface.classes.csv_class import CsvProcessor

arquivo_csv = './exemplo.csv'
arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtrar_por(['estado', 'preço'], ['SP', '10,50']))

# arquivo2 = './exemplo2.csv'
# limite2 = 'DF'

# arquivo_CSV2 = CsvProcessor(arquivo2)
# arquivo_CSV2.carregar_csv()
# print(arquivo_CSV2.filtrar_por(filtro, limite2))


