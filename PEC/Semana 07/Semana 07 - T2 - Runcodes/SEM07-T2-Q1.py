def func_definicao(nome, estado_civil):
    if estado_civil == '1':
        nome_conjuge = str(input()).strip()
        return len(nome) + len(nome_conjuge)
    if estado_civil == '2':
        return len(nome)
    
def main():
    nome = str(input()).strip()
    estado_civil = str(input()).strip()
    print(f'{func_definicao(nome, estado_civil)}')

if __name__ == '__main__':
    main()

    
