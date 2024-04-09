def menor_diferenca(n1, n2, n3):
    if abs(n1 - n2) < abs(n1 - n3):
        return abs(n1 - n2)
    else:
        return abs(n1 - n3)


def main():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = int(input('Digite o terceiro número: '))
    
    print(f'A menor diferença é a de {menor_diferenca(n1, n2, n3)}.')
    
if __name__ == '__main__':
    main()