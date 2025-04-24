# 14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0. Escrever a lista C modificada.

import random

def gerar_lista(tamanho=10):
    return [random.randint(-10, 10) for t in range(tamanho)]

def substituir_negativos(lista):
    for i in range(len(lista)):
        if lista[i] < 0:
            lista[i] = 0
    return lista

lista = gerar_lista()
print('Lista original:', lista)
lista_modificada = substituir_negativos(lista[:])  # copia
print('Lista modificada:', lista_modificada)
