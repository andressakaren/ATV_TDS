import re
import sys

while True:
    cpf_digitado = input('Digite o seu cpf: ')
    cpf_digitado = re.sub(
        r'[^0-9]', # Qualquer coisa de 0-9 que não seja um número
        '',
        cpf_digitado)
    
    if len(cpf_digitado) != 11:
        print('Insira um cpf com 11 dígitos para ser válido')
        continue
    
    entrada_eh_sequencial = cpf_digitado == cpf_digitado[0] * len(cpf_digitado)   
    if entrada_eh_sequencial:
        print('Você enviou dados sequenciais.')
        sys.exit()    
    ### PRIMEIRO DÍGITO
        
    # colocar somente os 9 digitos numa lista
    nove_digitos = cpf_digitado[:9]
    
    # multiplicar por contagem regressiva começando por 10 até 2 e somar resultado entre o si
    resultado_dig1 = 0
    contador_regressivo_1 = 10
    for digito in nove_digitos:
        resultado_dig1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1  

    # multiplicar por 10 e pegar o resto da div 11
    vezes10_dig1 = resultado_dig1 * 10
    resto_div11_dig1 = vezes10_dig1 % 11

    # condições verificação 
    digito1_correto = 0
    if resto_div11_dig1 > 9:
        digito1_correto = 0
    else:
        digito1_correto = resto_div11_dig1
        
    ### SEGUNDO DÍGITO
    
    dez_digitos = nove_digitos + str(digito1_correto)

    resultado_dig2 = 0
    contador_regressivo_2 = 11
    for digito in dez_digitos:
        resultado_dig2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1  
    
    vezes10_dig2 = resultado_dig2 * 10
    resto_div11_dig2 = vezes10_dig2 % 11
    
    digito2_correto = 0
    if resto_div11_dig2 > 9:
        digito2_correto = 0
    else:
        digito2_correto = resto_div11_dig2
        
    # print(f'O valor do primeiro dígito é: {digito1_correto}')
    # print(f'O valor do segundo dígito é: {digito2_correto}')
        
    ### VALIDAÇÃO DO CPF
    
    cpf_gerado_pelo_calculo = (f'{nove_digitos}{digito1_correto}{digito2_correto}')
    
    if cpf_digitado == cpf_gerado_pelo_calculo:
        print(f'{cpf_digitado} é Válido.')
    else:
        print('CPF inválido')