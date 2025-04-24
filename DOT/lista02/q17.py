# 17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V aparece. Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto.


import random

def gerar_lista(tamanho=10):
    return [random.randint(1, 20) for t in range(tamanho)]

def contar_ocorrencias(lista, valor):
    indices = []
    for i in range(len(lista)):
        if lista[i] == valor:
            indices.append(i)
    return indices

lista_w = gerar_lista()
print('Lista W:', lista_w)

try:
    valor_v = int(input('Digite o valor a ser procurado: '))
    posicoes = contar_ocorrencias(lista_w, valor_v)
    if posicoes:
        print(f'O valor {valor_v} ocorre {len(posicoes)} vez(es), nas posições: {posicoes}')
    else:
        print(f'O valor {valor_v} não ocorre na lista.')
except:
    print('Valor inválido.')
