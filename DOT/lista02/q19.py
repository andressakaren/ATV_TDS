# 19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos de S. Escrever a lista X.

import random

def gerar_lista(tamanho, minimo=0, maximo=100):
    return [random.randint(minimo, maximo) for t in range(tamanho)]

def juntar_listas(r, s):
    return r + s

lista_r = gerar_lista(5)
lista_s = gerar_lista(10)
lista_x = juntar_listas(lista_r, lista_s)
print("Lista R:", lista_r)
print("Lista S:", lista_s)
print("Lista X (R + S):", lista_x)
