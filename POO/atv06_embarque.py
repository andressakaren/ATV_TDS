# 1. Atributos imutáveis:
# o Nome do passageiro
# o Número do voo
# o Código da reserva (localizador)
# o Data e hora do embarque (utilizar biblioteca datetime para validação)

# 2. Atributos mutáveis:
# o Status do check-in (realizado ou não)
# o Assento

# 3. Métodos sugeridos:
# o Um método para realizar o check-in, que altera o status e associa um assento
# (aleatório) disponível ao passageiro.
# o Um método para alterar o assento (apenas se o check-in já tiver sido
# realizado).
# o Validações para garantir que assentos indisponíveis não sejam atribuídos e
# que o check-in só possa ser feito uma vez.

# 4. Requisitos de validação:
# o O código da reserva deve ter 6 caracteres alfanuméricos.
# o A hora do embarque não pode ser retroativa em relação ao momento de
# execução do código.

# 5. Teste:
# o Crie pelo menos três objetos da classe, representando cartões de embarque
# diferentes.
# o Demonstre os métodos implementados e suas validações em ação.


# class cartaoEmbarque:
    
#     def __init__(self, nome, numero_voo, localizador, data, hora, status, assento):
#         # imutáveis
#         self.nome = nome
#         self.numero_voo = numero_voo
#         self.localizador = localizador
#         self.data = data 
#         self.hora = hora
        
#         # mutáveis 
#         self.status = status
#         self.assento = assento

from random import randint, choice
from datetime import datetime

class CartaoEmb:
    def __init__(self, nome, numVoo, reserva, momentoEmb) -> None:
        self.__nome = nome
        self.__numVoo = numVoo
        if len(reserva) == 6:
            self.__reserva = reserva
        else:
            raise ValueError('Valor de reserva incorreto.')
        self.__momentoEmb = self.__val_dataHora(momentoEmb)
        self.__assento = 'Aguardando check-in.'
        self.__checkin = False
        
    def __str__(self) -> str:
        return f"## Cartão de embarque\nNome:{self.__nome}\nNúmero do Vôo: {self.__numVoo}\nReserva: {self.__reserva}\nMomento de embarque: {self.__momentoEmb}\nAssento: {self.__assento}\nCheck-in: {self.__checkin}"
        
    def set_checkin(self):
        if self.__checkin != True:
            self.__checkin = True
            self.__set_assento()
            print(f'Checkin realizado!\nSeu assento é: {self.__assento}')
        else:
            raise ValueError('Check-in já realizado.')
        
    def __set_assento(self):
        self.__set_assentosDisp()
        assento = choice(self.__assentosDisp)
        self.__assento = assento
        self.__assentosDisp.remove(assento)
        
    def __set_assentosDisp(self):
        self.__assentosDisp = []
        quantidade = randint(1, 10)
        while len(self.__assentosDisp) < quantidade:
            num = randint(1, 10)
            if (len(self.__assentosDisp) == 0) or (num not in self.__assentosDisp):
                self.__assentosDisp.append(num)
    
    def __val_dataHora(self, momento, formato="%d/%m/%Y %H:%M"):
        try:
            momentoVal = datetime.strptime(momento, formato)
            return momentoVal
        except ValueError:
            raise ValueError("Data e hora inválidas!")
        
def main():
    # Normal
    cartao1 = CartaoEmb('Hiromi', 266, "ABCDEF", "01/12/2024 13:23")
    print(cartao1)
    
    # Erro na reversa
    cartao2 = CartaoEmb('Anri', 377, "GHIJKL", "05/01/2025 09:45")
    
    # Erro na data
    cartao3 = CartaoEmb('Junko', 488, "MNOPQR", "10/02/2025 15:30")
    
    # Realizando checkin
    cartao1.set_checkin()
    print(cartao1)
    
    # Testando checkin
    cartao1.set_checkin()


if __name__ == "__main__":
    main()