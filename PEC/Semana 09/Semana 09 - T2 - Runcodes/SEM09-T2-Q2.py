def separar_numero(numero):
    if 0 < numero < 1000:
        u = numero % 10
        numero //= 10
        d = numero % 10
        numero //= 10
        c = numero % 10
    return c, d, u

def centenas(c):
    if c == 1:
        qntd = 'uma centena'
    elif c == 2:
        qntd = 'duas centenas'
    elif c == 3:
        qntd = 'três centenas'
    elif c == 4:
        qntd = 'quatro centenas'
    elif c == 5:
        qntd = 'cinco centenas'
    elif c == 6:
        qntd = 'seis centenas'
    elif c == 7:
        qntd = 'sete centenas'
    elif c == 8:
        qntd = 'oito centenas'
    else:
        qntd = 'nove centenas'
    return qntd

def dezenas(d):
    if d == 1:
        qntd = 'uma dezena'
    elif d == 2:
        qntd = 'duas dezenas'
    elif d == 3:
        qntd = 'três dezenas'
    elif d == 4:
        qntd= 'quatro dezenas'
    elif d == 5:
        qntd = 'cinco dezenas'
    elif d == 6:
        qntd = 'seis dezenas'
    elif d == 7:
        qntd = 'sete dezenas'
    elif d == 8:
        qntd = 'oito dezenas'
    else:
        qntd = 'nove dezenas'
    return qntd

def unidades(u):
    if u == 1:
        qntd = 'uma unidade'
    elif u == 2:
        qntd = 'duas unidades'
    elif u == 3:
        qntd = 'três unidades'
    elif u == 4:
        qntd = 'quatro unidades'
    elif u == 5:
        qntd = 'cinco unidades'
    elif u == 6:
        qntd = 'seis unidades'
    elif u == 7:
        qntd = 'sete unidades'
    elif u == 8:
        qntd = 'oito unidades'
    else:
        qntd = 'nove unidades'
    return qntd
    
def main():
    numero = int(input())
    cen, dez, un = separar_numero(numero)
    
    
    if cen > 0 and dez > 0 and un > 0:
        print(f'{centenas(cen)}, {dezenas(dez)} e {unidades(un)}.')
    elif cen == 0 and dez == 0 and un > 0:
        print(f'{unidades(un)}.')
    elif cen == 0 and dez > 0 and un == 0:
        print(f'{dezenas(dez)}.')
    elif cen > 0 and dez == 0 and un == 0:
        print(f'{centenas(cen)}.')
    elif cen == 0 and dez > 0 and un > 0:
        print(f'{dezenas(dez)} e {unidades(un)}.')
    elif cen > 0 and dez > 0 and un == 0:
        print(f'{centenas(cen)} e {dezenas(dez)}.')
    elif cen > 0 and dez == 0 and un > 0:
        print(f'{centenas(cen)} e {unidades(un)}.')

if __name__ == "__main__":
    main()