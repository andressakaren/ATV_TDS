def condicoes(num, resto):
    if resto == 0:
        return (9 * num) + 7
    elif resto == 1:
        return 'par' if num % 2 == 0 else 'ímpar'
    elif resto == 2:
        return (5 * num**2) - (3*num) + 42
    elif resto == 3:
        return num // 10
    elif resto == 4:
        return num**2
def main():
    num = int(input('Digite um número: '))
    
    resto = num % 5
    
    print(f'O total da ação executada: {condicoes(num, resto)}.')
    
if __name__ == '__main__':
    main()