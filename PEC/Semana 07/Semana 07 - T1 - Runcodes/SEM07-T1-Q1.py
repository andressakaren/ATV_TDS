def identificador(sexo):
    if sexo.upper() == '1':
        return 'Ilmo Sr.'
    else:
        return 'Ilma Sra.'

def main():
    nome = str(input()).strip()
    sexo = str(input()).strip()
    
    print (f'{identificador(sexo)} {nome}')
    
if __name__ == '__main__':
    main()
