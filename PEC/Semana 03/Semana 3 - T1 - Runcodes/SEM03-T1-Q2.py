dist_km = float(input())
veloc_km_h = float(input())
tempo_h = int(dist_km / veloc_km_h)
tempo_dias = int(tempo_h // 24)
tempo_rest_horas = int(tempo_h % 24)

print(f'{tempo_dias} dias e {tempo_rest_horas} horas')
