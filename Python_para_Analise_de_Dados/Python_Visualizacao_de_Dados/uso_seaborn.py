mport pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Gráfico de Dispersão
sns.jointplot(x='idade', y='salario', data=df, kind='scatter')
plt.show()

# Gráfico de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['salario'], fill=True, color='red')
plt.show('Densidade de Salários')
plt.xlabel('Salario')
plt.show()

# Gráfico de Pairplot - Dispersão e Histograma
sns.pairplot(df, vars=['idade', 'salario', 'anos_experiencia', 'nivel_educacao'])
plt.show()

# Gráfico de Regressão
sns.regplot(x='idade', y='salario', data=df, color='red', scatter_kws={'color': 'blue'})
plt.title('Regressão se Salário por Idade')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.show()

# Gráfico countplot com hue
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade de clientes')
plt.legend(title='Nivel de Educação')
plt.show()

df_corr = df[['salario', 'anos_experiencia', 'nivel_educacao_cod','area_atuacao_cod','estado_cod']].corr()
# Heatmap de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(df_corr, annot=True, fmt='.2f')
plt.title('Mapara de Calor da Correlação entre Variáveis')
plt.show()
