# 5) Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os elementos deste em uma outra lista de 20 elementos.

def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    for i in range(10):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    return lista_intercalada


def ler_lista():
    lista = []
    count = 0
    while count < 10:
        try:
            num = int(input(f'Digite o {count+1}º número da lista: '))
            lista.append(num)
            count += 1
        except:
            print('Digite um número válido!')
    return lista


lista1 = ler_lista()
lista2 = ler_lista()

lista_intercalada = intercalar_listas(lista1, lista2)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista Intercalada:", lista_intercalada)
