estacoes = {
    89.5: 'Cocais',
    91.5: 'Mix',
    94.1: 'Boa',
    99.1: 'Clube'
}

class RadioFM:
    def __init__(self, vol_max, estacoes):
        self.__volume_min = 0
        self.__volume_max = vol_max
        self.__freq_min = 88
        self.__freq_max = 108
        self.__estacoes = estacoes
        self.__volume = None
        self.__ligado = False
        self.__estacao_atual = None
        self.__frequencia_atual = None
        self.__antena_habilitada = False
        
    # método pra verificar ao inves de fazer varios if nos outros metodos
    def __verificar_status(self):
        if not self.__ligado:
            raise ValueError('Requisição inválida. A radio está desligada!')

    # No método ligar, atualizar o atributo ligado para True, o volume do rádio deverá ser inicializado com o volume mínimo do rádio. Se a antena estiver habilitada (antena_habilitada=True), a frequencia deverá ser inicializada com a frequencia da primeira estação de rádio definida no dicionário e a estação atual deverá ser inicializada com seu respectivo nome.

    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
            self.__volume = self.__volume_min
            
            antena_status = 'Não' if self.__antena_habilitada == False else 'Sim'
            print('Radio ligando...')
            print()
            print(f'Radio ligada\nVolume: {self.__volume}\nAntena habilitada: {antena_status}')
            
            if self.__antena_habilitada:
                return self.habilitar_antena()
            else: 
                while True:
                    habilitar = str(input('Deseja habilitar a antena? S/N: \n')).lower()
                    if habilitar == 's':                  
                        return self.habilitar_antena()
                    elif habilitar == 'n': 
                        print('Se precisar habilitar a antena insira [3] - Habilitar antena\n')
                        break
                    else:
                        print('Opção inválida\n')    
        else: 
            print('Rádio já está ligada\n')      
                
    def habilitar_antena(self):
        if self.__ligado:
            if not self.__antena_habilitada:
                self.__antena_habilitada = True             
                primeira_frequencia, primeira_estacao = next(iter(self.__estacoes.items())) 
                # O método items() retorna uma visão chave-valor do dict e o iter() cria um iterador sobre esses pares
                # for i in iter(self.estacoes.items()):
                #     print(i)               
                self.__frequencia_atual = primeira_frequencia 
                self.__estacao_atual = primeira_estacao
            else:
                print('Antena já está habilitada!\n') 
        else:
            print('Não é possível habilitar a antena com a rádio desligada.')         
            while True:
                ligar = str(input('Deseja ligar a radio? S/N: \n')).lower()
                if ligar == 's':                  
                    return self.ligar()
                elif ligar == 'n': 
                    print()
                    print('Se precisar habilitar a antena insira [1] - Ligar rádio\n')
                    break
                else:
                    print('Opção inválida\n')
     
    # No método desligar, mudar o estado para False, além de atualizar os atributos: volume, frequencia_atual e estação_atual para: None
        
    def desligar(self):
        print('Radio desligando...')
        self.__ligado = False
        self.__volume = None
        self.__estacao_atual = None
        self.__frequencia_atual = None 
        self.__antena_habilitada = False
            
    # O método aumentar_volume deverá receber um atributo opcional com valor inicial igual a 1. Caso este valor seja passado na chamada do argumento, atualizar o volume com o valor do argumento (fazer a crítica para não ultrapassar os valores permitidos para o volume). Caso o argumento fique vazio na chamada, o atributo volume deverá ser incrementado de uma unidade. (Fazer a crítica para não ultrapassar o valor máximo permitido)

    def aumentar_volume(self, valor = 1):
        if self.__ligado:
            if (self.__volume_min <= valor <= self.__volume_max):
                if valor == 1:
                    self.__volume += valor
                    print(f'Volume atual: {self.__volume}')
                # condição pra não deixar passar do volume máximo
                elif (valor + self.__volume) <= self.__volume_max:
                    self.__volume += valor
                    print(f'Volume atual: {self.__volume}')
            else:
                self.__volume = self.__volume_max
                print(f'Volume atual: {self.__volume}')
        else: 
            print('Requisição inválida. A radio está desligada!')
            
    def diminuir_volume(self, valor = 1):
        if self.__ligado:
            if (self.__volume_min <= valor <= self.__volume_max):
                if valor == 1:
                    self.__volume -= valor
                    print(f'Volume atual: {self.__volume}')
                # condição pra não deixar passar do volume máximo
                elif (valor - self.__volume) <= self.__volume_max:
                    self.__volume -= valor
                    print(f'Volume atual: {self.__volume}')
            else:
                self.__volume = self.__volume_max
                print(f'Volume atual: {self.__volume}')
        else: 
            print('Requisição inválida. A radio está desligada!')
            
    @property
    def volume(self):
        return self.__volume
    
    @property
    def frequencia(self):
        return self.__frequencia_atual
    
    @property
    def estacao(self):
        return self.__estacao_atual
    
    def mudar_frequencia(self, valor = 0):
        # verificar se radio ligada 
        # self.__verificar_status()
        if self.__ligado:
        
            frequencias = list(self.__estacoes.keys())
            nomes_estacoes = list(self.__estacoes.values())
            
            if valor == 0:
                # Se a frequencia atual for igual ao último elemento do dicionário e/ou self.__frequencia_atual is None
                if self.__frequencia_atual is None or self.__frequencia_atual == frequencias[-1]:
                    # mudar frequencia atual para a primeira
                    self.__frequencia_atual = frequencias[0]
                else:
                    indice_atual = frequencias.index(self.__frequencia_atual)
                    self.__frequencia_atual = frequencias[indice_atual + 1]
                    
            elif valor == 1:
                self.__frequencia_atual = frequencias[0]
                self.__estacao_atual = nomes_estacoes[0]
                
            elif valor == 2:
                self.__frequencia_atual = frequencias[1]
                self.__estacao_atual = nomes_estacoes[1]
                
            elif valor == 3:
                self.__frequencia_atual = frequencias[2]
                self.__estacao_atual = nomes_estacoes[2]
                
            elif valor == 4:
                self.__frequencia_atual = frequencias[3]
                self.__estacao_atual = nomes_estacoes[3]
                
            else:
                print('Opção inválida')
        else: 
            print('Requisição inválida. A radio está desligada!')    
            
        print(f"Frequência atual: {self.__frequencia_atual}\nEstação atual: {self.__estacao_atual}")           
    
    def __str__(self):
        return (
            f"\nRadioFM:\n"
            f"volume_min: {self.__volume_min}\n"
            f"volume_max: {self.__volume_max}\n"
            f"freq_min: {self.__freq_min}\n"
            f"freq_max: {self.__freq_max}\n"
            f"volume: {self.__volume}\n"
            f"ligado: {self.__ligado}\n"
            f"estação_atual: {self.__estacao_atual}\n"
            f"frequência_atual: {self.__frequencia_atual}\n"
            f"antena_habilitada: {self.__antena_habilitada}"
        )
        
    @property
    def definicao(self):
        return self.__str__()
    
