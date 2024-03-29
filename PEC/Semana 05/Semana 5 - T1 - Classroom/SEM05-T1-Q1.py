def calcular (a, b, c):
    return 2 * a + 5 * b - c

x = int(input('Digite o primeiro valor (a): '))
y = int(input('Digite o segundo valor (b): '))
z = int(input('Digite o terceiro valor (c): '))
valores = calcular(x, y, z)
print(f'O resultado da função 2 * a + 5 * b - c é: {valores}. ')
