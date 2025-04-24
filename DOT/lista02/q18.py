# 18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.
import random

def gerar_lista_negativos(tamanho=10):
    return [random.randint(-20, 20) for t in range(tamanho)]

def copiar_negativos(lista):
    negativos = []
    for valor in lista:
        if valor < 0:
            negativos.append(valor)
    return negativos


lista_x = gerar_lista_negativos()
lista_r = copiar_negativos(lista_x)
print('Lista X:', lista_x)
print('Lista R (apenas negativos):', lista_r)
