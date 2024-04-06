def peso_ideal(altura, genero):
    if genero == 1:
       p_i = (72.7 * altura) - 58
    if genero == 2:
       p_i = (62.1 * altura) - 44.7
    return f'{p_i:.2f}'

def main():
    altura = float(input('Digite a altura: '))
    genero = int(input('Digite (1) - Homens e (2) - Mulheres'))
    
    print(f'O resultado do peso ideal é: {peso_ideal(altura, genero)}')
    
if __name__ == '__main__':
    main()
    
