def eVogal(caractere):
    return caractere.upper() in 'AEIOU' 

def eLetra(caractere):
    return 'A' <= caractere.upper() <= 'Z' 

def comparacao(caractere):
    return eLetra(caractere) and not eVogal(caractere)

def main():
    caractere = input('Digite um caractere? ').strip()
    print(f'Esse caractere é uma Consoante? {comparacao(caractere)}.')
    
if __name__ == '__main__':
    main()