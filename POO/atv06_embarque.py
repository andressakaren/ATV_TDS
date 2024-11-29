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


class cartaoEmbarque:
    
    def __init__(self, nome, numero_voo, localizador, data, hora, status, assento):
        # imutáveis
        self.nome = nome
        self.numero_voo = numero_voo
        self.localizador = localizador
        self.data = data 
        self.hora = hora
        
        # mutáveis 
        self.status = status
        self.assento = assento