def data(dia_1, mes_1, ano_1, dia_2, mes_2, ano_2):
    if ano_1 > ano_2:
        return f'{dia_1}/{mes_1}/{ano_1}'
    
    elif ano_1 == ano_2 and mes_1 >= mes_2 and dia_1 >= dia_2:
        return f'{dia_1}/{mes_1}/{ano_1}'
    
    else:
        return f'{dia_2}/{mes_2}/{ano_2}'
        
                    
def main():
    dia_1 = int(input('Digite o dia 1: '))
    mes_1 = int(input('Digite o mês 1: '))
    ano_1 = int(input('Digite o ano 1: '))
    dia_2 = int(input('Digite o dia 2: '))
    mes_2 = int(input('Digite o mês 2: '))
    ano_2 = int(input('Digite o ano 2: '))

    print(f'A data mais recente é: {data(dia_1, mes_1, ano_1, dia_2, mes_2, ano_2)}')

if __name__ == '__main__':
    main()
