import pandas as pd
from sklearn.preprocessing import RobustScaler , MinMaxScaler, StandardScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

df = df[['idade', 'salario']] # Não irei utilizar todos os dados apenas os dados de idade e salario

# Normalização - MinMaxScaler
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

# Padronização - StandardScaler
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

# Padronização - RobustScaler

scaler_idade_robust = RobustScaler()
df['idadeRobustScaler'] = scaler_idade_robust.fit_transform(df[['idade']])

scaler_salario_robust = RobustScaler()
df['salarioRobustScaler'] = scaler_salario_robust.fit_transform(df[['salario']])

print(df.head(15))

