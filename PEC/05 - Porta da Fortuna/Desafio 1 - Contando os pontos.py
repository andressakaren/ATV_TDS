from random import *

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

jogando = True
tentativas = 0
pontuacao = 0
while True:
    print("\nEscolha uma porta (1,2 ou 3):")
    portaEscolhida = int(input())
    portaCerta = randint(1,3)
    print ("A porta escolhida foi a", portaEscolhida)
    print ("A porta certa é a", portaCerta)

    if portaEscolhida == portaCerta:
        tentativas += 1
        pontuacao +=1
        print (f'Sua pontuação é {pontuacao}')
    else:
        pontuacao = 0
        print (f'Sua pontuação é {pontuacao}')
    
    print ("\nVocê quer jogar de novo? (s/n)")
    resposta = input().lower()[0]
    if resposta == 'n':
        break

print(f'Você adivinhou a porta certa {tentativas} vezes.')