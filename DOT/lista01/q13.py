# 13. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.

def func_S(valor):
    soma = 0 
    for i in range(1, valor + 1):
        soma += 1/i
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
print('Somatório:',func_S(n))