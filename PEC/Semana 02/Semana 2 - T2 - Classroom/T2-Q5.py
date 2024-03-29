km_marte = float(input('Quantos quilômetros até Marte: '))
km_por_hr = float(input('Quantos Km/hora sua nave espacial pode viajar: '))
tempo = km_marte / km_por_hr
print(f'Você levaria {tempo:.2f} horas para chegar a Marte!')
