import pandas as pd

df = pd.read_csv('clientes.csv')

pd.set_option('display.width', None)
print(df.head())

# Remover os dados
#df.drop('idade', axis=1, inplace=True) # Coluna
df.drop(2 , axis=0, inplace=True) # Linha

# Normalizar campos de texto
df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()  # .str.strip() → Remove espaços extras no início e no fim das strings
print(df.head())

# Converter tipos de dados
df['idade'] = df['idade'].astype(int)

# Tratar valores nulos (ausentes)

df_fillna = df.fillna(0) # Substituir valores nulos por 0
df_dropna = df.dropna() # Remover registros com valore nulos
df_dropna4 = df.dropna(thresh=4) # Manter o registros de no minimo 4 valores não nulos
df = df.dropna(subset=['cpf']) # Remover registros com o CPF nulo

#df = (# todas os tratamentos juntos
   # df.fillna(0)                # Substituir valores nulos por 0
  # .dropna()                   # Remover registros com qualquer valor nulo
  #  .dropna(thresh=4)           # Manter registros com no mínimo 4 valores não nulos
   #.dropna(subset=['cpf'])     # Remover registros com CPF nulo
#)

print('Valores nulos \n', df.isnull().sum())
print('Quantidade de registros nulos com fillna', df_fillna.isnull().sum().sum())
print('Quantidade de registos nulos com dropna', df_dropna.isnull().sum().sum())
print('Quantidade de registos nulos com dropna4', df_dropna4.isnull().sum().sum())
print('Quantidade de registos nulos com cpf', df.isnull().sum().sum())

# Especificar um campo
df.fillna({'estado':'desconhecido'}, inplace=True)
df['endereco'] = df['endereco'].fillna('Endereço não informado')
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())

# Tratar um formato de dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%y', errors='coerce')

# Tratar dados duplicados
print('Quantidade de registros atual', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True)
print('Quantidade de registros removendo as duplicadas',len(df))
print('Dados limpos\n', df)

#Salvar dataframe
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print(pd.read_csv('clientes_limpeza.csv'))


