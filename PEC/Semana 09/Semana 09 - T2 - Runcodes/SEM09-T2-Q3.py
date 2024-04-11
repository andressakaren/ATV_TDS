def data_funcao(data):
    ano = data % 10000
    data = data // 10000
    mes = data % 100
    data = data // 100
    dia = data
    
    # se ano bissexto (fev 29)
    if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
        # condição de 4 digitos AAAA
        if (1000 <= ano <= 9999) and (1 <= mes <= 12):
            # para mes fev = 29
            if mes == 2:
                return True if (0 < dia <= 29) else False
            else:    
                # para mes = 31
                if mes in [1,3,5,7,8,10,12]:
                    return True if (0 < dia <= 31) else False
                # para mes = 30
                if mes in [4,6,9,11]:
                    return True if (0 < dia <= 30) else False
        else:
            return False
        
    # Se NAO ano bissexto (fev 28)
    else:
        # condição de 4 digitos AAAA
        if (1000 <= ano <= 9999) and (1 <= mes <= 12): 
            # para mes fev = 28
            if mes == 2:
                return True if (0 < dia <= 28) else False
            else:    
                # para mes = 31
                if mes in [1,3,5,7,8,10,12]:
                    return True if (0 < dia <= 31) else False
                # para mes = 30
                if mes in [4,6,9,11]:
                    return True if (0 < dia <= 30) else False
        else:
            return False
            
def main():
    data = int(input())
    print(f'{data_funcao(data)}')
    
if __name__ == '__main__':
    main()    