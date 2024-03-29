altura = int(input())
comprimento = int(input())
largura = int(input())

area_piso = largura * comprimento
volume_sala = largura * comprimento * altura
area_parede = 2 * altura * largura + 2 * altura * comprimento

print(f'{area_piso}')
print(f'{volume_sala}')
print(f'{area_parede}')