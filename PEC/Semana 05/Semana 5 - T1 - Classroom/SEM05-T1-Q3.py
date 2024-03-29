def acrescimo_e_desconto(valor_prod, valor_porcentagem):
    acresc = valor_prod  + (valor_prod * (valor_porcentagem/100))
    descont = valor_prod - (valor_prod * (valor_porcentagem/100))
    return acresc, descont

preco = float(input('Digite o valor do produto: '))
porcentagem = float(input('Digite a porcentagem: '))

acrescimo, desconto = acrescimo_e_desconto(preco, porcentagem)
print(f'O valor do produto acrescido {porcentagem}% é R$ {acrescimo:.2f}, e o valor com o desconto de {porcentagem}% é R$ {desconto:.2f}.')
