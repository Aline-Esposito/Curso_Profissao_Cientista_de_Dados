import pandas as pd

df = pd.read_csv('clientes-v2.csv')

print(df.head().to_string())
print(df.tail().to_string())
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print('Verificação inicial:')
print(df.info())

print('Analise de dados nulos:\n', df.isnull().sum())
print('% de dados nulos:\n' , df.isnull().mean() * 100)
df.dropna(inplace=True)
print('Confrmar a remoção de dados nulos:\n' , df.isnull().sum().sum())

print('Analise de dados suplicados:\n', df.duplicated().sum())

print('Analise de dados únicos:\n', df.nunique())

print('Estatisticas dos dados:\n' , df.describe())

df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head().to_string())

df.to_csv('clientes-v2-tratados.csv', index=False)
import os
print(os.getcwd())





