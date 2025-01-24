from mainBTree import main as mainBTree
from mainHash import main as mainHash

def main():
    
    escolha = 0

    while escolha != 3:
        print("\n*     SELECIONE A ESTRUTURA DE DADOS     *\n")
        print("1. Usar BTree")
        print("2. Usar Hash Linear")
        print("3. Sair")
        
        escolha = int(input("Informe sua escolha: "))
        
        if escolha == 1:
            mainBTree()
        elif escolha == 2:
            mainHash()
        elif escolha == 3:
            print("Saindo...")

if __name__ == '__main__':
    main()