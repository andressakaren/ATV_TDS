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
    numero = int(input('Digite um número de 10 a 99: '))
    n = 0
    print(f'O número {numero} tem {e_par(numero, n)}')
    
if __name__ == '__main__':
    main()
    
