# Estados - atributos de um relógio digital
# horas, minutos, segundos, estado_24h (12h ou 24h)

# Os métodos ( que seriam os comportamentos, 'funções')
# ajustar_hora, alterar_formato, exibir_hora, adcionar_segundo *****(pensar nisso depois)

class Relogio_Digital:
    # Usar valores padronizados para mesmo sem ter passado valor, ele ter valores válidos.
    def __init__(self, horas=0, minutos=0, segundos=0, estado_24=True):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self.estado_24 = estado_24
    
    # pra garantir ta dentro do intervalo possivel de hora, min e segundo.
    def ajustar_horario(self, h, m, s):
        self.horas = h % 24
        self.minutos = m % 60 
        self.segundos = s % 60
        
    def alternar_formato(self):
        self.estado_24 = not self.estado_24 #(True pra False)
        
    def exibir_hora(self):
        h = self.horas
        # se não True, ele é False e consequentemente, o formato ´12h. 
        if not self.estado_24: 
            periodo = 'AM' if h < 12 else 'PM'
            h = h % 12 or 12 
            return f'{h:02}:{self.minutos:02}:{self.segundos:02} {periodo}'
        else:
            return f'{h:02}:{self.minutos:02}:{self.segundos:02}'
            
    def incrementar_segundo():
        pass # pensar nisso 
    
# Criar dois objetos pra classe 
relogio1 = Relogio_Digital(14, 30, 45, estado_24=True) 
relogio2 = Relogio_Digital(2, 15, 20, estado_24=False)

# mostrar os valores iniciais dos atributos
print(f'Relógio 1: {relogio1.exibir_hora()}')
print(f'Relógio 2: {relogio2.exibir_hora()}')

# mudar formato de exibição
relogio1.alternar_formato()
relogio2.alternar_formato()
print(f'Relógio 1: {relogio1.exibir_hora()}')
print(f'Relógio 2: {relogio2.exibir_hora()}')


