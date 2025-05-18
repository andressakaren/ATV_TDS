# 9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.

# considerar n2 > n1, deve tratar essa condição (prof falou)
def soma_intervalo(n1, n2):
    soma = 0
    for i in range(n1, n2 + 1):
        soma += i
    return soma

def ler_inteiros():
    while True:
        try:
            n1 = int(input('Digite o primeiro numero: '))
            n2 = int(input('Digite o segundo numero: '))

            if n2 > n1 and n1 >= 0 and n2 >= 0:
                return n1, n2

            print('Os valores devem ser diferentes de zero e o segundo numero maior que o primeiro!')
        except:
            print('Digite um valor válido!')
            
def main():
    n1, n2 = ler_inteiros()

    print(
        f'A soma de todos os números inteiros contidos no intervalo [{n1},{n2}] = {soma_intervalo(n1, n2)}.')

if __name__ == "__main__":
    main()