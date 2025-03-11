# Estudo do dataframe
import pandas as pd

# Lista: é uma coleção ordenada de elementos que podem ser de qualquer tipo

lista_nomes = ['Ana', 'André', 'Adolfo']
print('Lista de nomes \n', lista_nomes)
print('Primeiro elemento da lista \n', lista_nomes[0])

# Dicionário: estrutua composta de pares chave-valor
dicionario_pessoa = {
    'nome': 'Ana',
    'idade': '56',
    'cidade':'Tupã'
}
print('Dicionario de uma pessoa \n', dicionario_pessoa)
print('Atributo de uma pessoa', dicionario_pessoa.get('idade'))

#Lista de dicionários: Estrutura de dados que combina lista e dicionários
dados = [
    {'nome': 'Ana', 'idade': '56', 'cidade': 'Tupã'},
    {'nome': 'Adolfo', 'idade': '32', 'cidade': 'Tupã'},
    {'nome': 'André', 'idade': '30', 'cidade': 'Tupã'}
]

# Dataframe: estrutura de dados bidimensional
df = pd.DataFrame(dados)
print('DataFrame \n', df)

#Selecionar uma coluna
print(df['nome'])

#Selecionar varias colunas
print(df[['nome', 'idade']])

#Selecionar linha pelo indice
print('Primeira linha \n', df.iloc[0])

#Adicionar um a nova linha
df['salario'] = ['1000', '2000', '3000']

#Adicionar um novo registro
df.loc[len(df)] = [
    'Ademir',
    '58',
    'Tupã',
    '4000'
]
print('DataFrame \n',df)

#Remover colunas
df.drop('salario', axis=1, inplace=True) #axis=1 referente a coluna axis=0 referente a linha
print(df)

#Filtrando
df['idade'] = pd.to_numeric(df['idade'], errors='coerce') 
filtro_idade = df[df['idade'] >= 32]
print('Filtro \n', filtro_idade)
