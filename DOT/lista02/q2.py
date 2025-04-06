# 2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos dessa lista.

def eh_positivo(valor):
    return valor >= 0

def ler_10_num():
    count = 0
    soma = 0
    lista_negativos = []
    lista_positivos = []
    while count < 10:
        try:
            n = float(input(f'Digite o {count + 1}° valor: '))
            if eh_positivo(n):
                if n not in lista_positivos:
                    lista_positivos.append(n)
                    soma += n
            else:
                if n not in lista_negativos:
                    lista_negativos.append(n)
            count += 1
        except:
            print('Digite um número válido!')
    return lista_negativos, lista_positivos, soma

lista_negativos, lista_positivos, soma = ler_10_num()
print(f'Lista números negativos: {lista_negativos}')
print(f'Quantidade de números negativos: {len(lista_negativos)}')
print(f'Lista números positivos: {lista_positivos}')
print(f'Soma dos números positivos: {soma}')