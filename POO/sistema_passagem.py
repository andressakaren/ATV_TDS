# LEMBRAR DE USAR ENCAPSULAMENTO

# CompanhiaAerea:
# o Adicionar um voo à companhia.
# o Listar todos os voos programados.

class CompanhiaAerea:
    def __init__(self, nome):
        self.nome = nome
        self.voos = []
        
    def adicionar_voo(self, voo):
        self.voos.append(voo)
        
    def listar_voos(self):
        print(f'Voos programados pela companhia {self.nome}: ')
        
        for voo in self.voos:
            voo.exibir_detalhes() # METODO EXIBIR DETALHES POSTERIORMENTE NA CLASSE VOO
            
# Voo: o Registrar múltiplas passagens para diferentes passageiros.
# o Calcular o valor total arrecadado pelo voo.

class Voo:
    def __init__(self, numero, origem, destino):
        self.numero = numero
        self.origem = origem
        self.destino = destino
        self.passagens = []
        
    def adicionar_passagem(self, passageiro, classe):
        if len(self.passagens) >= 5: # LIMITE TESTE
            return # RETORNAR ERRO, TIPO 'VOO LOTADO'
        passagem = PassagemAerea(passageiro, classe)
        self.passagens.append(passagem)
        # print para verificação
        print(f'Passagem registrada para {passageiro.nome} no voo com destino: {self.destino} e número: {self.numero}.')
               
    def calcular_total_arrecadado(self):
        # lista_precos = []
        # total = sum(lista_precos)
        # for passagem in self.passagens:
        #     lista_precos.append(passagem)
        # return total
        return sum(passagem.preco for passagem in self.passagens)
    
    def exibir_detalhes(self):
        print(f'Voo {self.numero} ({self.origem} -> {self.destino})')
        
        # DETALHES DE TODAS AS PASSAGENS ??
        
        print(f'Total arrecadado: R$ {self.calcular_total_arrecadado():.2f}')  
            
# PassagemAerea: o Registrar uma passagem comprada por um passageiro.
# o Exibir os detalhes da passagem.

class PassagemAerea:
    def __init__(self, passageiro, classe):
        self.passageiro = passageiro
        self.classe = classe
        self.preco = classe.calcular_preco()
        
    def exibir_detalhes(self):
        detalhes = f'Passageiro: {self.passageiro}\n'
        
        # Tipo de classe (????)
        if isinstance(self.classe, ClasseEconomica): # ISINSTANCE saber se a classe é instancia das subclasses economica ou executiva
            detalhes += f'Bagagem incluída: {'Sim' if self.classe.bagagem_incluida else 'Não'}\n'
            
        elif isinstance(self.classe, ClasseExecutiva):
            detalhes += f'Serviço de Bordo: {self.classe.servico_bordo}.\n'
            
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
    
     
                    
    

companhia = CompanhiaAerea("Sky Airlines")
print(companhia.nome)
companhia.listar_voos()


voo1 = Voo(101, 'São Paulo', 'Teresina')
companhia.adicionar_voo(voo1)
companhia.listar_voos()





# # Criando voos
# voo1 = Voo(101, "São Paulo", "Nova York")
# voo2 = Voo(202, "Rio de Janeiro", "Lisboa")
# companhia.adicionar_voo(voo1)
# companhia.adicionar_voo(voo2)
# # Cadastrando passageiros e comprando passagens
# passageiro1 = Passageiro("João", "123456789")
# passageiro2 = Passageiro("Maria", "987654321")
# passageiro3 = Passageiro("Pedro", "555666777")
# voo1.adicionar_passagem(passageiro1, ClasseExecutiva(4500, "Refeição completa"))
# voo1.adicionar_passagem(passageiro2, ClasseEconomica(2000, True))
# voo2.adicionar_passagem(passageiro3, ClasseEconomica(1800, False))
# # Listando voos e passagens
# companhia.listar_voos()
