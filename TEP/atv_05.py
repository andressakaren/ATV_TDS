import numpy as np

# Caminho do arquivo da cidade
path = 'station_belem.csv'

# Carregar ignorando o cabeçalho (primeira linha), delimitador é vírgula
data = np.loadtxt(path, delimiter=',', skiprows=1)

# Exibir as 5 primeiras linhas
# print(data[:5])