import pandas as pd

df = pd.read_csv('clientes.csv')

# Verificar os primeiros registros
print(df.head().to_string())

# Verificar os ultimos registros
print(df.tail().to_string())

# Verificando quantidade de linhas e colunas
print('Quantidade:', df.shape)

# Verificar o tipo de dados
print('Tipagem:\n', df.dtypes)

# Checar valores nulos
print('Valores nulos:', df.isnull().sum())

