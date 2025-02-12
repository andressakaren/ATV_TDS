# Estrutura das Classes

    1. CompanhiaAerea
    2. Voo
    3. PassagemAerea
    4. Passageiro
    5. ClasseVoo
    6. ClasseEconomica
    7. ClasseExecutiva

## CompanhiaAerea

### Métodos Principais - CompanhiaAerea

    - o Adicionar um voo à companhia.
    - o Listar todos os voos programados.

INFO: A classe é responsável só por gerenciar a companhia, como adcionar voo e listar, além de ser necessário criar o nome da companhia.

    ```python
    class CompanhiaAerea:
        def __init__(self, nome):
            self.nome = nome
            self.voos = []
                
        def adicionar_voo(self, voo):
            self.voos.append(voo)
                
        def listar_voos(self):
            print(f'Voos programados pela companhia {self.nome}: ')
                
            for voo in self.voos:
                voo.exibir_detalhes() # METODO EXIBIR DETALHES POSTERIORMENTE NA CLASSE VOO
    ```

## Voo

### Métodos Principais - Voo

    - adicionar_passagem(passageiro, classe)
    - calcular_total_arrecadado() - total arrecadado pelo voo

INFO: A classe é importante ser criada só pois pode ser reutilizada em outras companhias, não necessáriamente na mesma criada. Pensei somente em numero de voo (ID), origem e destino. Seria interessante tambem um atributo para definir a quantidade?

    ```python
    class Voo:
        def __init__(self, numero, origem, destino):
            self.numero = numero
            self.origem = origem
            self.destino = destino
            self.passagens = []
            
        def adicionar_passagem(self, passageiro, classe):
            if len(self.passagens) >= 5: # LIMITE TESTE
                return # RETORNAR ERRO, TIPO 'VOO LOTADO'
            passagem = PassagemAerea(passageiro, classe)
            self.passagens.append(passagem)
            print(f'Passagem registrada para {passageiro.nome} no voo com destino: {self.destino} e número: {self.numero}.')
                
        def calcular_total_arrecadado(self):
            return sum(passagem.preco for passagem in self.passagens)
        
        def exibir_detalhes(self):
            print(f'Voo {self.numero} ({self.origem} -> {self.destino})')
            
            # DETALHES DE TODAS AS PASSAGENS ??
            
            print(f'Total arrecadado: R$ {self.calcular_total_arrecadado():.2f}')  
    ```

PENDENCIAS:

    - RETORNAR MENSAGEM DE ERRO - LIMITE DE PASSAGENS
    - DETALHAR TODAS AS PASSAGENS
    - DEFINIR UM LIMITE DE PASSAGENS DISPONÍVEIS POR VOO

## PassagemAerea

### Metodos Principais - PassagemAerea

    - Registrar uma passagem comprada por um passageiro.
    - Exibir os detalhes da passagem.

INFO: Representa uma passagem de um passageiro para um voo específico,
contendo informações sobre a classe da passagem e o valor. Para registra uma passagem comprada por um passageiro, precisamos da informação do passageiro e da classe que ele escolheu.

    ``` Python
    class PassagemAerea:
        def __init__(self, passageiro, classe):
            self.passageiro = passageiro
            self.classe = classe
            self.preco = classe.calcular_preco()
            
        def exibir_detalhes(self):
            detalhes = f'Passageiro: {self.passageiro}\n'

            if isinstance(self.classe, ClasseEconomica):
                detalhes += f'Bagagem incluída: {'Sim' if self.classe.bagagem_incluida else 'Não'}\n'

            elif isinstance(self.classe, ClasseExecutiva):
                detalhes += f'Serviço de Bordo: {self.classe.servico_bordo}.\n'
                
            print(detalhes)
    ```

PENDENCIAS:

    - ADICIONAR # Tipo de classe (????) NO DETALHES
    - ...

## Passageiro

### Metodos Principais - Passageiro

    - Não tem descrição DE METODOS no pdf - só add atributos

INFO: Representa um passageiro, armazenando seu nome e documento de
identificação.

    ``` Python
    class Passageiro:
        def __init__(self, nome, documento):
            self.nome = nome
            self.documento = documento
    ```

PENDENCIAS:

    - INTERESSANTE ADD VERIFICAÇÃO DE DOCUMENTO

## ClasseVoo

### Metodos Principais - ClasseVoo

    - calcular_preco() - Retornar o preço da passagem

INFO: Superclasse que representa uma classe de passagem aérea, com um preço base associado.

    ``` Python
    class ClasseVoo:
        def __init__(self, preco):
            self.preco = preco
        
        def calcular_preco(self):
            return self.preco
    ```

## ClasseEconomica

### Metodos Principais - ClasseEconomica

    - calcular_preco() - Retornar o preço da passagem - IMPORTANTE: Saber que não precisa criar um novo metodo aqui e sim chamar da classe Pai que é a ClasseVoo, ou seja, vamos considerar aqui as variações de preço, sobrescrevendo o método da classe ClasseVoo

    ``` Python
        def __init__(self, preco, bagagem_incluida):
            super().__init__(preco)
            self.bagagem_incluida = bagagem_incluida
        
        def calcular_preco(self):
            return self.preco + (200 if self.bagagem_incluida else 0)
    ```

PENDENCIAS:

    - ACHO QUE NÃO TEM K

## ClasseExecutiva

### Metodos Principais - ClasseExecutiva

    - calcular_preco() - Retornar o preço da passagem - IMPORTANTE: Saber que não precisa criar um novo metodo aqui e sim chamar da classe Pai que é a ClasseVoo, ou seja, vamos considerar aqui as variações de preço, sobrescrevendo o método da classe ClasseVoo

    ``` Python
        def __init__(self, preco, servico_bordo):
            super().__init__(preco)
            self.servico_bordo = servico_bordo
        
        def calcular_preco(self):
            return self.preco + 1000
    ```

PENDENCIAS:

    - ACHO QUE NÃO TEM K

## IMPLEMENTAÇÃO EXTRA

    - Criar um método polimórfico para imprimir os detalhes do voo, incluindo passageiros, classe da passagem e total arrecadado. ------ EXIBIR_DETALHES() 
    - Criar um arquivo de testes utilizando pytest, cobrindo diferentes cenários de venda de passagens. ------ EU NÃO SEI FAZER
    - Utilizar exceções para tratar casos como tentativas de compra para voos lotados. ----- NÃO SEI FAZER, SÓ COLOQUEI UM LIMITE EXEMPLO 5
