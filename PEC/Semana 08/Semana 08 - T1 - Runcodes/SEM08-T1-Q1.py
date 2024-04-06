def idade_em_anos(dia_atual, mes_atual, ano_atual, dia_nasci, mes_nasci, ano_nasci):
    if mes_atual <= mes_nasci and dia_atual < dia_nasci:
        return (ano_atual - ano_nasci) - 1
    else: 
        return (ano_atual - ano_nasci)
    
def main():
    dia_atual = int(input())
    mes_atual = int(input())
    ano_atual = int(input())
    dia_nasci = int(input())
    mes_nasci = int(input())
    ano_nasci = int(input())
    
    print(f'{idade_em_anos(dia_atual, mes_atual, ano_atual, dia_nasci, mes_nasci, ano_nasci)}')
    
if __name__ == '__main__':
    main()