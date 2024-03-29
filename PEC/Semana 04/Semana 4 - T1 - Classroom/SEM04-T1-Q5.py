altura = int(input('Digite o valor da altura da sua sala, em metros: '))
comprimento = int(input('Digite o valor da comprimento, referente a uma das paredes da sua sala, em metros: '))
largura = int(input('Digite o valor do largura, referente a parede lateral à citada anteriormente, em metros: '))

area_piso = largura * comprimento
volume_sala = largura * comprimento * altura
area_parede = 2 * altura * largura + 2 * altura * comprimento

print(f'A área do piso da sala de {largura}m de largura e {comprimento}m comprimento é igual a {area_piso}m².')
print(f'O volume da sala de {largura}m de largura, {comprimento}m de comprimento e {altura}m de altura é igual a {volume_sala}m³.')
print(f'A área das paredes da sala é dado pela fórmula 2 * altura * largura + 2 * altura * comprimento e é igual a {area_parede}m².')
