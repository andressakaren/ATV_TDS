# 11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.

'''
para saber o numero de divisores dá pra testar de 1 ate o proprio numero, se o resto da divisao for zero, entao aquele numero pelo qual estamos tentando dividir é divisor desse valor. ex:
numero 10 
i começando por 1
10 % 1 = 0  --> count += 1
10 % 2 = 0  --> count += 1
10 % 3 != 0
10 % 4 != 0
10 % 5 = 0  --> count += 1
10 % 6 != 0
10 % 7 != 0
10 % 8 != 0
10 % 9 != 0
10 % 10 = 0 --> count += 1
'''

def numeroDivisores(valor):
    count = 0
    for i in range(1, valor + 1):
        if valor % i == 0:
            count += 1
    return count
    

# inteiro e positivo
while True:
    try:
        n = int(input('Digite um numero inteiro: '))
        if n > 0:
            break
        print('Numero deve ser maior que zero!')
    except:
        print('Digite um numero válido!')
        
print('Número:',n)
print('Quantidade de divisores:',numeroDivisores(n))