"""""
---------------------------------------------------------
       Trabalho Final - Banco de Dados II

    Implementação de Árvore B e Hash Linear
    Andressa Caroline Lopes de Assis - RA:0072749
    Hugo César Leal - RA:0072753
---------------------------------------------------------
"""

from mainBTree import main as mainBTree
from mainHash import main as mainHash

def main():
    """
    Função principal do programa que permite ao usuário selecionar entre diferentes estruturas de dados.
    A função exibe um menu com três opções:
    1. Usar BTree
    2. Usar Hash Linear
    3. Sair
    Dependendo da escolha do usuário, a função chama a função correspondente para a estrutura de dados selecionada ou encerra o programa.
    Variáveis:
        escolha (int): Armazena a escolha do usuário no menu. Inicialmente definida como 0.
    Fluxo:
        - A função entra em um loop while que continua até que o usuário escolha a opção 3 (Sair).
        - Dentro do loop, o menu é exibido e a escolha do usuário é lida.
        - Se a escolha for 1, a função mainBTree() é chamada.
        - Se a escolha for 2, a função mainHash() é chamada.
        - Se a escolha for 3, uma mensagem de saída é exibida e o loop termina.
    """
    
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