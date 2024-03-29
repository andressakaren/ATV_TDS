def horas_e_minutos(minutos):
    h = minutos // 60
    m = minutos % 60
    return h, m

min = int(input('Digite uma quantidade em mminutos: '))
horas, minutos = horas_e_minutos(min)
print(f'{min} minutos é equivalente a {horas} horas e {minutos} minutos.')
