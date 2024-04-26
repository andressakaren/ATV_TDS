def uma_funcao():
    for n in reversed(range(11, 100, 11)):
        print(f'{n} bugs no software, pegue onze deles e conserte...')
        print('Tecle "Ctrl+F5"')
        
def main():
    uma_funcao()
    print('Sem erros no software! Está estabilizado!')
    
if __name__ == "__main__":
    main()
