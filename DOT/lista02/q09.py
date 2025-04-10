# 9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.

def ler_lista():
    lista_X = []
    lista_Y = list(range(5))
    count = 0
    count_lista_y = 4
    while count < 5:
        try:
            valor = float(input(f"Digite o {count+1}° valor da lista: "))
            lista_X.append(valor)
            lista_Y[count_lista_y] = valor
            count_lista_y -= 1
            count += 1
        except ValueError:
            print("Valor inválido. Insira um valor numérico.")
    return lista_X, lista_Y

x, y = ler_lista()
print('Lista X',x)
print('Lista Y',y)

