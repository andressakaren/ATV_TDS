# 16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3. Escrever as listas X e Y.

# usando randm

import random
def gerar_lista(tamanho=10):
    return [random.randint(1, 100) for t in range(tamanho)]

def transformar_lista(x):
    y = []
    for i in range(len(x)):
        if i % 2 == 0:
            y.append(x[i] // 2)
        else:
            y.append(x[i] * 3)
    return y

lista_x = gerar_lista()
lista_y = transformar_lista(lista_x)
print("Lista X:", lista_x)
print("Lista Y:", lista_y)
