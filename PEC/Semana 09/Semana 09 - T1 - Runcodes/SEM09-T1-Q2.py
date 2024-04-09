def func_operacao(soma, subtracao, mult, divisao, operacao):
       
    if operacao == 1:
        print(soma)
    elif operacao == 2:
        print(subtracao)
    elif operacao == 3:
        print(mult)
    elif operacao == 4:
        print(divisao)
               
         
def main():
    n1 = float(input())
    n2 = float(input())
    operacao = int(input())
    
    soma = n1 + n2
    subtracao = n1 - n2
    mult = n1 * n2
    divisao = n1 / n2
    
    func_operacao(soma, subtracao, mult, divisao, operacao)
      
if __name__ == '__main__':
    main()