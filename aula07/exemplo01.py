import pandas as pd
import numpy as np

try:
    print('\nObtendo os dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    # utf-8, iso-8859-1, latin1, co1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # variáveis
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]
    
    # Totalizando os roubos pelos municípios
    df_roubo_veiculo = df_roubo_veiculo.groupby('munic', as_index=False)['roubo_veiculo'].sum()
    
    # Ordenando o df
    df_roubo_veiculo = df_roubo_veiculo.sort_values(by='roubo_veiculo', ascending=False)
    
    
    print(df_roubo_veiculo.head(10))
except Exception as e:
    print(f'Erro ao obter dados\nErro de{e}')
    


# Obtendo as medidas
try:
    print('\nCalculando as medidas...')    
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])
    
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    distancia = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo * 100)
    
    
    print('\nMedidas de Tendência Central')
    print(30*'-')
    print(f'Média: {media_roubo_veiculo}')
    print(f'Mediana: {mediana_roubo_veiculo}')
    print(f'Distância da média para mediana: {distancia:.2f} %')
    
# 0 - 10% dados simétricos = tem a tendencia de seguir uma certa simetria
# 10 - 25% dados assimetricos = tem a tendencia de ter uma assimetria moderada pode ser usada cmo uma medida de resumo
# 25%+ não é padrão =  

except Exception as e:
    print(f'Erro ao processar as medidas: {e}')