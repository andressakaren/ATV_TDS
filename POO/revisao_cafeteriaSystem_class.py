import datetime
import random
import string

class Pedido:
    def __init__(self, itens, mesa):
        self.numero = self.gerar_numero_pedido()
        self.mesa = mesa
        self.itens = itens
        self.data_hora_criacao = datetime.datetime.now()
        self.status = "ativo"
        self.data_hora_finalizacao = None
        self.valor_total = None

    @staticmethod
    def gerar_numero_pedido():
        """Gera um número único de pedido com 8 caracteres alfanuméricos."""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def finalizar(self):
        """Finaliza o pedido, calcula o total e registra a hora de finalização."""
        if self.status == "finalizado":
            print(f"O pedido {self.numero} já está finalizado.")
            return

        self.data_hora_finalizacao = datetime.datetime.now()
        self.status = "finalizado"
        self.valor_total = self.calcular_valor_total()
        print(f"Pedido {self.numero} finalizado. Total: R$ {self.valor_total:.2f}")

    def calcular_valor_total(self):
        """Calcula o valor total do pedido com base nos itens."""
        return sum(self.itens.values())

    def consultar(self):
        """Exibe os detalhes do pedido."""
        total = self.valor_total if self.status == "finalizado" else "Aguardando finalização"
        print(f"""
        Detalhes do Pedido {self.numero}:
        Mesa: {self.mesa}
        Itens: {self.itens}
        Status: {self.status}
        Total: {total}
        Data/Hora de Criação: {self.data_hora_criacao}
        Data/Hora de Finalização: {self.data_hora_finalizacao}
        """)

class Cafeteria:
    def __init__(self):
        self.pedidos = []

    def criar_pedido(self, itens, mesa):
        """Cria um novo pedido para uma mesa."""
        pedido = Pedido(itens, mesa)
        self.pedidos.append(pedido)
        print(f"Pedido {pedido.numero} criado para a mesa {mesa}.")
        return pedido

    def consultar_pedido(self, numero_pedido):
        """Consulta os detalhes de um pedido pelo número."""
        pedido = self.buscar_pedido(numero_pedido)
        if pedido:
            pedido.consultar()
        else:
            print("Pedido não encontrado.")

    def finalizar_pedido(self, numero_pedido):
        """Finaliza um pedido pelo número."""
        pedido = self.buscar_pedido(numero_pedido)
        if pedido:
            pedido.finalizar()
        else:
            print("Pedido não encontrado.")

    def buscar_pedido(self, numero_pedido):
        """Busca um pedido pelo número."""
        for pedido in self.pedidos:
            if pedido.numero == numero_pedido:
                return pedido
        return None

# Demonstração
cafeteria = Cafeteria()

# Criar três pedidos
pedido1 = cafeteria.criar_pedido({"Café": 5.00, "Pão de Queijo": 3.50}, mesa=1)
pedido2 = cafeteria.criar_pedido({"Capuccino": 7.00, "Bolo": 6.00}, mesa=2)
pedido3 = cafeteria.criar_pedido({"Suco": 4.50, "Sanduíche": 8.00}, mesa=3)

# Consultar um pedido
cafeteria.consultar_pedido(pedido1.numero)

# Finalizar pedidos
cafeteria.finalizar_pedido(pedido1.numero)
cafeteria.finalizar_pedido(pedido2.numero)

# Consultar pedidos finalizados
cafeteria.consultar_pedido(pedido1.numero)
cafeteria.consultar_pedido(pedido2.numero)

# Tentar finalizar novamente
cafeteria.finalizar_pedido(pedido1.numero)

# Consultar pedido não finalizado
cafeteria.consultar_pedido(pedido3.numero)
