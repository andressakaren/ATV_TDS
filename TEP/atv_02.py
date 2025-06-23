# Pesquisando na biblioteca oficial do python, implemente um programa para ler um arquivo .csv (Pessoas.csv) em anexo e produza os seguntes relatórios:

# a) Pessoas por cidade (ex: todos de Fortaleza).
# b) Pessoas com idade maior que X agrupados por cidade.
# c) Pessoas entre faixas etárias.
# d) Média de idade das pessoas por cidade

import csv
from collections import defaultdict

file_path = "pessoas.csv"

pessoas = []

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile) 
    for row in reader:
        row['Idade'] = int(row['Idade'])
        pessoas.append(row)

def pessoas_por_cidade(cidade):
    dict_pesspa_por_cidade = [p for p in pessoas if p['Cidade'].lower() == cidade.lower()]
    
    return dict_pesspa_por_cidade

def pessoas_com_idade_maior_X(X):
    resultado = defaultdict(list)
    for p in pessoas:
        if p['Idade'] > X:
            resultado[p['Cidade']].append(p)
    return resultado

def pessoas_por_faixa_etaria():
    faixas = {
        '0-18': [],
        '19-30': [],
        '31-60': [],
        '60+': []
    }
    for p in pessoas:
        idade = p['Idade']
        if idade <= 18:
            faixas['0-18'].append(p)
        elif idade <= 30:
            faixas['19-30'].append(p)
        elif idade <= 60:
            faixas['31-60'].append(p)
        else:
            faixas['60+'].append(p)
    return faixas

def media_idade_por_cidade():
    soma = defaultdict(int)
    contagem = defaultdict(int) # contar qnts pessoas tem em cada cidade
    medias = {}

    for p in pessoas:
        cidade = p['Cidade']
        soma[cidade] += p['Idade']
        contagem[cidade] += 1

    for cidade in soma:
        medias[cidade] = soma[cidade] / contagem[cidade]

    return medias

# a) Pessoas por cidade (ex: todos de Fortaleza).
print(pessoas_por_cidade('Fortaleza'))

# [{'Nome': 'Ana', 'Idade': 30, 'Cidade': 'Fortaleza'}, {'Nome': 'Felipe', 'Idade': 40, 'Cidade': 'Fortaleza'}, {'Nome': 'Gabriela', 'Idade': 19, 'Cidade': 'Fortaleza'}, {'Nome': 'Marina', 'Idade': 26, 'Cidade': 'Fortaleza'}, {'Nome': 'Paulo', 'Idade': 37, 'Cidade': 'Fortaleza'}]
    
# b) Pessoas com idade maior que X agrupados por cidade.
print(dict(pessoas_com_idade_maior_X(20)))

# {'Fortaleza': [{'Nome': 'Ana', 'Idade': 30, 'Cidade': 'Fortaleza'}, {'Nome': 'Felipe', 'Idade': 40, 'Cidade': 'Fortaleza'}, {'Nome': 'Marina', 'Idade': 26, 'Cidade': 'Fortaleza'}, {'Nome': 'Paulo', 'Idade': 37, 'Cidade': 'Fortaleza'}], 'Recife': [{'Nome': 'Bruno', 'Idade': 25, 'Cidade': 'Recife'}, {'Nome': 'Heitor', 'Idade': 33, 'Cidade': 'Recife'}, {'Nome': 'Tiago', 'Idade': 34, 'Cidade': 'Recife'}], 'Salvador': [{'Nome': 'Carla', 'Idade': 28, 'Cidade': 'Salvador'}, {'Nome': 'Isabela', 'Idade': 24, 'Cidade': 'Salvador'}, {'Nome': 'João', 'Idade': 27, 'Cidade': 'Salvador'}, {'Nome': 'Olívia', 'Idade': 29, 'Cidade': 'Salvador'}], 'Belo Horizonte': [{'Nome': 'Daniel', 'Idade': 35, 'Cidade': 'Belo Horizonte'}, {'Nome': 'Lucas', 'Idade': 31, 'Cidade': 'Belo Horizonte'}, {'Nome': 'Ricardo', 'Idade': 36, 'Cidade': 'Belo Horizonte'}], 'Curitiba': [{'Nome': 'Eduarda', 'Idade': 22, 'Cidade': 'Curitiba'}, {'Nome': 'Karla', 'Idade': 21, 'Cidade': 'Curitiba'}, {'Nome': 'Quésia', 'Idade': 23, 'Cidade': 'Curitiba'}]} 

# c) Pessoas entre faixas etárias.
print(pessoas_por_faixa_etaria())

# {'0-18': [{'Nome': 'Nicolas', 'Idade': 18, 'Cidade': 'Recife'}], '19-30': [{'Nome': 'Ana', 'Idade': 30, 'Cidade': 'Fortaleza'}, {'Nome': 'Bruno', 'Idade': 25, 'Cidade': 'Recife'}, {'Nome': 'Carla', 'Idade': 28, 'Cidade': 'Salvador'}, {'Nome': 'Eduarda', 'Idade': 22, 'Cidade': 'Curitiba'}, {'Nome': 'Gabriela', 'Idade': 19, 'Cidade': 'Fortaleza'}, {'Nome': 'Isabela', 'Idade': 24, 'Cidade': 'Salvador'}, {'Nome': 'João', 'Idade': 27, 'Cidade': 'Salvador'}, {'Nome': 'Karla', 'Idade': 21, 'Cidade': 'Curitiba'}, {'Nome': 'Marina', 'Idade': 26, 'Cidade': 'Fortaleza'}, {'Nome': 'Olívia', 'Idade': 29, 'Cidade': 'Salvador'}, {'Nome': 'Quésia', 'Idade': 23, 'Cidade': 'Curitiba'}, {'Nome': 'Sofia', 'Idade': 20, 'Cidade': 'Curitiba'}], '31-60': [{'Nome': 'Daniel', 'Idade': 35, 'Cidade': 'Belo Horizonte'}, {'Nome': 'Felipe', 'Idade': 40, 'Cidade': 'Fortaleza'}, {'Nome': 'Heitor', 'Idade': 33, 'Cidade': 'Recife'}, {'Nome': 'Lucas', 'Idade': 31, 'Cidade': 'Belo Horizonte'}, {'Nome': 'Paulo', 'Idade': 37, 'Cidade': 'Fortaleza'}, {'Nome': 'Ricardo', 'Idade': 36, 'Cidade': 'Belo Horizonte'}, {'Nome': 'Tiago', 'Idade': 34, 'Cidade': 'Recife'}], '60+': []}


# d) Média de idade das pessoas por cidade
print(media_idade_por_cidade())

# {'Fortaleza': 30.4, 'Recife': 27.5, 'Salvador': 27.0, 'Belo Horizonte': 34.0, 'Curitiba': 21.5}