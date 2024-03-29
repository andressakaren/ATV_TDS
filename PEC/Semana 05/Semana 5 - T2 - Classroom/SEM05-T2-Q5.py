def eNum(caractere):
    return caractere in '0123456789' 

def eLetra(caractere):
    return 'A' <= caractere.upper() <= 'Z' 

def comparacao(caractere):
    return not eLetra(caractere) and not eNum(caractere)

def main():
    caractere = input('Digite um caractere? ').strip()
    print(f'Esse caractere é um símbolo? {comparacao(caractere)}.')
    
if __name__ == '__main__':
    main()