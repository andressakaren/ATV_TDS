from datetime import datetime

# Utilizando o processo de abstração, implemente uma classe em python que represente uma carteira de habilitação. Identifique atributos mutáveis e imutáveis, implemente um construtor da classe e métodos para manipulação dos atributos mutáveis. Faça todas as validações possíveis. Crie objetos para testar os métodos implementados.

# atributos: Nome, Doc Identidade/Emissor/UF, CPF, Data de nascimento, Filiação, permissão, acc, categoria, Num Registro, valodade, data de emissao
# (self, numero, categoria, data_emissao, data_validade, nome, cpf

class ValidarCNH:
    def __init__(self, registro, cpf, nome, data_nascimento, data_emissao, data_validade, categoria):
        # Imutáveis
        self.registro = registro
        
        ## Lembrar de atribuir o cpf antes de validar, pra garantir que o self.cpf esteja disponível no método validar_cpf()
        self.cpf = cpf 
        ## validar cpf
        if not self.validar_cpf():
            raise ValueError(f'CPF inserido inválido: {self.cpf}')
        
        self.nome = nome
        
        ## validar datas
        if not self.validar_datas(data_nascimento):
            raise ValueError(f"Data de nascimento inválida: {data_nascimento}")
        self.data_nascimento = data_nascimento
        
        if not self.validar_datas(data_emissao):
            raise ValueError(f"Data de emissão inválida: {data_emissao}")
        self.data_emissao = data_emissao
        
        if not self.validar_datas(data_validade):
            raise ValueError(f"Data de validade inválida: {data_validade}")
        self.data_validade = data_validade
       
        # Mutáveis
        self.categoria = categoria
           
    def validar_cpf(self):
        nove_digitos = self.cpf[:9]
        # print(nove_digitos)
        contador_regressivo_1 = 10
        
        resultado_digito_1 = 0
        for digito in nove_digitos:
            resultado_digito_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1
        digito_1 = (resultado_digito_1 * 10) % 11        
        digito_1 = digito_1 if digito_1 <= 9 else 0
        
        dez_digitos = nove_digitos + str(digito_1) # passar pra str pra poder concatenar 
        contador_regressivo_2 = 11
        resultado_digito_2 = 0
        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1
            
        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0
        
        # verificar       
        cpf_calculo = f'{nove_digitos}{digito_1}{digito_2}'
        
        # if cpf_calculo == self.cpf:
        #     return self.cpf
        # else:
        #     return False
        
        return cpf_calculo == self.cpf

    def validar_datas(self, data_str):
        try:
            # tentar converter para o formato DD/MM/AAAA
            data = datetime.strptime(data_str, '%d/%m/%Y')
            return True
        except ValueError:
            return False
        
    def __str__(self):
        return (f'Registro: {self.registro}\n'
                f'CPF: {self.cpf}\n'
                f'Nome: {self.nome}\n'
                f'Data de nascimento: {self.data_nascimento}\n'
                f'Data de emissão: {self.data_emissao}\n'
                f'Data de validade: {self.data_validade}\n'
                f'Categoria: {self.categoria}\n') 

try: 
    obj = ValidarCNH('registro', '05727651344', 'Andressa Karen', '03/02/1998', '10/05/2015', '10/05/2030', 'AB')
    print('CNH válida')
    print()
    print(obj)
except ValueError as e:
    print(e)
    print('CNH inválida')
    
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""