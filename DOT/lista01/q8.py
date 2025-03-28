# Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.

def num_ao_cubo(valor):
    return valor ** 3

# verificar S ou N
while True:
    try:
        condicao = input('Digite\n S - SIM, continuar\n N - NÃO continuar\n > ').upper()
        
        if condicao == 'N':
            break        
        
        if condicao == 'S':
            numero = float(input('Digite um valor: '))
            print(num_ao_cubo(numero))
            
        print('Digite um valor válido.')

    except:
        print('valor inválido. Digite um valor válido.')

