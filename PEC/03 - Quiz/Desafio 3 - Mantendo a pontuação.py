print('''
Q1 - Qual é o nome do leão protagonista em "O Rei Leão"? 
a. Simba
b. Pumba
c. Timão
''')
resposta1 = input().lower() 

def perg_1(resposta1):
    score = 0
    if resposta1 == 'a':
        score = 1
    elif resposta1 == 'b':
        score = 0
    elif resposta1 == 'c':
        score = 0
    else:
        score = 0
    
    return score

   
print('''
Q2 - Quem é a fada madrinha de Cinderela? 
a. Tiana
b. Aurora
c. Fada Azul
''')

resposta2 = input().lower() 
     
def perg_2(resposta2):
    score = 0
    if resposta2 == 'a':
        score = 0
    elif resposta2 == 'b':
        score = 0
    elif resposta2 == 'c':
        score = 1

    else:
        score = 0
    
    return score  

print('''
Q3 - Qual é o nome da pequena peixe protagonista em "A Pequena Sereia"? 
a. Ariel
b. Bella
c. Jasmine
''')
resposta3 = input().lower() 
     
def perg_3(resposta3):
    score = 0
    if resposta3 == 'a':
        score = 1
    elif resposta3 == 'b':
        score = 0
    elif resposta3 == 'c':
        score = 0
    else:
        score = 0
    
    return score 

print('''
Q4 - Qual é o nome do famoso brinquedo cowboy em "Toy Story"? 
a. Buzz Lightyear
b. Woody
c. Sr. Cabeça de Batata
''')
resposta4 = input().lower() 
     
def perg_4(resposta4):
    score = 0
    if resposta4 == 'a':
        score = 0
    elif resposta4 == 'b':
        score = 1
    elif resposta4 == 'c':
        score = 0
    else:
        score = 0
    
    return score  
    
print('''
Q5 - Qual é a princesa de cabelos compridos em "Enrolados"? 
a. Elsa
b. Rapunzel
c. Moana
''')
resposta5 = input().lower() 
    
def perg_5(resposta5):
    score = 0
    if resposta5 == 'a':
        score = 0
    elif resposta5 == 'b':
        score = 1
    elif resposta5 == 'c':
        score = 0
    else:
        score = 0
        
    return score  
    
    
    
print(f'Obrigada por jogar! Seu score foi = {perg_1(resposta1) + perg_2(resposta2) + perg_3(resposta3) + perg_4(resposta4) + perg_5(resposta5)}!! ')
