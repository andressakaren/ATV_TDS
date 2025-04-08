# 4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.

def maior_elemento(lista):
    maior = lista[0]
    indice = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice = i
    return maior, indice

def menor_elemento(lista):
    menor = lista[0]
    indice = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice = i
    return menor, indice

def ler_sequencia():
    count = 0
    lista_original = []
    while count < 5:
        try: 
            num = int(input(f'Digite o {count+1}° número: '))
            lista_original.append(num)
            count += 1
        except:
            print('Digite um número válido')
            
    return lista_original

lista = ler_sequencia()
print('Lista original:', lista)  

maior, indice_maior = maior_elemento(lista)
menor, indice_menor = menor_elemento(lista)

print(f"Maior elemento: {maior}, indice: {indice_maior})")
print(f"Menor elemento: {menor}, indice: {indice_menor})")