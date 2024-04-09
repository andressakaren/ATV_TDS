def msg(n1, n2, n3):
    if (n1 != n2 and n1 != n3 and n2 != n3):
        return 'Todos os valores são diferentes' 
    else:
        return 'Todos os valores são iguais' if (n1 == n2 == n3) else 'Existem dois valores iguais e um diferente'
      
def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    
    print(f'{msg(n1, n2, n3)}')
    
if __name__ == '__main__':
    main()