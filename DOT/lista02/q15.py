# 15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim por diante. Escrever todo a lista D e todo a lista E.

# mesma lógica da q9

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
print('Lista D',x)
print('Lista E',y)