import datetime
import random
import string

class Cafeteria:
    def __init__(self):
        self.ligado = False
        self.cafe_disponivel = 0.0  # Quantidade de café disponível em litros
        self.pedidos = []  # Lista de pedidos criados

    def ligar(self):
        if self.ligado:
            print("A cafeteria já está ligada.")
        else:
            self.ligado = True
            print("Cafeteria ligada.")

    def desligar(self):
        if not self.ligado:
            print("A cafeteria já está desligada.")
        else:
            self.ligado = False
            print("Cafeteria desligada.")

    def adicionar_cafe(self, quantidade):
        if not self.ligado:
            print("Ligue a cafeteria antes de adicionar café.")
            return
        if quantidade <= 0:
            print("Adicione uma quantidade válida de café.")
            return
        self.cafe_disponivel += quantidade
        print(f"Foram adicionados {quantidade:.2f} litros de café. Total disponível: {self.cafe_disponivel:.2f} litros.")

    def servir_cafe(self, quantidade):
        if not self.ligado:
            print("Ligue a cafeteria antes de servir café.")
            return
        if quantidade <= 0:
            print("Informe uma quantidade válida para servir.")
            return
        if quantidade > self.cafe_disponivel:
            print("Quantidade insuficiente de café disponível.")
            return
        self.cafe_disponivel -= quantidade
        print(f"Servidos {quantidade:.2f} litros de café. Restante disponível: {self.cafe_disponivel:.2f} litros.")

    def criar_pedido(self, itens, mesa):
        if not self.ligado:
            print("Ligue a cafeteria antes de criar pedidos.")
            return
        numero_pedido = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        pedido = {
            "numero_pedido": numero_pedido,
            "mesa": mesa,
            "itens": itens,
            "data_hora_criacao": datetime.datetime.now(),
            "status": "ativo",
            "data_hora_finalizacao": None,
            "valor_total": None
        }
        self.pedidos.append(pedido)
        print(f"Pedido {numero_pedido} criado para a mesa {mesa}.")
        return numero_pedido

    def finalizar_pedido(self, numero_pedido):
        for pedido in self.pedidos:
            if pedido["numero_pedido"] == numero_pedido:
                if pedido["status"] == "finalizado":
                    print("O pedido já está finalizado.")
                    return

                pedido["data_hora_finalizacao"] = datetime.datetime.now()
                pedido["status"] = "finalizado"
                pedido["valor_total"] = self.calcular_valor_total(pedido["itens"])
                print(f"Pedido {numero_pedido} finalizado. Total: R$ {pedido['valor_total']:.2f}")
                return
        print("Pedido não encontrado.")

    def calcular_valor_total(self, itens):
        return sum(itens.values())

    def consultar_pedido(self, numero_pedido):
        for pedido in self.pedidos:
            if pedido["numero_pedido"] == numero_pedido:
                status = pedido["status"]
                total = pedido["valor_total"] if status == "finalizado" else "Aguardando finalização"
                print(f"""
                Detalhes do Pedido {numero_pedido}:
                Mesa: {pedido['mesa']}
                Itens: {pedido['itens']}
                Status: {status}
                Total: {total}
                Data/Hora de Criação: {pedido['data_hora_criacao']}
                Data/Hora de Finalização: {pedido['data_hora_finalizacao']}
                """)
                return
        print("Pedido não encontrado.")

# Demonstração
cafeteria = Cafeteria()

# Ligar a cafeteria
cafeteria.ligar()

# Adicionar café
cafeteria.adicionar_cafe(5.0)

# Servir café
cafeteria.servir_cafe(2.0)

# Criar pedidos
pedido1 = cafeteria.criar_pedido({"Café": 5.00, "Pão de Queijo": 3.50}, mesa=1)
pedido2 = cafeteria.criar_pedido({"Capuccino": 7.00, "Bolo": 6.00}, mesa=2)

# Consultar pedidos
cafeteria.consultar_pedido(pedido1)

# Finalizar pedidos
cafeteria.finalizar_pedido(pedido1)

# Consultar pedidos novamente
cafeteria.consultar_pedido(pedido1)

# Desligar a cafeteria
cafeteria.desligar()
