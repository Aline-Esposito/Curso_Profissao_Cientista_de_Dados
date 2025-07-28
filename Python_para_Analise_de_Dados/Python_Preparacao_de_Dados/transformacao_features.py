import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')
print(df.head())

# Transformação Logaritimica
df['salario_log'] = np.log1p(df['salario']) #log1p é usado para evitar problemas com valores zero
print('\n Data frame após a transfomação logaritmica no salario: \n',  df.head())

# Transformação Box Cox
df['salario_boxcox'], _ = stats.boxcox(df['salario'] + 1)
print(df.head())

# Codificação de frequencia para 'estado'

estado_freq = df['estado'].value_counts() / len(df)
df['estado_freq'] = df['estado'].map(estado_freq)
print(df.head())

# Interações
df['Interação_idade_filhos'] = df['idade'] * df['numero_filhos']
print(df.head())