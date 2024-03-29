def eVogal(caractere):
    return caractere.upper() in 'AEIOU'
 
def main():
    caractere = input('Digite um caractere? ').strip()
    print(f'Esse caractere é uma vogal? {eVogal(caractere)}.')
    
if __name__ == '__main__':
    main()