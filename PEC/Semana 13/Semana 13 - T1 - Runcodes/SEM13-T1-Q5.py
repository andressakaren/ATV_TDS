# Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir uma lista C de 50 elementos, cujos elementos sejam a intercalação dos elementos de A e B.
def lista_a(n):
    lista_a = []
    for i in range(n):
        num = int(input())
        lista_a.append(num)
    return lista_a

def lista_b(n):
    lista_b = []
    for i in range(n):
        num = int(input())
        lista_b.append(num)
    return lista_b
            
def main():
    lista_C = []
    lista_A = lista_a(2)
    lista_B = lista_b(2)
    
    for i in range(4):
        if i == 0:
            lista_C.insert(i, lista_A[i])
        # else: 
        #     if i % 2 != 0:
        #         lista_C.insert(i, lista_A[i])
        #     else:    
        #         lista_C.insert(i, lista_B[i])
                
        # elif i % 2 != 0:
        #     lista_C.insert(i, lista_B[i])
        # else:
        #     lista_C.insert(i, lista_A[i])
    print(lista_A)
    print(lista_B)
    print(lista_C)
if __name__ == '__main__':
    main()