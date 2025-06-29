import numpy as np
import csv

def carregar_dados_csv(mudancas_climaticas):
    anos = []
    cidades = []
    temperaturas = []
    co2 = []
    precipitacoes = []
    
    #ler aqyivo
    with open(mudancas_climaticas, 'r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        
        next(leitor_csv) # pula o cabeçalho
        
        for linha in leitor_csv:
            anos.append(int(linha[0]))         
            cidades.append(linha[1])          
            temperaturas.append(float(linha[2])) 
            co2.append(float(linha[3]))  
            precipitacoes.append(float(linha[4]))
    
    return anos, cidades, temperaturas, co2, precipitacoes

print("=" * 60)
print("Análise de dados climáticos com Numpy")
print()

anos, cidades, temperaturas, co2, precipitacoes = carregar_dados_csv('mudancas_climaticas.csv')

# print(anos)

anos_array = np.array(anos)
temperaturas_array = np.array(temperaturas)
co2_array = np.array(co2)
precipitacao_array = np.array(precipitacoes)

dados_numericos = np.column_stack((anos_array, temperaturas_array, co2_array, precipitacao_array))

print(f"Formato do array de dados numéricos: {dados_numericos.shape}")
print(f"Número total de registros: {len(cidades)}")
print(f"Cidades únicas: {list(set(cidades))}")

# a) Exiba as primeiras 5 linhas do dataset.

print("\n1. PRIMEIRAS 5 LINHAS DO DATASET")
print("-" * 40)
print("Formato: [Ano, Temperatura, CO2, Precipitação]")
print()

for i in range(5):
    print(f"Linha {i+1}: {cidades[i]:<15} {dados_numericos[i]}")
    
# b) Calcule e exiba a média da temperatura, nível de CO2 e precipitação de todas as cidades.

print("\n2. ESTATÍSTICAS DESCRITIVAS")
print("-" * 30)

media_temperatura = np.mean(temperaturas_array)
media_co2 = np.mean(co2_array)
media_precipitacao = np.mean(precipitacao_array)

print(f"Temperatura média global: {media_temperatura:.2f}°C")
print(f"Nível médio de CO2: {media_co2:.2f} ppm")
print(f"Precipitação média: {media_precipitacao:.2f} mm")

# c) Determine o índice da cidade com a maior temperatura média anual.

print("\n3. ANÁLISE DE VALORES MAIR TEMPERATURA")
print("-" * 35)

indice_max_temp = np.argmax(temperaturas_array)
maior_temperatura = temperaturas_array[indice_max_temp]

print(f"Maior temperatura registrada:")
print(f"  Valor: {maior_temperatura:.2f}°C")
print(f"  Cidade: {cidades[indice_max_temp]}")
print(f"  Ano: {anos[indice_max_temp]}")
print(f"  Índice no array: {indice_max_temp}")

# d) Encontre a cidade com o maior nível de CO2 e exiba suas informações completas.

print("\n4. ANÁLISE DE VALORES MAIR NÍVEL DE CO2")
print("-" * 35)

indice_max_co2 = np.argmax(co2_array)
maior_co2 = co2_array[indice_max_co2]

print(f"\nMaior nível de CO2 registrado:")
print(f"  Valor: {maior_co2:.2f} ppm")
print(f"  Cidade: {cidades[indice_max_co2]}")
print(f"  Ano: {anos[indice_max_co2]}")
print(f"  Temperatura: {temperaturas_array[indice_max_co2]:.2f}°C")
print(f"  Precipitação: {precipitacao_array[indice_max_co2]:.2f} mm")