def acrescimo_e_desconto(valor_prod, valor_porcentagem):
    acresc = valor_prod  + (valor_prod * (valor_porcentagem/100))
    descont = valor_prod - (valor_prod * (valor_porcentagem/100))
    return acresc, descont

preco = float(input())
porcentagem = float(input())

acrescimo, desconto = acrescimo_e_desconto(preco, porcentagem)
print(f'{acrescimo:.2f}')
print(f'{desconto:.2f}')
