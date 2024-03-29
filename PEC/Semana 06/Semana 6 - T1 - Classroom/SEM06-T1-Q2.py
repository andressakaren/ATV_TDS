def codigo_numerico(caractere):
    return ord(caractere)

def main():
    caractere = input('Digite um único e qualquer caractere pelo teclado: ')
    
    print(f'/o código numérico do {caractere}, é {codigo_numerico(caractere)}.')
    
if __name__ == '__main__':
    main()
    