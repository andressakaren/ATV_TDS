print('''
Qual nome do filme que foi eleito vencedor da categoria melhor filme do Oscar 2024: 
a - Barbie
b - Oppenheimer
c - Minha Mãe é uma Peça!
''')
resposta = input().lower()


if resposta == 'a':
    print('Não foi Barbie, infelizmente!! :(')
elif resposta == 'b':
    print('Correto!!! Nolan não erra uma produção. :)')
elif resposta == 'c':
    print('Não, mas no BR é o melhor que temos.')
else:
    print("Você não escolheu a, b ou c :(")  
    
print("Obrigada por jogar!")