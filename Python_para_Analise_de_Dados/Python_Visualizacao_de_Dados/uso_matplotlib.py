import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head(20).to_string())

# Gráficos de barras

plt.figure(figsize=(10, 6))
df['nivel_educacao'].value_counts().plot(kind='bar', color='blue')
plt.title('Divisão de Escolaridade - 1')
plt.xlabel('Nivél de educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color='blue')
plt.title('Divisão de Escolaridade - 2')
plt.xlabel('Nivel de Educacao')
plt.ylabel('Quantidade')

# Gráfico de pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição de Nivél de Educação')
plt.savefig('Distribuição de Nivél de Educação.png')
plt.show()

# Gáfico de dispersão
plt.hexbin(df['idade'], df['salario'], gridsize=4, cmap='Blues')
plt.colorbar(label='Salario')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.title('Dispersão de Idade e Salario')
plt.show()
