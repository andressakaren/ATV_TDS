def lista():
    lista_nomes = []
    while True:
        print('\n==== MENU ====')
        print('1) Cadastrar nome')
        print('2) Pesquisar nome')
        print('3) Listar todos os nomes')
        print('0) Sair do programa')
        escolha = input('Digite sua escolha: ')

        if escolha == '1':
            nome = input('Digite o nome a ser cadastrado: ')
            lista_nomes.append(nome)
        elif escolha == '2':
            nome = input('Digite o nome a ser pesquisado: ')
            if nome in lista_nomes:
                print(f'{nome} encontrado na posição {lista_nomes.index(nome)}.')
            else:
                print(f'{nome} não está na lista.')
        elif escolha == '3':
            print('Lista de nomes:', lista_nomes)
        elif escolha == '0':
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida. Tente novamente.')

lista()
