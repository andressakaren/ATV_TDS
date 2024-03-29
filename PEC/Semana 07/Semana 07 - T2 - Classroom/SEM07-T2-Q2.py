def e_par(numero, n):
    if (numero % 10) % 2 == 0:
        n = 1
    
    numero = numero // 10 
                
    if (numero % 10) % 2 == 0:
        n = n + 1
        
    numero = numero // 10
    
    if numero > 0:    
        if numero % 2 == 0: 
            n = n + 1 
        
    return n
     
def main():
    numero = int(input('Digite um número entre 100 e 999: '))
    n = 0
    print(f'O número {numero} tem {e_par(numero, n)} dígito(s) par(es).')
    
if __name__ == '__main__':
    main()
  
