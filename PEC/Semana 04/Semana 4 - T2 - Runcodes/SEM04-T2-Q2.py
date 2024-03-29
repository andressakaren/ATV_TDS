anos = int(input())
meses = int(input())
dias = int(input())

anos_dias = anos * 365
meses_dias = meses * 30
total = meses_dias + anos_dias + dias

print(f'{total}')