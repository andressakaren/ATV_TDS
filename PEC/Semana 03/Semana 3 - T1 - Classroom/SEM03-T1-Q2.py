# Desenvolva um programa que pergunte a distância até um planeta em quilômetros e a velocidade da nave em km/h.
# Informe quantos dias e quantas horas a viagem levará, considerando 24 horas por dia.
dist_km = float(input('Quantos quilômetros tem até o planeta escolhido? '))
veloc_km_h = float(input('Qual a velocidade que sua nave pode viajar, em Km/h? '))
tempo_h = dist_km / veloc_km_h
tempo_dias = int(tempo_h // 24)
tempo_rest_horas = int(tempo_h % 24)

print(f'A sua viagem levará {tempo_dias} dias e {tempo_rest_horas} horas.')
