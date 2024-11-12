# Implemente a classe Bicicleta, colocando limites máximos e mínimos para os estados: veloc_atual, altura_cela e calibragem_pneus através de seus respectivos métodos. Altere os métodos: regular_cela, calibrar_pneus para permitirem as mudanças caso a bicicleta esteja parada (veloc_atual=0).

# estados: veloc_atual, altura_cela e calibragem_pneus
# metodos: regular_cela, calibrar_pneus para permitirem as mudanças caso a bicicleta esteja parada (veloc_atual=0)

class Bicileta:
    def __init__(self, veloc_atual=0, altura_cela=0, calibragem_pneus=30):
        self.veloc_atual = veloc_atual # limite de 0 a 50 km/h
        self.altura_cela = altura_cela # limite de 0 a 25 cm
        self.calibragem_pneus = calibragem_pneus # limite de 30 a 40 PSI
        
    def acelerar(self):
        valor_alterado = int(input('Em quanto acelerar: '))
        nova_velocidade = valor_alterado + self.veloc_atual
        self.veloc_atual = nova_velocidade
        print(f'Velociade atual: {nova_velocidade:.2f} Km/h')
    
    def frear(self):
        valor_alterado = int(input('Em quanto frear: '))
        nova_velocidade = self.veloc_atual - valor_alterado
        self.veloc_atual = nova_velocidade
        print(f'Velociade atual: {nova_velocidade:.2f} Km/h')
                    
    def regular_cela(self): # supondo variar de 0 a 25cm
        if self.veloc_atual == 0:
            print('''As opções: 
                a) 0
                b) 10cm
                c) 15cm 
                d) 25cm ''')
            opc = input('Qual opção desejada: ').strip().lower()
            if opc == 'a':
                print('A cela da bicicleta foi regulada em 0cm.')
            elif opc=='b':
                print('A cela da bicicleta foi regulada para 10cm.')    
            elif opc=='c':
                print('A cela da bicicleta foi regulada para 15cm.')
            elif opc=='d':
                print('A cela da bicicleta foi regulada para 25cm.')
            else:
                print('Escolha uma alternativa válida.')    
                return self.regular_cela()
        else:
            print('A bicicleta deve está parada para regular.')
               
    def calibrar_pneus(self):
        if self.veloc_atual == 0:
            print('''As opções para calibrar: 
                a) 30 PSI
                b) 40 PSI
                ''')
            opc = input('Qual opção desejada: ').strip().lower()
            if opc == 'a':
                print('Calibragem dos pneus ajustada para: 30 PSI')
            elif opc=='b':
                print('Calibragem dos pneus ajustada para: 40 PSI')
            else:
                print('Escolha uma alternativa válida.')    
                return self.calibrar_pneus()
        else:
            print('A bicicleta deve está parada para calibrar.')
# criar objeto                     
bicicleta1 = Bicileta()
# regular cela
print('regulando a altura da cela...')
bicicleta1.regular_cela()

bicicleta1.acelerar()
print()

#regular cela
print('Tentando regular a altura da cela....')
bicicleta1.regular_cela()
print()

# frear para poder permitir mudanças
print('freando...')
bicicleta1.frear()
print()

print('Tentando regular a altura da cela....')
bicicleta1.regular_cela()
print()

print('Tentando calibrar os pneus....')
bicicleta1.calibrar_pneus()
print()


