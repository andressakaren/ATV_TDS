# 7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
# outro valor dado pertence ou não à lista.


def ler_lista():
    lista = []
    count = 0
    while count < 5:
        try:
            valor = float(input(f"Digite o {count+1}° valor da lista: "))
            lista.append(valor)
            count += 1
        except ValueError:
            print("Valor inválido. Tente novamente.")
    return lista

def contem_lista(valor, lista):
    if valor in lista:
        return f'Esse valor pertence a lista: {lista}'
    else:
        return f'Esse valor NÃO pertence a lista: {lista}'
    
lista = ler_lista()
# print(lista)

while True:
    try:
        num = float(input(f"Digite o valor que deseja verificar se pertence a lista: "))
        print(contem_lista(num, lista))     
        break
    except ValueError:
        print("Valor inválido. Tente novamente.")