import pandas as pd

# Carregar o dataset
df = pd.read_csv('heart.csv')

# Exibir as primeiras linhas do DataFrame
head = df.head()

# Exibir as últimas linhas do DataFrame
tail = df.tail()

# Verificar as dimensões do DataFrame
shape = df.shape

# Informações sobre as colunas
info = df.info()

# Estatísticas descritivas básicas
describe = df.describe()

head, tail, shape, describe

print()
print(head)
print(tail)
print(shape)
print(describe)