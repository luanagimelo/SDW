import pandas as pd

'carrega e le arquivo csv'
df = pd.read_csv('cats.csv')

'recebe dados de cores para os gatos'
for index, cat in df.iterrows():
    nome = cat['Cat']
    cores = input(f"Insira cor de {nome}: ")
    
    df.at[index, 'Color'] = cores

'atualiza a planilha'
df.to_csv('cats.csv', index=False)
