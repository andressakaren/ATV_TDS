from random import choices
from datetime import datetime
import string

class cartaoEstacionamento:   
    def __init__(self):
        self.__numero = self.__gerar_numero()
        self.__data_entrada = datetime.now() 
        self.__data_entrada = None 
        self.__status = 'Ativo'
        self.__valor_total = 0.0
        
    @staticmethod
    def __gerar_numero():
        return ''.join(choices(string.ascii_uppercase + string.digits, k=8))
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def data_entrada(self):
        return self.__data_entrada

    @property
    def data_saida(self):
        return self.__data_saida
               
    @data_saida.setter
    def data_saida(self, valor):
        if valor <= self.__data_entrada:
            raise ValueError("A data de saída não pode ser anterior à data de entrada.")
        self.__data_saida = valor
        self.__status = "Finalizado"  # Altera o status para finalizado
        self.calcular_valor()
        
    def status(self):
        return self.__status
    
    @property
    def valor_total(self):
        return self.__valor_total

    def registrar_saida(self):
        """Registra a saída do veículo, calculando o valor total."""
        if self.__data_saida is not None:
            print("Saída já registrada para este cartão!")
            return
        
        self.data_saida = datetime.now()  # Define a data de saída atual
        print(f"Saída registrada. Total a pagar: R$ {self.__valor_total:.2f}")
        
    def consultar_valor_acumulado(self):
        """Consulta o valor acumulado até o momento."""
        if self.__data_saida:
            print(f"Valor total a pagar (cartão finalizado): R$ {self.__valor_total:.2f}")
        else:
            _, valor_parcial = self.__calcular_tempo_e_valor()
            print(f"Valor acumulado até o momento: R$ {valor_parcial:.2f}")

    def calcular_valor(self):
        if self.__data_saida is None:
            raise ValueError("Saída não registrada. Não é possível calcular o valor total.")
        _, self.__valor_total = self.__calcular_tempo_e_valor()

    def __calcular_tempo_e_valor(self):
        data_fim = self.__data_saida or datetime.now()
        if data_fim < self.__data_entrada:
            raise ValueError("A data de saída não pode ser anterior à data de entrada.")
        
        tempo_total = data_fim - self.__data_entrada
        minutos_totais = tempo_total.total_seconds() / 60
        
        if minutos_totais <= 120:
            valor = 8.00  # Valor fixo para até 2 horas
        else:
            excesso = minutos_totais - 120
            valor_excedente = (excesso / 15) * 0.50  # R$0.50 por cada 15 min
            valor = 8.00 + valor_excedente
        return tempo_total, round(valor, 2)

    def __str__(self):
        entrada = self.__data_entrada.strftime("%d/%m/%Y %H:%M:%S")
        saida = self.__data_saida.strftime("%d/%m/%Y %H:%M:%S") if self.__data_saida else "Ainda não registrada"
        return (f"Cartão #{self.__numero}\n"
                f"Status: {self.__status}\n"
                f"Entrada: {entrada}\n"
                f"Saída: {saida}\n"
                f"Valor Total: R$ {self.__valor_total:.2f}\n")

# Teste
cartao1 = cartaoEstacionamento()
print(cartao1)
cartao1.consultar_valor_acumulado()

cartao1.registrar_saida()
print(cartao1)

cartao2 = cartaoEstacionamento()
print(cartao2)