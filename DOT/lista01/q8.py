# Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.

def num_ao_cubo(valor):
    return valor ** 3

# função para verificar S ou N
def obter_condicao():
    while True:
        condicao = input('Digite\n S - SIM, continuar\n N - NÃO continuar\n > ').strip().upper()
        
        if condicao in ('S', 'N'):
            return condicao
        
        print('valor inválido. Digite um valor válido.')


# verificar a resposta
while True:
    resposta = obter_condicao()
     
    if resposta == 'N':
        break

    try:
        numero = float(input('Digite um valor: '))
        print(f'O cubo de {numero} = {num_ao_cubo(numero)}')
    except:
        print('Digite um valor válido.')
