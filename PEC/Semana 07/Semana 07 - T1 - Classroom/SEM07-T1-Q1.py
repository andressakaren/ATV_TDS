def identificador(sexo):
    if sexo.upper() == '1':
        return 'Ilmo Sr.'
    else:
        return 'Ilma Sra.'

def main():
    nome = str(input('Digite seu nome: ')).strip()
    sexo = str(input('Digite 1 para Masculino, 2 para Feminino: ')).strip()
    
    print (f'Olá, {identificador(sexo)} {nome}!')
    
if __name__ == '__main__':
    main()
