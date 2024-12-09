import string
from datetime import datetime
from random import choices

# ARRUMAR O FORMATO DA HORA NA HORA DE IMPRIMIR 

class CartaoEstacionamento:
    # , data_saida, hora_saida, valor_total
    def __init__(self, dataHora):
        
        self.__dataHora_entrada = self.__validar_dataHora(
            dataHora)  # registrado na hr da criação do cartão
        
        # gerado automaticamente 8char alfanumérico, SE A HORA/DATA VÁLIDA
        self.__numero_cartao = self.__gerar_numero_cartao() if self.__dataHora_entrada else 'Não é possível gerar numero do cartão. Data e/ou hora inválida!'
        
        # se tiver data válida, status = ativo, se não = inativo. != FINALIZADO
        self.__status_cartao = 'Ativo' if self.__dataHora_entrada else 'INATIVO'
        
        self.__saida = None
        self.__tarifa = 4 # 4 reais por hora, 0,5 por 15 min add dps de 2h
        
        # self.data_saida = data_saida  # registrado na hr da criação do cartão
        # self.hora_saida = hora_saida  # registrado na hr da criação do cartão
        # self.valor_total = valor_total

    def __validar_dataHora(self, dataReferencia, formato="%d/%m/%Y %H:%M"):
        try:
            dataReferencia = datetime.strptime(dataReferencia, formato)
            return dataReferencia
        except ValueError:
            return None
        
    def __gerar_numero_cartao(self):
        digitos = ''.join(choices(string.digits, k=5))
        letras = ''.join(choices(string.ascii_letters, k=3))
        return digitos + letras

    def __valor(self, saida):
        saida = self.__validar_dataHora(saida)
        if saida <= self.__dataHora_entrada:
            raise ValueError('Inválido!')
        
        # metodo para transformar em segundos, dps / 60 para passar p min
        totalMin = (saida - self.__dataHora_entrada).total_seconds() / 60
        
        if totalMin > 120:
            minRestante = totalMin - 120
            valorRestante = (minRestante / 15) * 0.5
            valorTotal = (self.__tarifa * 2) + valorRestante 
        else:
            valorTotal = self.__tarifa * (totalMin / 60)
        return round(valorTotal, 2), (totalMin / 60)
            
        
    # NÃO É PRIVADO
    def consultar_valor(self, saida):
        valorTotal, tempoPermanencia = self.__valor(saida)
        print(f'Data e Hora ENTRADA: {self.__dataHora_entrada}\nData e Hora SAÍDA: {saida}\nTempo de permanencia: {tempoPermanencia:.0f} horas\nTotal a pagar: R${valorTotal}\n')

    # NÃO É PRIVADO, PQ VAI SER REGISTRADO E VALIDADO DATA E HORAR PELO MAIN
    def registrar_saida(self, saida):
        print('*'*10)
        self.consultar_valor(saida)   
        self.__saida = saida
        self.__status_cartao = 'Finalizado'
        print('*'*10)
        print(f'RESUMO:\n\n{self.__str__()}')
        print('*'*10)

    @property
    def numero_cartao(self):
        return self.__numero_cartao
    
    @property
    def entrada(self):
        return self.__dataHora_entrada

    @property
    def status(self):
        return self.__status_cartao
    
    @property
    def saida(self):
        return self.__saida

    def __str__(self):
        return f'Número cartão: {self.__numero_cartao}\nData e hora entrada: {self.__dataHora_entrada}\nStatus: {self.__status_cartao}\n'

#### OBJETO TESTE 1

# tentando entrar com data e hora válidas

cart1 = CartaoEstacionamento('09/11/2024 10:59')

# print(cart1)
    # SAÍDA TERMINAL
    # Número cartão: 52191VAV
    # Data e hora entrada: 2024-11-09 10:59:00
    # Status: Ativo

# cart1.consultar_valor('09/11/2024 13:59')
    # SAÍDA TERMINAL
    # Data e Hora ENTRADA: 2024-11-09 10:59:00
    # Data e Hora SAÍDA: 09/11/2024 13:59
    # Tempo de permanencia: 3 horas
    # Total a pagar: R$10.0
    

# cart1.registrar_saida('09/11/2024 13:59')
    # SAÍDA TERMINAL
    # **********
    # Data e Hora ENTRADA: 2024-11-09 10:59:00
    # Data e Hora SAÍDA: 09/11/2024 13:59
    # Tempo de permanencia: 3 horas
    # Total a pagar: R$10.0

    # **********
    # RESUMO:

    # Número cartão: 99151Kal
    # Data e hora entrada: 2024-11-09 10:59:00
    # Status: Finalizado

    # **********

# print(cart1.entrada) # 2024-11-09 10:59:00
# print(cart1.numero_cartao) # 02114hDB
# print(cart1.status) # Ativo
# print(cart1.saida) # None
# cart1.registrar_saida('09/11/2024 13:59')
# print(cart1.status) # Finalizado
# print(cart1.saida) # 09/11/2024 13:59


#### OBJETO TESTE 2

# tentando entrar com data formato inválido
cart2 = CartaoEstacionamento('09/11/28 10:59')
print(cart2) 
    # SAÍDA
    # Número cartão: Não é possível gerar numero do cartão. Data e/ou hora inválida!
    # Data e hora entrada: None
    # Status: INATIVO

# print(cart2.status) # INATIVO
# print(cart2.entrada) # None
# print(cart2.numero_cartao) # Não é possível gerar numero do cartão. Data e/ou hora inválida!
# print(cart2.saida) # None

