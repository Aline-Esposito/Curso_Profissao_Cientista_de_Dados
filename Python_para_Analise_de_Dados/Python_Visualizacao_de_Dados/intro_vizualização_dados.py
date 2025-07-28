import matplotlib
import numpy as np

matplotlib.use('Agg')  # Usar backend não interativo
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Histograma
plt.hist(df['salario'])
plt.savefig('histograma_salario.png')

# Histograma - Parâmetros
plt.figure(figsize=(10, 6))
plt.hist(df['salario'], bins=100, color='blue', alpha=0.8)
plt.title('Histograma - Distribuição de Salarios')
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))
plt.ylabel('Frequência')
plt.grid(True)
plt.savefig('Histograma - Distribuição de Salarios.png')

# Múltiplos Gráficos
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1) # 2 linha # 2 Colunas 1ºGráfico
#Gráfico de dispersão
plt.scatter(df['salario'], df['salario'])
plt.title('Dispersão Sálario ')
plt.xlabel('Salario')
plt.ylabel('Salario')

plt.subplot(1, 2, 2) # 1 Linha, 2 Colunas, 2º Gráfico
plt.scatter(df['salario'], df['anos_experiencia'], color='red', alpha=0.6, s=30)
plt.title('Dispersão - Salario e Anos de Experiencia')
plt.xlabel('salario')
plt.ylabel('Anos de Experiencia')

# Mapa de calor
corr = df[['idade', 'salario']].corr()
plt.subplot(2, 2, 3) # 2 Linha, 2 Colunas, 3º Gráfico
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação de Salário e Idade')
plt.tight_layout()
plt.savefig('figira 3')
