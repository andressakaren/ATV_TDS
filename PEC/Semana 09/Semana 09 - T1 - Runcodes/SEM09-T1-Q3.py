def eh_quadrado(base, altura):
    if base == altura:
        return 'QUADRADO'
    else:
        perimetro = (base * 2) + (altura * 2)
        area = base * altura
        return (f'{perimetro:.0f} - {area:.0f}') 

def main():
    base = int(input())
    altura = int(input())
    
    print(f'{eh_quadrado(base, altura)}')
    
if __name__ == '__main__':
    main()