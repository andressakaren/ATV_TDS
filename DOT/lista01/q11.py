# 11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.

def numeroDivisores(valor):
    ...

# inteiro e positivo
while True:
    try:
        n = int(input('Digite um numero inteiro: '))
        if n > 0:
            break
        print('Numero deve ser maior que zero!')
    except:
        print('Digite um numero válido!')
        
print(n)