num_doces = int(input('Insira a quantidade de doces produzidos: '))
num_pacotes = int(input('Insira o número de pacotes disponíveis: '))

quantidade_pacote = num_doces // num_pacotes
print(f'O número de doces em cada pacote é: {quantidade_pacote}.')
