import re

# CompanhiaAerea:
# o Adicionar um voo à companhia.
# o Listar todos os voos programados.

class CompanhiaAerea:
    def __init__(self, nome):
        if not nome.strip():
            raise ValueError("Nome da companhia não pode ser vazio!")
        self._nome = nome
        self._voos = []
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def voos(self):
        return self._voos
    
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
        self._numero = numero
        self._origem = origem
        self._destino = destino
        self._passagens = [] 
        
    @property
    def numero(self):
        return self._numero
        
    @property
    def origem(self):
        return self._origem
        
    @property
    def destino(self):
        return self._destino
        
    @property
    def passagens(self):
        return self._passagens
    
    def adicionar_passagem(self, passageiro, classe):
        if len(self.passagens) >= 4: # LIMITE TESTE - VOO DE 4 PESSOAS
            print(f"\nErro: Voo {self.numero} está lotado. O passageiro {passageiro.nome} não foi incluido no voo.\n")
            return
        passagem = PassagemAerea(passageiro, classe)
        self.passagens.append(passagem)
        # print para verificação
        print(f'Passagem registrada para {passageiro.nome} no voo {self.numero} com destino: {self.destino}.')
        print('-' * 70)
        
    def calcular_total_arrecadado(self):
        return sum(passagem.preco for passagem in self.passagens)
    
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
        self._passageiro = passageiro
        self._classe = classe
        self._preco = classe.calcular_preco()
        
    @property
    def passageiro(self):
        return self._passageiro
    
    @property
    def classe(self):
        return self._classe

    @property
    def preco(self):
        return self._preco
                
    def exibir_detalhes(self):
        detalhes = f'Passageiro: {self.passageiro.nome}\n'
                
        if isinstance(self.classe, ClasseEconomica): 
            detalhes += 'Tipo de Classe: Econômica\n'
            detalhes += f'Documento: {self.passageiro._documento}\n'
            detalhes += f'Bagagem incluída: {'Sim' if self.classe.bagagem_incluida else 'Não'}\n'
                               
        elif isinstance(self.classe, ClasseExecutiva):
            detalhes += 'Tipo de Classe: Executiva\n'
            detalhes += f'Documento: {self.passageiro._documento}\n'
            detalhes += f'Serviço de Bordo: {self.classe.servico_bordo}.\n.'
         
        detalhes += f'Preço: R$ {self.preco:.2f}\n'
           
        print(detalhes)

# Passageiro: Representa um passageiro, armazenando seu nome e documento de identificação.

class Passageiro:
    def __init__(self, nome, documento):
        self._nome = nome
        if not self.verificar_cpf(documento):
            raise ValueError("CPF invalido!")
        self._documento = documento
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def documento(self):
        return self._documento
     
    @staticmethod   
    def verificar_cpf(documento):
        cpf_limpo = re.sub(r'[^0-9]', '', documento)
        if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[0] * 11:
            return False
        # Validação simplificada para os dígitos verificadores
        return True
        
# ClasseVoo: Superclasse que representa uma classe de passagem aérea, com um preço base associado. Métodos: calcular_preco(): Retorna o preço da passagem.       

class ClasseVoo:
    def __init__(self, preco):
        self._preco = preco
        
    @property
    def preco(self):
        return self._preco
        
    def calcular_preco(self):
        return self.preco
    
# ClasseEconomica possui um atributo bagagem_incluida (booleano para indicar se inclui bagagem despachada).

class ClasseEconomica(ClasseVoo): # herda da classeVoo que é a superclasse
    def __init__(self, preco, bagagem_incluida):
        super().__init__(preco) # pra chamar os metodos da classe pai. Sem ele teria que reescrever a logica pra poder usar o preco aqui 
        self._bagagem_incluida = bagagem_incluida
        
    @property
    def bagagem_incluida(self):
        return self._bagagem_incluida
    
    def calcular_preco(self):
        return self.preco + (200 if self.bagagem_incluida else 0)
    
# ClasseExecutiva possui um atributo servico_bordo (ex.: "Refeição completa", "Lanche rápido").

class ClasseExecutiva(ClasseVoo):
    def __init__(self, preco, servico_bordo):
        super().__init__(preco)
        self._servico_bordo = servico_bordo
          
    @property
    def servico_bordo(self):
        return self._servico_bordo
    
    def calcular_preco(self):
        return self.preco + 1000
    


# def menu_interativo(companhia):
#     while True:
#         print("\n--- MENU INTERATIVO ---")
#         print("1. Adicionar um voo")
#         print("2. Listar todos os voos programados")
#         print("3. Adicionar passagem a um voo")
#         print("4. Exibir informações da companhia")
#         print("5. Exibir informações de um voo")
#         print("6. Sair\n")
        
#         opcao = input("Escolha uma opção: ")

#         if opcao == "1":
#             numero = input("Número do voo: ")                
#             origem = input("Origem do voo: ")
#             destino = input("Destino do voo: ")
#             voo = Voo(numero, origem, destino)
#             companhia.adicionar_voo(voo)
#         elif opcao == "2":
#             companhia.listar_voos()
#         elif opcao == "3":
#             numero_voo = input("Informe o número do voo: ")
#             voo_encontrado = None
#             for voo in companhia.voos:
#                 if voo.numero == numero_voo:
#                     voo_encontrado = voo
#                     break
#             if voo_encontrado:
#                 nome_passageiro = input("Nome do passageiro: ")
#                 documento = input("Documento do passageiro: ")
#                 passageiro = Passageiro(nome_passageiro, documento)
#                 print("Escolha a classe:")
#                 print("1. Econômica sem bagagem (R$ 500)")
#                 print("2. Econômica com bagagem (R$ 700)")
#                 print("3. Executiva (R$ 1500 + Refeição completa)")

#                 classe_opcao = input("Opção de classe: ")
#                 if classe_opcao == "1":
#                     classe = ClasseEconomica(500, False)
#                 elif classe_opcao == "2":
#                     classe = ClasseEconomica(500, True)
#                 elif classe_opcao == "3":
#                     classe = ClasseExecutiva(1500, "Refeição completa")
#                 else:
#                     print("Opção inválida.")
#                     continue
#                 voo_encontrado.adicionar_passagem(passageiro, classe)
#             else:
#                 print("Voo não encontrado.")
#         elif opcao == "4":
#             # Exibe informações sobre a companhia
#             print(f"\nInformações da companhia {companhia.nome}:")
#             print(f"Total de voos programados: {len(companhia.voos)}")
#             print("-" * 70)
#         elif opcao == "5":
#             # Exibe informações de um voo específico
#             numero_voo = input("Informe o número do voo para ver os detalhes: ")
#             voo_encontrado = None
#             for voo in companhia.voos:
#                 if voo.numero == numero_voo:
#                     voo_encontrado = voo
#                     break
#             if voo_encontrado:
#                 voo_encontrado.exibir_detalhes()
#             else:
#                 print("Voo não encontrado.")
#         elif opcao == "6":
#             print("Encerrando o programa...")
#             break
#         else:
#             print("Opção inválida. Tente novamente.")


# # Criar uma companhia
# companhia = CompanhiaAerea("Sky Airlines")
# # Iniciar o menu interativo
# menu_interativo(companhia)
