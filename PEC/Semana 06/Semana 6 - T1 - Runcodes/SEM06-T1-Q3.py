def horas_min_seg(segundos):
    horas = segundos // 3600
    segundos = segundos % 3600
    min = segundos // 60
    segundos = segundos % 60
    seg = segundos
    return (f'{horas}:{min}:{seg}')
def main():
    segundos = int(input())
    print(f'{horas_min_seg(segundos)}')
if __name__ == '__main__':
    main()
    