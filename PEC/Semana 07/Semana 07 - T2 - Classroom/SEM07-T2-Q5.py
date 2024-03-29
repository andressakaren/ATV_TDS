# Escreva um programa que leia três números por parâmetro e mostre na tela em ordem crescente.

def func_comparacao(n1, n2, n3):
    v1 = max(n1, n2, n3)
    v3 = min(n1, n2, n3)
    v2 = (n1 + n2 + n3) - (v1 + v3)
    return (f'{v3}\n{v2}\n{v1}')

def main():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = int(input('Digite o terceiro número: '))

    print(f'''A ordem crescente dos números digitados é: \n{func_comparacao(n1, n2, n3)}.''')

if __name__ == '__main__':
    main()
