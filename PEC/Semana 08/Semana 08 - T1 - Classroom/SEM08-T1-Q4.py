def media_numeros(n1, n2, n3, n4, n5):
    media = (n1 + n2 + n3 + n4 + n5) / 5
    print(f'{media}')    
    if n1 > media:
        print(f'{n1}')    
    if n2 > media:
        print(f'{n2}')       
    if n3 > media:
        print(f'{n3}')       
    if n4 > media:
        print(f'{n4}')       
    if n5 > media:
        print(f'{n5}')     
    
    
def main():
    n2 = int(input('Digite o primeiro número: '))
    n3 = int(input('Digite o segundo número: '))
    n1 = int(input('Digite o terceiro número: '))
    n4 = int(input('Digite o quarto número: '))
    n5 = int(input('Digite o quinto número: ')) 
    
    print(f'O valor da média e os números maiores que ela são: ')  
    media_numeros(n1, n2, n3, n4, n5)

if __name__ == '__main__':
    main()


