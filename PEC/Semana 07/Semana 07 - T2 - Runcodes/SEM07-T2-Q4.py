def comparar_mes(dia_nascimento, mes_nascimento):
    if mes_nascimento == 1 and 20 <= dia_nascimento <= 30 or mes_nascimento == 2 and 1 <= dia_nascimento <= 18: 
        return 'Aquário'  
    
    if mes_nascimento == 2 and 19 <= dia_nascimento <= 30 or mes_nascimento == 3 and 1 <= dia_nascimento <= 20: 
        return 'Peixes'
    
    if mes_nascimento == 3 and 21 <= dia_nascimento <= 30 or mes_nascimento == 4 and 1 <= dia_nascimento <= 19: 
        return 'Áries'
    
    if mes_nascimento == 4 and 20 <= dia_nascimento <= 30 or mes_nascimento == 5 and 1 <= dia_nascimento <= 20:
        return 'Touro'
    
    if mes_nascimento == 5 and 21 <= dia_nascimento <= 30 or mes_nascimento == 6 and 1 <= dia_nascimento <= 21: 
        return 'Gêmeos'
    
    if mes_nascimento == 6 and 22 <= dia_nascimento <= 30 or mes_nascimento == 7 and 1 <= dia_nascimento <= 22:
        return 'Câncer'
    
    if mes_nascimento == 7 and 23 <= dia_nascimento <= 30 or mes_nascimento == 8 and 1 <= dia_nascimento <= 22:
        return 'Leão'
    
    if mes_nascimento == 8 and 23 <= dia_nascimento <= 30 or mes_nascimento == 9 and 1 <= dia_nascimento <= 22:
        return 'Virgem'
    
    if mes_nascimento == 9 and 23 <= dia_nascimento <= 30 or mes_nascimento == 10 and 1 <= dia_nascimento <= 22: 
        return 'Libra'
    
    if mes_nascimento == 10 and 23 <= dia_nascimento <= 30 or mes_nascimento == 11 and 1 <= dia_nascimento <= 21:
        return 'Escorpião'
    
    if mes_nascimento == 11 and 22 <= dia_nascimento <= 30 or mes_nascimento == 12 and 1 <= dia_nascimento <= 21:
        return 'Sagitário'
    
    if mes_nascimento == 12 and 22 <= dia_nascimento <= 30 or mes_nascimento == 1 and 1 <= dia_nascimento <= 19:
        return 'Capricórnio'

def main():
    dia_nascimento = int(input())
    mes_nascimento = int(input())
    print(f'{comparar_mes(dia_nascimento, mes_nascimento)}')

if __name__ == '__main__':
    main()
