def ler_10_elementos():
    count = 0
    lista_X = []
    while count < 10:
        try: 
            n = int(input(f'Digite o {count + 1}° número: '))
            lista_X.append(n)
            count += 1
        except ValueError:
            print('Digite um número válido!')
    return lista_X

def lista_Y(listaX):
    lista_Y = []
    for i in range(10):
        if listaX[i] % 2 == 0: # par
            lista_Y.append((listaX[i]) / 2)
        else:
            lista_Y.append((listaX[i]) * 3)
    return lista_Y
      
def main():
    listaX = ler_10_elementos()
    listaY = lista_Y(listaX)
    print(listaX)
    print(listaY)
    
if __name__ == "__main__":
    main()
                    
        