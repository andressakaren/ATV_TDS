def e_par(numero, n):
    if (numero % 10) % 2 != 0:
        n += 1
    numero = numero // 10
    
    if numero % 2 != 0:
        n += 1
        
    if n == 0:
        return 'Nenhum dígito é ímpar.'
    
    if n == 1:
        return 'Apenas um dígito é ímpar.'
    
    else:
        return 'Os dois dígitos são ímpares.'
         

def main():
    numero = int(input())
    n = 0
    print(f'{e_par(numero, n)}')
    
if __name__ == '__main__':
    main()
    