# 14. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.

# S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!

def func_S(valor):
    soma = 1  
    fatorial = 1 
    
    for i in range(1, valor + 1): 
        fatorial *= i 
        soma += 1 / fatorial 

    return round(soma, 2)

# inteiro e positivo
while True:
    try:
        n = int(input('Digite um número inteiro positivo: '))
        if n > 0:
            break
        print('Número deve ser maior que zero!')
    except ValueError:
        print('Digite um número inteiro válido!')


print('Número:',n)
print('Valor de S:',func_S(n))   