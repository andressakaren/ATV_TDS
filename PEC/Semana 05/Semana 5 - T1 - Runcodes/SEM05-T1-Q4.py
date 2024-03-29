def horas_e_minutos(minutos):
    h = minutos // 60
    m = minutos % 60
    return h, m

min = int(input())
horas, minutos = horas_e_minutos(min)
print(f'{horas}:{minutos}')
