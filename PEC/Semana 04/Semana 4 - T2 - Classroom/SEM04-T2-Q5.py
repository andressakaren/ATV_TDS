n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
n3 = float(input('Digite a sua terceira nota: '))

media_ponderada = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10

print(f'A média final é feita pela média ponderada das notas. Sua média final é: {media_ponderada:.2f}.')