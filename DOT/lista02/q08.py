# 8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes ocorreu a letra ‘A’.
# OBS: Fazer crítica na entrada do caractere para aceitar somente letras.
# Raise para 'obrigar' o except lançar o erro

from string import ascii_letters

def lista_letras(n):
    lista = []
    count = 0
    total = 0
    while count < n:
        try:
            valor = input(f"Digite a {count+1}° letra da lista: ").strip().upper()
            if valor not in ascii_letters or len(valor) != 1:
                raise ValueError
            lista.append(valor)
            count += 1
            if valor == 'A':
                total += 1
        except ValueError:
            print("Valor inválido. Digite apenas uma letra.")
    return lista, total


lista, total = lista_letras(10)
print('\nNa lista:', lista)
print('A quantidade de vezes que a letra "A" foi inserida:', total)
