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
    numero = int(input())
    n = 0
    print(f'{e_par(numero, n)}')
    
if __name__ == '__main__':
    main()
