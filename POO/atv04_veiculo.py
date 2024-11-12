# Implementar uma classe Veiculo que represente o registro de um veículo em um sistema de controle de veículos. A atividade deve explorar a criação de construtores, atributos obrigatórios e opcionais, e o uso de métodos para exibir e atualizar as informações do veículo.

class Veiculos:
    def __init__(self, chassi, marca, modelo, ano, placa='N/A', cor='Não especificado', proprietario='Não especificado', quilometragem=0):
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = int(ano)
        
        self.placa = input('Informe a placa: ') or placa
        self.cor = input('Informe a cor: ') or cor
        self.proprietario = input('Informe o proprietario: ') or proprietario
        self.quilometragem = input('Informe a quilometragem: ') or quilometragem
        
        self.ligado = False
        self.velocidade_atual = 0

    def __str__(self):  # imprimir o estado atual do veículo
         return (f'O chassi: {self.chassi}\n'
                f'O marca: {self.marca}\n'
                f'O modelo: {self.modelo}\n'
                f'O ano: {self.ano}\n'
                f'A placa: {self.placa}\n'
                f'A cor: {self.cor}\n'
                f'O proprietario: {self.proprietario}\n'
                f'A quilometragem: {self.quilometragem}\n') 
    
    def ligar_motor(self):
        self.ligado = True
        print('O motor está ligando...')
        print('O motor ligado!')
    
    def acelerar(self):
        if self.ligado:
            self.velocidade_atual = 0
            self.quantidade_alterada = int(input('Em quanto deseja acelerar: '))
            self.velocidade_atual = self.quantidade_alterada       
            print(f'O carro está acelerando...')
            print(f'Velocidade atual: {self.velocidade_atual} Km/h')
        else:
            print('Ligue o motor primeiro..')
        
    def frear(self):
        if self.ligado:
            self.quantidade_alterada = int(input('Em quanto deseja frear: '))
            if self.quantidade_alterada == 0:
                print('O valor inserido (0 km/h) não altera a velocidade atual.')
            else:
                self.velocidade_atual = self.velocidade_atual - self.quantidade_alterada       
                print(f'O carro está desacelerando...')
                print(f'Velocidade atual: {self.velocidade_atual} Km/h')
        else:
            print('Ligue o motor primeiro...')
           
    def desligar_motor(self):
        self.ligado = False
        print('O motor está desligando...')
        print('O motor desligado!')
        
    def abrir_porta(self):
        if self.velocidade_atual == 0:
            print('Abrindo porta...')
        else:
            print('Não pode abrir a porta enquanto acelera o veiculo!')
            

# cirar um objeto
carro1 = Veiculos('9BD111060T5002156', 'volkswagen', 'Gol', '2010')
print(carro1)

carro1.ligar_motor()
print()
carro1.acelerar()
print()
carro1.frear()
print()
carro1.abrir_porta()
print()
carro1.frear()
print()
carro1.abrir_porta()