def main():
    volume_max = int(input('Insira o volume máximo da rádio: '))
    print()
    print('#'*15)
    print('Radio FM')
    # criar objeto 
    radio1 = RadioFM(volume_max, estacoes)
    for i, n in iter(estacoes.items()):
        print(f'{i} : {n}')
    print('#'*15)
    
    while True:
        print(
'''
O que deseja fazer:
[1] - Ligar rádio              
[2] - Desligar rádio              
[3] - Habilitar antena              
[4] - Aumentar volume              
[5] - Diminuir volume   
[6] - Mudar estação 
[7] - Frequencia e estação atual 
[8] - Descrição atual 
[9] - Sair do programa          
              ''')
        resposta = input('')
        print()
        
        if resposta == '1':
            radio1.ligar()
            continue
        elif resposta == '2':
            return radio1.desligar()
        
        elif resposta == '3':
            radio1.habilitar_antena()
            continue
        
        elif resposta == '4':
            valor = int(input(f'''Qual volume deseja aumentar\nVolume mínimo: 0\nVolume máximo: {volume_max}\n'''))
            radio1.aumentar_volume(valor)
            continue
        
        elif resposta == '5':
            valor = int(input(f'''Qual volume deseja diminuir\nVolume mínimo: 0\nVolume máximo: {volume_max}\n'''))
            radio1.diminuir_volume(valor)
            continue
        
        elif resposta == '6':
            valor = int(input(
'''
'Estações disponíveis:

[0] - Proxima estação              
[1] - 89.5: 'Cocais
[2] - 91.5: 'Mix'
[3] - 94.1: 'Boa'
[4] - 99.1: 'Clube'
>
'''))
            radio1.mudar_frequencia(valor)
            continue
        
        elif resposta == '7':
            print('Frequencia:', radio1.frequencia)
            print('Estação:', radio1.estacao)
            continue
        
        elif resposta == '8':
            print(radio1.definicao)
            continue
        
        elif resposta == '9':
            print('Encerrando programa...')
            break
        
if __name__ == "__main__":
    main()