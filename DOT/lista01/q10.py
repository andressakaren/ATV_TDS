# 10. Escreva um programa composto de uma função Max e o programa principal como segue:
# a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um deles;
# b) O programa principal lê 4 séries de 2 números a, b. Para cada série lida imprime o maior dos dois números usando a função Max.

# fazer a logica depois pra nao usar função q já exite
def max_(a, b, c, d):
    maior = a 
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    if d > maior:
        maior = d
    return maior

# receber 2 numeros INTEIROS em 4 series
def ler_serie(): 
    while True:
        try:
            n1 = int(input('Digite o primeiro numero: '))
            n2 = int(input('Digite o segundo numero: '))
            n3 = int(input('Digite o terceiro número: '))
            n4 = int(input('Digite o quarto número: '))
            return n1, n2, n3, n4
        except:
            print('Digite um valor válido!')
            
            
# programa principal
lista_final = [] 
for i in range(4):
    n1, n2, n3, n4 = ler_serie()
    maior = max_(n1, n2, n3, n4)
    lista_final.append(maior)
    print(f'O maior entre {n1}, {n2}, {n3} e {n4} = {maior}')

print('Lista dos maiores números de cada série: ', lista_final)
print(f'O maior valor entre os maiores: {max_(lista_final[0],lista_final[1],lista_final[2],lista_final[3],)}')