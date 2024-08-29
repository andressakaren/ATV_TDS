def ler_valores(n):
    lista = []
    for i in range(n):
        valor = input(f'Digite o {i + 1}° número: ').strip()
        lista.append(valor)
    return lista

def esta_ordenada(lista, lista_ordenada):
    return lista == lista_ordenada

def main():
    n = int(input('Digite o valor da constante: '))
    lista = ler_valores(n)
    lista_ordenada = sorted(lista)
    conferencia = esta_ordenada(lista, lista_ordenada)
    
    if conferencia:
        print('LISTA ORDENADA')
    else:
        print('LISTA NÃO ORDENADA')

if __name__ == '__main__':
    main()