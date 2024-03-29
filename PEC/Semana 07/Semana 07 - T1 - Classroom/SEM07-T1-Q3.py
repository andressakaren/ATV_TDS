def mensagem(cor_sinal):
    if cor_sinal.upper() == 'V':
        return 'Siga'
    elif cor_sinal.upper() == 'A':
        return 'Atenção'
    elif cor_sinal.upper() == 'E':
        return 'Pare'

def main():
    cor_sinal = str(input('''As cores do sinal de trânsito são:
Verde, digite “V” ;
Amarelo, digite “A” ;
Vermelho, digite “E” ;
Qual a cor você deseja saber o significado: ''')).strip().upper()
    print(f'A cor referente a inicial {'"'}{cor_sinal}{'"'} é {mensagem(cor_sinal)}!!')
    
if __name__ == '__main__':
    main()
