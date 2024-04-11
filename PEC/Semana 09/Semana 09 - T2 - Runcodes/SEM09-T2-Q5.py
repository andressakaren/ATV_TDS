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
    q1 = input().upper().strip()
    q2 = input().upper().strip()
    q3 = input().upper().strip()
    q4 = input().upper().strip()
    q5 = input().upper().strip()
    
    total = qst(q1, q2, q3, q4, q5)
    
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