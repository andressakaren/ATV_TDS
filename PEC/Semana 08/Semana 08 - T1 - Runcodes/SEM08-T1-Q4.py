def media_numeros(n1, n2, n3, n4, n5):
    media = (n1 + n2 + n3 + n4 + n5) / 5
    print(f'{media}')    
    if n1 > media:
        print(f'{n1}')    
    if n2 > media:
        print(f'{n2}')       
    if n3 > media:
        print(f'{n3}')       
    if n4 > media:
        print(f'{n4}')       
    if n5 > media:
        print(f'{n5}')     
    
    
def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input()) 
      
    media_numeros(n1, n2, n3, n4, n5)

if __name__ == '__main__':
    main()

