# 8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
# ocorreu a letra ‘A’.
# OBS: Fazer crítica na entrada do caractere para aceitar somente letras.

## (incompleta)

def lista_letras(n):
    lista = []
    count = 0
    total = 0
    while count < n:
        try:
            valor = str(
                input(f"Digite a {count+1}° letra da lista: ")).strip().upper()
            lista.append(valor)
            count += 1
            if valor == 'A':
                total += 1
        except ValueError:
            print("Valor inválido. Tente novamente.")
    return lista, total


lista, total = lista_letras(5)
print('A lista:', lista)
print('A quantidade de vezes que a letra "A" foi inserida:', total)
