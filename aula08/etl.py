import pandas as pd 
import os
import glob


# uma funcao de extract que le e consolida os json
def extrair_dados_e_consolidar(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# uma funcao que transformacao
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df['Venda']
    return df

def carregar_dados(df: pd.DataFrame, format_saida: list):
    if 'csv' in format_saida:
        df.to_csv('dados.csv')
    if 'parquet' in format_saida:
        df.to_parquet('dados.parquet')

def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(path=pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)