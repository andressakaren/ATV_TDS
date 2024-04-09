def qual_dia(dia):
    if dia == 1:
        return 'domingo'
    if dia == 2:
        return 'segunda-feira'        
    if dia == 3:
        return 'terça-feira'
    if dia == 4:
        return 'quarta-feira'       
    if dia == 5:
        return 'quinta-feira'        
    if dia == 6:
        return 'sexta-feira'       
    if dia == 7:
        return 'sábado'
    else:
        return ValueError('valor inválido')

def main():
    dia = int(input())
    
    print(f'{qual_dia(dia)}')
    
if __name__ == '__main__':
    main()  