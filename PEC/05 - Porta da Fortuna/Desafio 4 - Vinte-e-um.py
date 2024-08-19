from random import *

jogando = True
pontuacao = 0

print('''
Vinte e um!
=========
      
Tente fazer exatamente 21 pontos!
''')

while jogando == True:

    proxNum = randint(1,10)
    print("\nSeu próximo número é:", proxNum)
    print("Sua pontuação agora é:", pontuacao)

    print ("\nGostaria de somar mais um número? (s/n)")
    resposta = input().upper()[0]

    if resposta == 'S':
        pontuacao = pontuacao + proxNum 

    if resposta == 'N':
        jogando = False

print(f'\nSua pontuação final é: {pontuacao}')
if pontuacao != 21:
    print('Que pena!!')
if pontuacao == 21:
    print('VOCÊ VENCEU!!')