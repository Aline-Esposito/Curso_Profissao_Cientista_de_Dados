import pandas as pd
import random
from faker import Faker

faker = Faker('pt_Br')

dados_pessoas = []

for _ in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 60)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime('%d/%m/%y')
    endereco = faker.address()
    estado = faker.state()
    pais = 'Brasil'

    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'data': data,
        'endereço': endereco,
        'estado': estado,
        'pais': pais
    }
    dados_pessoas.append(pessoa)


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

df_pessoas = pd.DataFrame(dados_pessoas)
print(df_pessoas)

df_pessoas.to_csv('Clientes.csv')



