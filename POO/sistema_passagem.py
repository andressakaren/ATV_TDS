# LEMBRAR DE USAR ENCAPSULAMENTO

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