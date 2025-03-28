# Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por
# sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize
# uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
# número, também do tipo inteiro.

def calc_fatorial(n):
    mult_fatorial = 1
    for i in range(1, n + 1):
        mult_fatorial *= i 
    return mult_fatorial


while True:
    try:
        numero = int(input('Digite o número: '))
        if numero >= 0:
            print(f'O fatorial do número {numero} é: {calc_fatorial(numero)}')
            break
        print('Numero inválido.')
    except:
        print('valor inválido. Digite um valor válido.')
