# LEMBRAR DE USAR ENCAPSULAMENTO

# CompanhiaAerea:
# o Adicionar um voo à companhia.
# o Listar todos os voos programados.

class CompanhiaAerea:
    def __init__(self, nome):
        self.nome = nome
        self.voos = []
        
    def adicionar_voo(self, voo):
        
        for v in self.voos:
            if v.numero == voo.numero:
                print(f"ERRO: O voo com número {voo.numero} já está cadastrado!")
                return
        
        print('Adicionando voo...')
        print(f'O voo {voo.numero} foi adicionado a {self.nome} com sucesso.')
        print('-' * 70)
        self.voos.append(voo)
        
    def listar_voos(self):
        print(f'\nVoos programados pela companhia {self.nome}: \n')
        total_arrecadado_geral = 0
        
        if len(self.voos) == 0:
                print('Nenhum voo cadastrado!')
        else:
            for voo in self.voos:
                voo.exibir_detalhes() # METODO EXIBIR DETALHES POSTERIORMENTE NA CLASSE VOO
                total_arrecadado_geral += voo.calcular_total_arrecadado()
            print('-' * 70)
        
        print(f'\nTotal arrecadado geral: R$ {total_arrecadado_geral:.2f}'.upper())
            
# Voo: o Registrar múltiplas passagens para diferentes passageiros.
# o Calcular o valor total arrecadado pelo voo.

class Voo:
    def __init__(self, numero, origem, destino):
        self.numero = numero
        self.origem = origem
        self.destino = destino
        self.passagens = []
        self.lista_numeros = []
        
    # def verificar_numero_voo(self):
    #     return self.numero in self.lista_numeros            
        
    def adicionar_passagem(self, passageiro, classe):
        if len(self.passagens) >= 5: # LIMITE TESTE
            print(f"Erro: Voo {self.numero} está lotado.")
            return
        passagem = PassagemAerea(passageiro, classe)
        self.passagens.append(passagem)
        # print para verificação
        print(f'Passagem registrada para {passageiro.nome} no voo {self.numero} com destino: {self.destino}.')
        print('-' * 70)
               
    def calcular_total_arrecadado(self):
        # lista_precos = []
        # total = sum(lista_precos)
        # for passagem in self.passagens:
        #     lista_precos.append(passagem.preco)
        # return total
        return sum(passagem.preco for passagem in self.passagens)
    
    # def total_arrecadado(self):
    #     return f'Total arrecadado: R$ {self.calcular_total_arrecadado():.2f}'  
    
    def exibir_detalhes(self):
        print(f'Voo {self.numero} ({self.origem} -> {self.destino})\n')
        print('Passageiros e detalhes das passagens:\n')
        
        if len(self.passagens) == 0:
                print('Não tem usuários cadastrados!')   
        else:       
            for passagem in self.passagens:               
                passagem.exibir_detalhes()
                print('-' * 70)            
        
        print(f'Total arrecadado para este voo: R$ {self.calcular_total_arrecadado():.2f}')               
        
            
# PassagemAerea: o Registrar uma passagem comprada por um passageiro.
# o Exibir os detalhes da passagem.

class PassagemAerea:
    def __init__(self, passageiro, classe):
        self.passageiro = passageiro
        self.classe = classe
        self.preco = classe.calcular_preco()
                
    def exibir_detalhes(self):
        detalhes = f'Passageiro: {self.passageiro.nome}\n'
                
        if isinstance(self.classe, ClasseEconomica): 
            detalhes += 'Tipo de Classe: Econômica\n'
            detalhes += f'Documento {self.passageiro.documento}\n'
            detalhes += f'Bagagem incluída: {'Sim' if self.classe.bagagem_incluida else 'Não'}\n'
                               
        elif isinstance(self.classe, ClasseExecutiva):
            detalhes += 'Tipo de Classe: Executiva\n'
            detalhes += f'Documento {self.passageiro.documento}\n'
            
            detalhes += f'Serviço de Bordo: {self.classe.servico_bordo}.\nClasse Executiva.'
         
        detalhes += f'Preço: R$ {self.preco:.2f}\n'
           
        print(detalhes)

# Passageiro: Representa um passageiro, armazenando seu nome e documento de identificação.

class Passageiro:
    def __init__(self, nome, documento):
        self.nome = nome        
        self.documento = documento
        
# ClasseVoo: Superclasse que representa uma classe de passagem aérea, com um preço base associado. Métodos: calcular_preco(): Retorna o preço da passagem.       

class ClasseVoo:
    def __init__(self, preco):
        self.preco = preco
        
    def calcular_preco(self):
        return self.preco
    
# ClasseEconomica possui um atributo bagagem_incluida (booleano para indicar se inclui bagagem despachada).

class ClasseEconomica(ClasseVoo): # herda da classeVoo que é a superclasse
    def __init__(self, preco, bagagem_incluida):
        super().__init__(preco) # pra chamar os metodos da ckasse pai. Sem ele teria que reescrever a logica pra poder usar o preco aqui 
        self.bagagem_incluida = bagagem_incluida
    
    # def quantidade_passagens(self): LIMITE DE PASSAGEM
    #     return self.quantidade
        
    def calcular_preco(self):
        # Valor no teste por enquanto coloquei pra ser True e False, MUDAR PRA SIM E NAO
        return self.preco + (200 if self.bagagem_incluida else 0)
    
# ClasseExecutiva possui um atributo servico_bordo (ex.: "Refeição completa", "Lanche rápido").

class ClasseExecutiva(ClasseVoo):
    def __init__(self, preco, servico_bordo):
        super().__init__(preco)
        self.servico_bordo = servico_bordo
          
    def calcular_preco(self):
        return self.preco + 1000
    

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
            # if voo.verificar_numero_voo():
            #     print(f"ERRO: Este número {numero} já foi cadastrado!")
            #     continue        
            # else:
            #     print(f"Voo {numero} cadastrado com sucesso!")
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

