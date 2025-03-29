# 12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.

'''
10 
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
'''

def somatorio(valor):
    count = 0
    for i in range(1, valor + 1):
        count += i
    return count


# inteiro e positivo
while True:
    try:
        n = int(input('Digite um numero inteiro positivo: '))
        if n > 0:
            break
        print('Numero deve ser maior que zero!')
    except ValueError:
        print('Digite um numero válido!')


print('Número:',n)
print('Somatório:',somatorio(n))