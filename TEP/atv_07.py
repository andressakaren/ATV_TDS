import pandas as pd

dataset = pd.read_csv('carros.csv', sep=';')

dataset_head = dataset.head()

# tipos de dados
tipos_dados = dataset.dtypes

# estatística quilometragem e valor
estatisticas = dataset[['Quilometragem', 'Valor']].describe()

# 7 Verifica dados nulos por coluna
dados_nulos = dataset.isnull().sum()

# 8 Calcular a quilometragem média
def calcular_km_media(df, ano_atual):
    df = df.copy()
    df['Km_media'] = df['Quilometragem'] / (ano_atual - df['Ano'])
    return df['Km_media'].mean()

km_media_geral = calcular_km_media(dataset, 2025)

# qst 9a
diesel_v8 = dataset.query('Motor == "Motor Diesel V8"')

# 9b Carros com motor 1.0 8v usados (<100.000)
motor_1_0_usados = dataset.query('(Motor == "Motor 1.0 8v") & (Zero_km == False) & (Valor < 100000)')


info = dataset.info()

# print(dataset_head, tipos_dados, estatisticas)
print(dados_nulos)
print(diesel_v8)
print(motor_1_0_usados)
