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
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    operacao = int(input('''Escolha a operação que deseja executar:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
'''))
    
    soma = n1 + n2
    subtracao = n1 - n2
    mult = n1 * n2
    divisao = n1 / n2
    print('O resultado da operação escolhida é: ')
    func_operacao(soma, subtracao, mult, divisao, operacao)
      
if __name__ == '__main__':
    main()