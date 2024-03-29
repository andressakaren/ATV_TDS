# 1 ano terrestre = 0.5 ano espacial
from math import trunc

def convert_(idade):
    return trunc(idade * 0.5)

def main():
    idade = int(input('Digite a idade que deseja converder para ano espacial: '))
    print(f'A idade {idade} em anos terrestres corresponde a {convert_(idade)} em anos espaciais.')
    
if __name__ == '__main__':
    main()
    