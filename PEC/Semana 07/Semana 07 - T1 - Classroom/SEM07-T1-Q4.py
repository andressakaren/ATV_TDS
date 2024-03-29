def e_oque(caractere):
    if caractere.upper() in 'AEIOU':
        return 'vogal'
    
    if 'A' <= caractere.upper() <= 'Z':
        return 'consoante'
    
    if caractere in '0123456789':
        return 'número'
    
    else:
        return 'símbolo'

def main():
    caractere = str(input('Digite um caractere: '))
    print(f'O caractere digitado é um(a): {e_oque(caractere)}.')
    
if __name__ == '__main__':
    main()
    