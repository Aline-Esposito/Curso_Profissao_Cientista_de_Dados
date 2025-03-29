import pandas as pd


# Função para calcular o cubo de um  numero
def eleva_cubo(x):
    return x ** 3

# Expressão de lambda para calcular o cubo de um número

eleva_cubo_lambda = lambda x: x ** 3 # não há necessidade dessa linha, mas foi colocada por  didádica

print(eleva_cubo(2))
print(eleva_cubo_lambda(2))

df = pd.DataFrame({'numeros': [1, 2, 3, 4, 5, 10]})

df['Cubo_função'] = df['numeros'].apply(eleva_cubo)
df['Cubo_função_lambda'] = df['numeros'].apply(lambda x: x ** 3)
df['Cubo_função_lambda'] = df['numeros'].apply(lambda x: x * 10)
print(df)