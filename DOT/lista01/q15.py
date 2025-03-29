# 15. Escreva uma função que recebe por parâmetro um valor inteiro e positivo t e retorna o valor de S.
# S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)


def func_S(valor):
    soma = 0  
   
    for i in range(1, valor + 1): 
        termo = (i**2 + 1) / (i + 3) 
        soma += termo 

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