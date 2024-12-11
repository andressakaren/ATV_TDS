estações = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}

class RadioFM:
    # , estações
    def __init__(self, vol_max):
        self.volume_min = 0
        self.volume_max = vol_max
        # self.freq_min = 88
        # self.freq_max = 108
        self.estações = estações
        self.__volume = None
        self.__ligado = False
        self.estação_atual = None
        self.frequencia_atual = None
        self.__antena_habilitada = False

# No método ligar, atualizar o atributo ligado para True, o volume do rádio deverá ser inicializado com o volume mínimo do rádio. Se a antena estiver habilitada (antena_habilitada=True), a frequencia deverá ser inicializada com a frequencia da primeira estação de rádio definida no dicionário e a estação atual deverá ser inicializada com seu respectivo nome.

    def ligar(self):
        self.__ligado = True
        self.__volume = self.volume_min
        
        antena_status = 'Não' if self.__antena_habilitada == False else 'Sim'
        print(f'Radio ligada\nVolume: {self.__volume}\nAntena habilitada: {antena_status}')
        
        if self.__antena_habilitada == True:
            return self.habilitarAntena()
        else: 
            while True:
                habilitar = str(input('Deseja habilitar a antena? S/N: ')).lower()
                if habilitar == 's':                  
                    return self.habilitarAntena()
                elif habilitar == 'n': 
                    print('Se precisar habilitar a antena utilize o método .habilitarAntena()')
                    break
                else:
                    print('Opção inválida')
                    
                
    def habilitarAntena(self):
        if self.__antena_habilitada == False:
            self.__antena_habilitada = True
            # Arrumar isso aqui pra iniciar na estação certa
            self.frequencia_atual = 89.5 # frequencia primeira estação
            self.estação_atual = 'Cocais'
            print()
            print(f'Antena habilitada\nEstação: {self.estação_atual}\nFrequencia: {self.frequencia_atual}')
        else:
            print('Antena já está habilitada!')
        
            
    # def __str__(self):
    #     return f''

    # def desligar(self):
    #     pass

    # def aumentar_volume(self):
    #     pass

    # def diminuir_volume(self):
    #     pass

    # def mudar_frequencia(self):
    #     pass

radio = RadioFM(20)
radio.ligar()
# print('#'*10)
# radio.habilitarAntena()