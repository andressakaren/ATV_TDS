dividendo = float(input('Digite o valor do dividendo: '))
divisor = float(input('Digite o valor do divisor: '))

quociente = dividendo // divisor
resto = dividendo % divisor

print(f'O número {dividendo} dividido por {divisor}')
print(f'é igual a {quociente:.4f} e o resto {resto:.4f}.')
