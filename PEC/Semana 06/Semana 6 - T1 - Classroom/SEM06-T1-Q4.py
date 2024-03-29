def maior_num(n1, n2, n3, n4, n5):
    return max(n1, n2, n3, n4, n5)
    
def menor_num(n1, n2, n3, n4, n5):
    return min(n1, n2, n3, n4, n5)
    
def media_num(n1, n2, n3, n4, n5):    
    return (n1 + n2 + n3 + n4 + n5) / 5

def main():   
    n1 = int(input('Digite o valor do primeiro número: '))
    n2 = int(input('Digite o valor do segundo número: '))
    n3 = int(input('Digite o valor do terceiro número: '))
    n4 = int(input('Digite o valor do quarto número: '))
    n5 = int(input('Digite o valor do quinto número: '))

    print(f'O maior número é: {maior_num(n1, n2, n3, n4, n5)}.')
    print(f'O menor número é: {menor_num(n1, n2, n3, n4, n5)}.')
    print(f'A média entre os números digitados é: {media_num(n1, n2, n3, n4, n5)}.')

if __name__ == '__main__':
    main()