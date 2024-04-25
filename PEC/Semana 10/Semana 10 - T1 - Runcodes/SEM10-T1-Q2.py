def main():
    par = 0
    impar = 0 
    
    for num in range(100):
        num = int(input())
        if num % 2 == 0:
            par += 1
        else:
            impar += 1     
    print(f'{par}\n{impar}')

    
if __name__ == "__main__":
    main()    