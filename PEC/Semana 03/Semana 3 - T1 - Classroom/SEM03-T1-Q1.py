# Faça um programa que pergunte ao usuário quantas fatias de pizza tem e quantos amigos vão dividir a pizza. Mostre
# quantas fatias cada um recebe e quantas sobram.
num_fatias = int(input('Quantas fatias tem a pizza? '))
num_amigos = int(input('Quantos amigos vão dividir a pizza? '))
num_recebe = num_fatias // num_amigos
num_sobram = num_fatias % num_amigos
print(f'Cada amigo recebe {num_recebe} fatias, e sobram {num_sobram} fatias.')
