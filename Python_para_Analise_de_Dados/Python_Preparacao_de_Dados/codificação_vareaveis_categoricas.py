import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head(15))

#Codificação one-hot para estado civil
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)
print("\n DataFrame após a codificação one-hot para estamo civil: \n", df.head())

# Codificação ordinal para 'nivel_educação'
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós Graduação': 4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)
print("\n DataFrame após a codificação ordinal para nível de educação: \n", df.head())

# Transformar a area de atuação em categorias codificadas usando o método cat.codes

df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes
print("\n DataFrame após transformar 'area de atuacao' em codigos numericos: \n", df.head())

# LabelEconder para 'estado'
# LabelEconder converte cada valor único em número de 0 a n_classes-1
label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])
print("\n DataFrame após aplicar LabelEconder em 'estado': \n", df.head())


