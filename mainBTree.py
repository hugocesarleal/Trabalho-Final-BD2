"""""
---------------------------------------------------------
       Trabalho Final - Banco de Dados II

    Implementação de Árvore B e Hash Linear
    Andressa Caroline Lopes de Assis - RA:0072749
    Hugo César Leal - RA:0072753
---------------------------------------------------------
"""

from bPlusTree import ArvoreBPlus  # Importa a classe ArvoreBPlus do módulo bPlusTree
from time import time  # Importa a função time do módulo time para medir o tempo de execução
import os  # Importa o módulo os para manipulação de caminhos de arquivos

# Função para inserir um registro na árvore B+
def inserirRegistro(arvore, numCampos):
    # Solicita ao usuário o registro completo, separado por '-'
    registro = [int(r) for r in input("Registro completo (campos separados por '-'): ").split('-')]
    # Verifica se o número de campos do registro é igual ao esperado
    if len(registro) == numCampos:
        # Insere o registro na árvore
        arvore.inserir(registro[0], registro)
    else:
        # Exibe mensagem de erro se o número de campos for incompatível
        print("Tamanho incompatível com o valor informado.")

# Função para remover um registro da árvore B+
def removerRegistro(arvore):
    # Solicita ao usuário a chave do registro a ser removido
    chave = int(input("Chave do registro a ser removido: "))
    # Remove o registro da árvore
    arvore.excluir(chave)

# Função para buscar um registro por igualdade na árvore B+
def buscarIgualdade(arvore):
    # Solicita ao usuário a chave do registro a ser buscado
    chave = int(input("Chave do registro a ser buscado: "))
    # Procura o registro na árvore
    r = arvore.procurarChave(arvore.procurar(chave), chave)
    # Se o registro for encontrado, exibe-o
    if r:
        print(f"Registro: {r}")

# Função para buscar registros por intervalo na árvore B+
def buscarIntervalo(arvore):
    # Solicita ao usuário a opção de busca por intervalo
    opcao = input("Informe a opção desejada (1 - Maior, 2 - Menor, 3 - Entre dois números): ").upper()
    if opcao == '1':
        # Busca registros maiores que um valor
        valor = int(input("Informe o valor: "))
        arvore.procurarIntervalo(arvore.procurar(valor), valor, 0, '>')
    elif opcao == '2':
        # Busca registros menores que um valor
        valor = int(input("Informe o valor: "))
        arvore.procurarIntervalo(arvore.procurar(valor), valor, 0, '<')
    elif opcao == '3':
        # Busca registros entre dois valores
        valor1 = int(input("Informe o primeiro valor: "))
        valor2 = int(input("Informe o segundo valor: "))
        arvore.procurarIntervalo(arvore.procurar(valor1), valor1, valor2, '|')
    else:
        # Exibe mensagem de erro se a opção for inválida
        print("Opção inválida.")

# Função para executar casos de teste a partir de um arquivo CSV
def casosTeste(arvore):
    # Obtém o caminho do arquivo de teste
    basePath = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(basePath, 'testes/teste1.csv')
    # Abre o arquivo de teste
    with open(filePath, 'r') as arquivo:
        comeco = time()  # Marca o início do tempo de execução
        for coluna in arquivo:
            registro = coluna.split(',')
            if registro[0] == '+':
                # Insere registros indicados por '+'
                registro = [int(r) for r in registro[1:]]
                arvore.inserir(registro[0], registro)
            elif registro[0] == '-':
                # Remove registros indicados por '-'
                registro = [int(r) for r in registro[1:]]
                arvore.excluir(registro[0])
        fim = time()  # Marca o fim do tempo de execução
        print(f"Tempo total decorrido: {fim - comeco}")  # Exibe o tempo total decorrido

# Função principal do programa
def main():
    # Solicita ao usuário o tamanho da página em bytes e o número de campos do registro
    tamanhoPagina = int(input("Informe o tamanho da página em bytes: "))
    numCampos = int(input("Informe quantos campos tem o registro: "))
    
    # Cria uma instância da árvore B+
    arvore = ArvoreBPlus(tamanhoPagina, numCampos)
    
    # Dicionário de ações disponíveis no menu
    acoes = {
        1: lambda: casosTeste(arvore),
        2: lambda: inserirRegistro(arvore, numCampos),
        3: lambda: removerRegistro(arvore),
        4: lambda: buscarIgualdade(arvore),
        5: lambda: buscarIntervalo(arvore),
        6: lambda: arvore.mostrarArvore(),
    }

    resp = 0  # Inicializa a variável de resposta do menu
    
    # Loop do menu principal
    while resp != 7:
        print("\n*     ÁRVORE B+     *\n")
        print("1. Casos de teste")
        print("2. Inserir registro")
        print("3. Remover registro")
        print("4. Busca por igualdade")
        print("5. Busca por intervalo")
        print("6. Mostrar árvore")
        print("7. Voltar")
        
        resp = int(input(""))  # Solicita ao usuário a opção desejada
        
        if resp in acoes:
            acoes[resp]()  # Executa a ação correspondente à opção escolhida

# Executa a função principal se o script for executado diretamente
if __name__ == '__main__':
    main()
