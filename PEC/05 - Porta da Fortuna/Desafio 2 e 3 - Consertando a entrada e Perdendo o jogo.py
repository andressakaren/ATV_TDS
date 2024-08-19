from random import *

jogando = True
pontuacao = 0

print('''
Porta da Fortuna!
=========
      
Existe um super prêmio atrás de uma destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!
  _____   _____   _____
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |   o | |   o | |   o |
 |_____| |_____| |_____|
''')

while jogando == True:
    print("\nEscolha uma porta (1,2 ou 3):")

    portaEscolhida = int(input())

    portaCerta = randint(1,3)

    print ("A porta escolhida foi a", portaEscolhida)
    print ("A porta certa é a", portaCerta)

    if portaEscolhida == portaCerta:
        pontuacao = pontuacao+1
        print ("Parabéns!")
    else:
        print ("Que peninha!")
        pontuacao = 0

    print("\nSua pontuação é:", pontuacao)

    print ("\nVocê quer jogar de novo? (s/n)")
    resposta = input().upper()[0]

    if resposta == 'N':
        jogando = False
        