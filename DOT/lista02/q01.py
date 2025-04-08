def par_impar(n):
    return n % 2 == 0


def receber_inteiros(n):
    lista_total = []
    lista_par = []
    lista_impar = []

    count = 0
    while count < n:
        try:
            valor = int(input(f'Digite o {count + 1}° numero inteiro: '))
            lista_total.append(valor)

            if par_impar(valor):
                if valor not in lista_par:
                    lista_par.append(valor)
            else:
                if valor not in lista_impar:
                    lista_impar.append(valor)
            count += 1
        except:
            print('Digite um número válido!')
    return lista_total, lista_par, lista_impar


lista_total, lista_par, lista_impar = receber_inteiros(5)

# 1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
print('Lista total:', lista_total)
# a) Mostre a quantidade de números pares;
print('Quantidade de números pares:', len(lista_par))
# b) Grave uma lista somente com os números pares e mostre a lista;
print('Lista somente com números pares:', lista_par)
# c) Mostre a quantidade de números ímpares;
print('Quantidade de números impares:', len(lista_impar))
# d) Grave uma lista somente com os números ímpares e mostre a lista.
print('Lista somente com números impares:', lista_impar)
