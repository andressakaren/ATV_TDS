def mensagem(cor_sinal):
    if cor_sinal.upper() == 'V':
        return 'Siga'
    elif cor_sinal.upper() == 'A':
        return 'Atenção'
    elif cor_sinal.upper() == 'E':
        return 'Pare'

def main():
    cor_sinal = str(input()).strip()
    print(f'{mensagem(cor_sinal)}')
    
if __name__ == '__main__':
    main()
