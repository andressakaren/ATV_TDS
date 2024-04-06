def idade_em_anos(dia_atual, mes_atual, ano_atual, dia_nasci, mes_nasci, ano_nasci):
    if mes_atual <= mes_nasci and dia_atual < dia_nasci:
        return (ano_atual - ano_nasci) - 1
    else: 
        return (ano_atual - ano_nasci)
    
def main():
    dia_atual = int(input('Digite o dia atual: '))
    mes_atual = int(input('Digite o mês atual: '))
    ano_atual = int(input('Digite o ano atual: '))
    dia_nasci = int(input('Digite o dia do nascimento: '))
    mes_nasci = int(input('Digite o mês do nascimento: '))
    ano_nasci = int(input('Digite o ano do nascimento: '))
    
    print(f'Na data de atual você tem: {idade_em_anos(dia_atual, mes_atual, ano_atual, dia_nasci, mes_nasci, ano_nasci)} anos.')
    
if __name__ == '__main__':
    main()
