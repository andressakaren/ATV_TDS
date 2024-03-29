print('Digite sua idade expressa em anos, meses e dias.')
anos = int(input('Digite o valor em anos: '))
meses = int(input('Digite o valor em meses: '))
dias = int(input('Digite o valor em dias: '))

anos_dias = anos * 365
meses_dias = meses * 30
total = meses_dias + anos_dias + dias

print(f'Sua idade expressa apenas em dias é {total}. *Considerando sempre os anos com 365 dias e os messes com 30 dias.')