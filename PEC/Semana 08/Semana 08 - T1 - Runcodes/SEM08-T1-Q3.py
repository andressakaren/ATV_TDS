def maior_numero(n1, n2, n3, n4, n5):
    maior = n1
    if n2 > maior: 
        maior = n2
    if n3 > maior: 
        maior = n3
    if n4 > maior: 
        maior = n4
    if n5 > maior: 
        maior = n5
    return maior

def menor_numero(n1, n2, n3, n4, n5):
    menor = n1
    if n2 < menor: 
        menor = n2
    if n3 < menor: 
        menor = n3
    if n4 < menor: 
        menor = n4
    if n5 < menor: 
        menor = n5
    return menor

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())
    
    print(f'{maior_numero(n1, n2, n3, n4, n5)}\n{menor_numero(n1, n2, n3, n4, n5)}')
    
if __name__ == '__main__':
    main()
