def identificador(numero):
    return not numero % 2 == 0

def main():
    numero = int(input('Digite um número: '))
    
    print(f'Esse número é ímpar? R: {identificador(numero)}')
    
if __name__ == '__main__':
    main()
