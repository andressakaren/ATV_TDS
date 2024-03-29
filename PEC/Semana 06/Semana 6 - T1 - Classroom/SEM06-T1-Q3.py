def horas_min_seg(segundos):
    horas = segundos // 3600
    segundos = segundos % 3600
    min = segundos // 60
    segundos = segundos % 60
    seg = segundos
    return (f'{horas}:{min}:{seg}')

def main():
    segundos = int(input('Digite o tempo de duração de um evento em segundos: '))
    
    print(f'O tempo {segundos} segundos é equivalente a {horas_min_seg(segundos)}.')
    
if __name__ == '__main__':
    main()
    