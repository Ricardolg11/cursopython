import pandas
import random

import pandas as pd
from faker import Faker

faker = Faker('pt_BR')

dados_pessoas = [] # Crinado uma lista

for _ in range(10): # Setando lista tamanho 10
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 50)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade ).strftime('%d/%m/%Y')
    endereco = faker.street_address()
    estado = faker.state()
    pais = 'Brasil'

    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'data': data,
        'endereco': endereco,
        'estado': estado,
        'pais': pais,
    }

    dados_pessoas.append(pessoa)

df_pessoas = pd.DataFrame(dados_pessoas) #dataframe para gera a base de dados
print(df_pessoas)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print(df_pessoas.to_string()) #head() convertendo o codigo em string para pequeno exemplos

df_pessoas.to_csv('clientes.csv')


