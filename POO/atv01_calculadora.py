class Calculadora:    
    def __init__(self, digito1, digito2, operador):   
        # Dá pra fazer condições caso o usuário não digite o valor dentro do intervalo correto e evitar parar o programa. 
        # Usar try Except
        self.digito1 = digito1
        self.digito2 = digito2 
        self.operador = operador    
    
    def operacao(self):       
        if self.operador == '+':
            return self.digito1 + self.digito2
        elif self.operador == '-':
            return self.digito1 - self.digito2
        elif self.operador == '*':
            return self.digito1 - self.digito2
        elif self.operador == '/':
            if self.digito2 != 0:
                return self.digito1 - self.digito2
            else: 
                return 'Erro: divisão por zero não permitida'
        else:
            return 'Operação inválida'  
        
def main():
    
    while True:
        digito1 = float(input('Digite o primeiro numero: '))
        operador = input('Digite o operador (+ - * /): ')
        digito2 = float(input('Digite o segundo numero: '))
        minha_calculadora = Calculadora(digito1, digito2, operador)
        
        resultado = minha_calculadora.operacao()            
        print(f'O resultado da sua operação: {resultado}')
        
        verificador = input('Deseja sair da calculadora [S/N]: ').lower()
        if operador == 's':
            print("Encerrando calculadora...")
            break
        
    
if __name__ == "__main__":
    main()
        