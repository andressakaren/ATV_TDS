import random


class Pedra_Papel_Tesoura:
    def __init__(self, escolha_usuario=None, escolha_computador=None):
        self.escolha_usuario = escolha_usuario
        self.escolha_computador = escolha_computador

    def obter_escolha_usuario(self):
        escolha = input(
            "Escolha Pedra, Papel ou Tesoura (ou 'sair' para encerrar): ").strip().lower()
        if escolha in ['pedra', 'papel', 'tesoura']:
            self.escolha_usuario = escolha
        elif escolha == 'sair':
            return None
        else:
            print("Escolha inválida. Tente novamente.")
            return self.obter_escolha_usuario()
        return self.escolha_usuario

    def obter_escolha_computador(self):
        self.escolha_computador = random.choice(['pedra', 'papel', 'tesoura'])
        return self.escolha_computador

    def determinar_vencedor(self):
        if self.escolha_usuario == self.escolha_computador:
            return "Empate!"
        elif (self.escolha_usuario == 'pedra' and self.escolha_computador == 'tesoura') or \
             (self.escolha_usuario == 'papel' and self.escolha_computador == 'pedra') or \
             (self.escolha_usuario == 'tesoura' and self.escolha_computador == 'papel'):
            return "Você venceu!"
        else:
            return "O computador venceu!"


def main():
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    while True:
        jogo = Pedra_Papel_Tesoura()
        usuario = jogo.obter_escolha_usuario()
        if usuario is None:
            print("Encerrando o jogo...")
            break

        computador = jogo.obter_escolha_computador()
        print(f"Computador escolheu: {computador}")

        resultado = jogo.determinar_vencedor()
        print(resultado)


# Chama a função principal
main()
