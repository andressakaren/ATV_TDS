def qst(q1, q2, q3, q4, q5):
    total = 0
    if q1 == 'S':
        total += 1
    if q2 == 'S':
        total += 1
    if q3 == 'S':
        total += 1
    if q4 == 'S':
        total += 1
    if q5 == 'S':
        total += 1
    return total            

def main():
    q1 = input("Telefonou para a vítima ? S ou N: ").upper().strip()
    q2 = input("Esteve no local do crime ? S ou N: ").upper().strip()
    q3 = input("Mora perto da vítima ? S ou N: ").upper().strip()
    q4 = input("Devia para a vítima ? S ou N: " ).upper().strip()
    q5 = input("Já trabalhou com a vítima ? S ou N: " ).upper().strip()
    
    total = qst(q1, q2, q3, q4, q5)
    print(f'O resultado do questionário decretou: ')
    if total == 2:
        print('Suspeito')
    elif total == 3 or total == 4:
        print('Cúmplice')
    elif total == 5:
        print('Assassino')
    else:
        print('Inocente')
    
    
    
if __name__ == '__main__':
    main()