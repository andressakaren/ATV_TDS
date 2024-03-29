def identificador(numero):
    return not numero % 2 == 0

def main():
    numero = int(input())
    
    print(f'{identificador(numero)}')
    
if __name__ == '__main__':
    main()
