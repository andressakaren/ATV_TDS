# 13) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de cada face.

def ler_resultados(n):
    resultados = []
    count = 0
    while count < n:
        try:
            valor = int(input(f'Digite o resultado do lançamento {count+1} (entre 1 e 6): '))
            if 1 <= valor <= 6:
                resultados.append(valor)
                count += 1
            else:
                print('Digite um número entre 1 e 6.')
        except:
            print('Digite um valor válido.')
    return resultados

def contar_ocorrencias(resultados):
    ocorrencias = [0, 0, 0, 0, 0, 0]  # 0 a 5 p representar as faces 1 a 6
    for valor in resultados:
        ocorrencias[valor - 1] += 1
    return ocorrencias

def exibir_ocorrencias(ocorrencias):
    for i in range(len(ocorrencias)):
        print(f'Face {i+1}: {ocorrencias[i]} ocorrência(s)')

try:
    n = int(input('Quantos lançamentos foram feitos? '))
    resultados = ler_resultados(n)
    ocorrencias = contar_ocorrencias(resultados)
    print('Ocorrências de cada face:')
    exibir_ocorrencias(ocorrencias)
except:
    print('Insira um número válido de lançamentos.')
