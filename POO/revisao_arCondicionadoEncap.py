class ArCondicionado:
    # Método inicializador
    def __init__(self, temperatura=20, velocidade=3, modo='Automático', ligado=False):
        self.__temperatura = temperatura
        self.__velocidade = velocidade
        self.__modo = modo
        self.__ligado = ligado

    def __str__(self) -> str:
        if self.__ligado:
            return f'APARELHO LIGADO\nModo: {self.__modo}\nTemperatura: {self.__temperatura}°C\nVelocidade: {self.__velocidade}\n'
        else:
            return f'APARELHO DESLIGADO\n'

    # Propriedade para temperatura
    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor < 18:
            self.__temperatura = 18
        elif valor > 28:
            self.__temperatura = 28
        else:
            self.__temperatura = valor

    # Propriedade para velocidade
    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, valor):
        if valor < 1:
            self.__velocidade = 1
        elif valor > 5:
            self.__velocidade = 5
        else:
            self.__velocidade = valor

    # Propriedade para modo
    @property
    def modo(self):
        return self.__modo

    @modo.setter
    def modo(self, valor):
        if valor in ['Frio', 'Ventilar', 'Automático']:
            self.__modo = valor
        else:
            raise ValueError('Modo inválido. Opções válidas: Frio, Ventilar, Automático.')

    # Propriedade para ligado
    @property
    def ligado(self):
        return self.__ligado

    @ligado.setter
    def ligado(self, valor):
        if isinstance(valor, bool):
            self.__ligado = valor
        else:
            raise ValueError('O atributo "ligado" deve ser um valor booleano.')

    # Métodos para ligar e desligar
    def ligar(self):
        if self.__ligado:
            print('Aparelho já está ligado.')
        else:
            self.__ligado = True
        print(self)

    def desligar(self):
        if not self.__ligado:
            print('Aparelho já está desligado.')
        else:
            self.__ligado = False
        print(self)

    # Métodos de ajuste de temperatura
    def aumentar_temperatura(self):
        temp = int(input('Em quantos graus deseja aumentar a temperatura?\n'))
        self.temperatura += temp
        print(self)

    def diminuir_temperatura(self):
        temp = int(input('Em quantos graus deseja diminuir a temperatura?\n'))
        self.temperatura -= temp
        print(self)

    # Métodos de ajuste de velocidade
    def aumentar_velocidade(self):
        self.velocidade += 1
        print(self)

    def diminuir_velocidade(self):
        self.velocidade -= 1
        print(self)

    # Método para mudar o modo
    def mudar_modo(self):
        op_modo = int(input('Informe a opção desejada:\n   1 - Frio\n   2 - Ventilar\n   3 - Automático\n'))
        modos = {1: 'Frio', 2: 'Ventilar', 3: 'Automático'}
        if op_modo in modos:
            self.modo = modos[op_modo]
        else:
            print('Opção inválida.')
        print(self)


def operacao(aparelho):
    while True:
        op_operacao = int(input('Informe a operação desejada:\n   1 - Sair\n   2 - Ligar o aparelho\n   3 - Desligar o aparelho\n   4 - Aumentar a temperatura\n   5 - Diminuir a temperatura\n   6 - Aumentar a velocidade\n   7 - Diminuir a velocidade\n   8 - Mudar o modo\n'))
        if op_operacao == 1:
            print(aparelho)
            break
        elif op_operacao == 2:
            aparelho.ligar()
        elif op_operacao == 3:
            aparelho.desligar()
        elif op_operacao == 4:
            aparelho.aumentar_temperatura()
        elif op_operacao == 5:
            aparelho.diminuir_temperatura()
        elif op_operacao == 6:
            aparelho.aumentar_velocidade()
        elif op_operacao == 7:
            aparelho.diminuir_velocidade()
        elif op_operacao == 8:
            aparelho.mudar_modo()
        else:
            print('Opção inválida.')

def main():
    aparelho = ArCondicionado()
    print(aparelho)
    operacao(aparelho)

if __name__ == '__main__':
    main()


# Exercício – Implementação da Classe Ar-Condicionado
# OBS: Implementar no código tudo que foi visto até agora na disciplina: Construtores,
# atributos opcionais, encapsulamento, ...)
# Fazer as validações necessárias
# Requisitos:
# 1. Classe ArCondicionado
# o atributos:
# ▪ temp_min:
# ▪ temp_max:
# ▪ vel_min:
# ▪ vel_max:
# ▪ temperatura: <temperatura_escolhida dentro dos limites>
# ▪ velocidade: <velocidade escolhida dentro dos limites>
# ▪ modo: <’automático’/’frio’/’ventilar’>
# ▪ ligado: True/False
# 2. Métodos a serem implementados:
# o ligar() :
# o desligar() :
# o aumentar_temperatura() :
# o diminuir_temperatura() :
# o aumentar_velocidade() :
# o diminuir_velocidade() :
# o mudar_modo(modo) : No modo automático, não é permitido alterar a
# velocidade

# 3. Crie pelo menos 3 objetos, imprima seus estados iniciais, execute os métodos e depois
# imprima seus estados finais.