class Calculadora:
    digito1 = None
    digito2 = None
    operadores = None
    resultado = None     
    
    def operacao(self, digito1, digito2, operador):
        
        if operador == '+':
            self.resultado = digito1 + digito2
        elif operador == '-':
            self.resultado = digito1 - digito2
        elif operador == '*':
            self.resultado = digito1 * digito2
        elif operador == '/':
            self.resultado = digito1 / digito2
            
        return self.resultado    
        
def main():
    minha_calculadora = Calculadora()
    
    digito1 = int(input('Digite o primeiro numero: '))
    digito2 = int(input('Digite o segundo numero: '))
    operadores = input('Digite o operador (+ - * /): ')
    
    resultado = minha_calculadora.operacao(digito1, digito2, operadores)    
    
    print(f'O resultado da sua operação: {resultado}')
    
if __name__ == "__main__":
    main()
        