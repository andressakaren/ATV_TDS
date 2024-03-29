def numero_inverso(num_digitado):
    d1 = num_digitado // 1000
    d2 = (num_digitado % 1000) // 100
    d3 = (num_digitado % 100) // 10
    d4 = (num_digitado % 10) // 1
    return (d4 * 1000) + (d3 * 100) + (d2 * 10) + d1

numero = int(input('Digite um valor inteiro entre 1000 e 9999: '))
num_inverso = numero_inverso(numero)
print(f'O número {numero} na ordem inversa é {num_inverso}.')
