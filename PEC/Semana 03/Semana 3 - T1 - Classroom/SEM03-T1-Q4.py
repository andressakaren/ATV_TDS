tempo_seg = int(input('Insira um número em segundos: '))
tempo_min = tempo_seg // 60
resto_divisao = tempo_seg % 60
print(f'O valor é {tempo_min} min e {resto_divisao} segundos.')

