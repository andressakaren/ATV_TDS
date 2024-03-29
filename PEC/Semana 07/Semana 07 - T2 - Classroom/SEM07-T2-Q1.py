def func_definicao(nome, estado_civil):
    if estado_civil == '1':
        nome_conjuge = str(input('Digite o nome do cônjuge: ')).strip()
        return len(nome) + len(nome_conjuge)
    if estado_civil == '2':
        return len(nome)
    
def main():
    nome = str(input('Digite seu nome: ')).strip()
    estado_civil = str(input('Digite “1” para casado e “2” para solteiro: ')).strip()
    print(f'A quantidade de caracteres do seu nome e do cônjuge, caso tenha, é: {func_definicao(nome, estado_civil)}.')

if __name__ == '__main__':
    main()
