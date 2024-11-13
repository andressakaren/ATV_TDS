# Utilizando o processo de abstração, implemente uma classe em python que represente uma carteira de habilitação. Identifique atributos mutáveis e imutáveis, implemente um construtor da classe e métodos para manipulação dos atributos mutáveis. Faça todas as validações possíveis. Crie objetos para testar os métodos implementados.

# atributos: Nome, Doc Identidade/Emissor/UF, CPF, Data de nascimento, Filiação, permissão, acc, categoria, Num Registro, valodade, data de emissao
# (self, numero, categoria, data_emissao, data_validade, nome, cpf

class ValidarCNH:
    def __init__(self, registro, cpf, nome, data_nascimento, categoria, data_emissao, data_validade):
        # Imutáveis
        self.registro = registro
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.data_emissao = data_emissao
        # Mutáveis
        self.categoria = categoria
        self.data_validade = data_validade
        
        # criar dois métodos para validar: cpf e as datas
        
    def validar_cpf(self):