def e_vogal(caractere):
    if caractere.upper() in 'AEIOU':
        return 'vogal'
    
    if 'A' <= caractere.upper() <= 'Z':
        return 'consoante'
    
    if caractere in '0123456789':
        return 'número'
    
    else:
        return 'símbolo'

def main():
    caractere = str(input())
    print(f'{e_vogal(caractere)}')
    
if __name__ == '__main__':
    main()
    