class MaquinaDeCafe:
    def __init__(self, capacidade_reservatorio, temperatura_min=70, temperatura_max=100):
        self.__nivel_agua = 0
        self.__capacidade_reservatorio = capacidade_reservatorio
        self.__tipo_cafe = None
        self.__temperatura = temperatura_min
        self.__temperatura_min = temperatura_min
        self.__temperatura_max = temperatura_max
        self.__ligado = False

    def __verificar_status(self):
        if not self.__ligado:
            raise ValueError("A máquina está desligada. Ligue-a para continuar.")

    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
            print("Máquina ligada.")
        else:
            print("A máquina já está ligada.")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("Máquina desligada.")
        else:
            print("A máquina já está desligada.")

    def adicionar_agua(self, quantidade):
        self.__verificar_status()
        if quantidade <= 0:
            print("Quantidade inválida de água.")
            return

        if self.__nivel_agua + quantidade > self.__capacidade_reservatorio:
            print(f"Não é possível adicionar toda a água. O reservatório suporta apenas mais {self.__capacidade_reservatorio - self.__nivel_agua} ml.")
            self.__nivel_agua = self.__capacidade_reservatorio
        else:
            self.__nivel_agua += quantidade
        print(f"Nível de água: {self.__nivel_agua} ml.")

    def aquecer_agua(self, temperatura):
        self.__verificar_status()
        if not (self.__temperatura_min <= temperatura <= self.__temperatura_max):
            print(f"Temperatura inválida. Insira um valor entre {self.__temperatura_min} e {self.__temperatura_max} graus Celsius.")
            return

        self.__temperatura = temperatura
        print(f"Água aquecida a {self.__temperatura} graus Celsius.")

    def selecionar_tipo(self, tipo):
        self.__verificar_status()
        tipos_validos = ["expresso", "cappuccino", "latte"]
        if tipo.lower() not in tipos_validos:
            print(f"Tipo de café inválido. Escolha entre: {', '.join(tipos_validos)}.")
            return

        self.__tipo_cafe = tipo.lower()
        print(f"Tipo de café selecionado: {self.__tipo_cafe}.")

    def preparar_cafe(self):
        self.__verificar_status()
        if self.__nivel_agua <= 0:
            print("Não há água suficiente para preparar o café.")
            return

        if self.__temperatura < self.__temperatura_min:
            print(f"A temperatura da água está muito baixa ({self.__temperatura} graus). Aquecer para no mínimo {self.__temperatura_min} graus Celsius.")
            return

        if not self.__tipo_cafe:
            print("Nenhum tipo de café selecionado.")
            return

        print(f"Preparando um {self.__tipo_cafe}... Pronto! Aproveite seu café.")
        self.__nivel_agua -= 50  # Assumindo que cada café consome 50 ml de água

    def estado_atual(self):
        estado = {
            "Ligado": self.__ligado,
            "Nível de água (ml)": self.__nivel_agua,
            "Temperatura (°C)": self.__temperatura,
            "Tipo de café selecionado": self.__tipo_cafe if self.__tipo_cafe else "Nenhum",
            "Capacidade do reservatório (ml)": self.__capacidade_reservatorio
        }
        return estado

# Criando objetos da classe e simulando o uso
maquina1 = MaquinaDeCafe(1000)
maquina2 = MaquinaDeCafe(1500)
maquina3 = MaquinaDeCafe(2000)

# Imprimindo estados iniciais
for i, maquina in enumerate([maquina1, maquina2, maquina3], start=1):
    
    print(f"Estado inicial da Máquina {i}: {maquina.estado_atual()}")
print()

# Simulação de uso
maquina1.ligar()
maquina1.adicionar_agua(500)
maquina1.aquecer_agua(85)
maquina1.selecionar_tipo("expresso")
maquina1.preparar_cafe()
print(f"Estado final da Máquina 1: {maquina1.estado_atual()}")
print()
maquina2.ligar()
maquina2.adicionar_agua(1000)
maquina2.aquecer_agua(95)
maquina2.selecionar_tipo("cappuccino")
maquina2.preparar_cafe()
print(f"Estado final da Máquina 2: {maquina2.estado_atual()}")

maquina3.ligar()
maquina3.adicionar_agua(1500)
maquina3.aquecer_agua(100)
maquina3.selecionar_tipo("latte")
maquina3.preparar_cafe()
print(f"Estado final da Máquina 3: {maquina3.estado_atual()}")
