# Criar uma companhia
companhia = CompanhiaAerea("Sky Airlines")

print(companhia.nome)
# companhia.listar_voos()

# Cadastra voo1
voo1 = Voo(101, 'São Paulo', 'Teresina')

companhia.adicionar_voo(voo1)
# companhia.listar_voos()

# Cadastra voo2
voo2 = Voo(202, 'Xique Xique', 'Belo Horizonte')
companhia.adicionar_voo(voo2)
# companhia.listar_voos()


### CADASTRAR PASSAGEIROS
passageiro1 = Passageiro('Kallya', '57427651344')
passageiro2 = Passageiro('Carlos', '54622255468')
passageiro3 = Passageiro('luiz', '78955532684')

## CRIANDO CLASSES
economica_sem_bag = ClasseEconomica(500, False)
economica_com_bag = ClasseEconomica(500, True)
executiva_nivel1 = ClasseExecutiva(1500, 'Refeição completa')
executiva_nivel2 = ClasseExecutiva(2000, 'All inclusive')

## ADD as classes ao respectivo voo
voo1.adicionar_passagem(passageiro1, economica_com_bag)
voo1.adicionar_passagem(passageiro2, economica_sem_bag)
voo2.adicionar_passagem(passageiro3, executiva_nivel2)

companhia.listar_voos()









--------------------------------------------------------

   
def menu_interativo(companhia):
    while True:
        print("\n--- MENU INTERATIVO ---")
        print("1. Adicionar um voo")
        print("2. Listar todos os voos programados")
        print("3. Adicionar passagem a um voo")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = input("Número do voo: ")
            # condição de se já existir esse numero .. tem  u ser unico
            origem = input("Origem do voo: ")
            destino = input("Destino do voo: ")
            voo = Voo(numero, origem, destino)
            companhia.adicionar_voo(voo)
            print(f"Voo {numero} cadastrado com sucesso!")
        
        elif opcao == "2":
            companhia.listar_voos()
        
        elif opcao == "3":
            numero_voo = input("Informe o número do voo: ")
            voo_encontrado = None
            for voo in companhia.voos:
                if voo.numero == numero_voo:
                    voo_encontrado = voo
                    break
            if voo_encontrado:
                nome_passageiro = input("Nome do passageiro: ")
                documento = input("Documento do passageiro: ")
                passageiro = Passageiro(nome_passageiro, documento)

                print("Escolha a classe:")
                print("1. Econômica sem bagagem (R$ 500)")
                print("2. Econômica com bagagem (R$ 700)")
                print("3. Executiva (R$ 1500 + Refeição completa)")
                
                classe_opcao = input("Opção de classe: ")
                if classe_opcao == "1":
                    classe = ClasseEconomica(500, False)
                elif classe_opcao == "2":
                    classe = ClasseEconomica(500, True)
                elif classe_opcao == "3":
                    classe = ClasseExecutiva(1500, "Refeição completa")
                else:
                    print("Opção inválida.")
                    continue

                voo_encontrado.adicionar_passagem(passageiro, classe)
            else:
                print("Voo não encontrado.")
        
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Criar uma companhia
companhia = CompanhiaAerea("Sky Airlines")

# Iniciar o menu interativo
menu_interativo(companhia)

=-------------------------------------------

# # Criar uma companhia
# companhia = CompanhiaAerea("Sky Airlines")

# print(companhia.nome)
# # companhia.listar_voos()

# # Cadastra voo1
# voo1 = Voo(101, 'São Paulo', 'Teresina')

# companhia.adicionar_voo(voo1)
# # companhia.listar_voos()

# # Cadastra voo2
# voo2 = Voo(202, 'Xique Xique', 'Belo Horizonte')
# companhia.adicionar_voo(voo2)

# voo3 = Voo(303, 'São Luiz', 'Manaus')
# companhia.adicionar_voo(voo3)

# voo4 = Voo(404, 'Porto Alegre', 'Fortaleza')
# companhia.adicionar_voo(voo4)

# voo5 = Voo(505, 'Salvador', 'João Pessoa')
# companhia.adicionar_voo(voo5)

# voo6 = Voo(606, 'Salvador', 'João Pessoa')
# companhia.adicionar_voo(voo6)
# # companhia.listar_voos()


# ### CADASTRAR PASSAGEIROS
# passageiro1 = Passageiro('Kallya', '57427651344')
# passageiro2 = Passageiro('Carlos', '54622255468')
# passageiro3 = Passageiro('luiz', '78955532684')
# passageiro4 = Passageiro('Jõao', '47387488734')
# passageiro5 = Passageiro('Pedro', '65364356309')


# ## CRIANDO CLASSES
# economica_sem_bag = ClasseEconomica(500, False)
# economica_com_bag = ClasseEconomica(500, True)
# executiva_nivel1 = ClasseExecutiva(1500, 'Refeição completa')
# executiva_nivel2 = ClasseExecutiva(2000, 'All inclusive')

# ## ADD as classes ao respectivo voo
# voo1.adicionar_passagem(passageiro1, economica_com_bag)
# voo1.adicionar_passagem(passageiro2, economica_sem_bag)
# voo1.adicionar_passagem(passageiro2, economica_com_bag)
# voo1.adicionar_passagem(passageiro4, economica_sem_bag)
# voo1.adicionar_passagem(passageiro5, economica_sem_bag)

# voo2.adicionar_passagem(passageiro3, executiva_nivel2)

# companhia.listar_voos()