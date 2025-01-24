"""""
---------------------------------------------------------
       Trabalho Final - Banco de Dados II

    Implementação de Árvore B e Hash Linear
    Andressa Caroline Lopes de Assis - RA:0072749
    Hugo César Leal - RA:0072753
---------------------------------------------------------
"""

from hashLinear import HashLinear  # Importa a classe HashLinear do módulo hashLinear
from time import time  # Importa a função time do módulo time para medir o tempo
import os  # Importa o módulo os para manipulação de caminhos de arquivos

# Função para inserir um registro no hash linear
def inserirRegistro(hashLinear, campos):
    # Solicita ao usuário o registro completo, separado por '-'
    registro = [int(x) for x in input("Registro completo (campos separados por -): ").split('-')]
    # Verifica se o tamanho do registro é compatível com o número de campos
    if len(registro) == campos:
        # Insere o registro no hash linear
        hashLinear.inserir(registro[0], registro)
    else:
        # Informa ao usuário que o tamanho é incompatível
        print("Tamanho incompatível com o valor informado.")

# Função para remover um registro do hash linear
def removerRegistro(hashLinear):
    # Solicita ao usuário a chave do registro a ser removido
    chave = int(input("Chave do registro a ser removido: "))
    # Remove o registro do hash linear
    hashLinear.excluir(chave)

# Função para buscar um registro no hash linear
def buscarRegistro(hashLinear):
    # Solicita ao usuário a chave do registro a ser buscado
    chave = int(input("Chave do registro a ser buscado: "))
    # Procura o registro no hash linear
    i, r = hashLinear.procurar(chave)
    # Se o registro for encontrado, imprime-o
    if r:
        print(r)

# Função para mostrar o conteúdo do hash linear
def mostrarHash(hashLinear):
    # Chama o método mostrarHash da classe HashLinear
    hashLinear.mostrarHash()

# Função para executar casos de teste a partir de um arquivo CSV
def casosDeTeste(hashLinear):
    # Obtém o caminho base do arquivo atual
    basePath = os.path.dirname(os.path.abspath(__file__))
    # Constrói o caminho completo para o arquivo de teste
    filePath = os.path.join(basePath, 'testes/teste1.csv')
    # Abre o arquivo de teste para leitura
    with open(filePath, 'r') as arquivo:
        # Marca o tempo de início
        comeco = time()
        # Lê cada linha do arquivo
        for coluna in arquivo:
            # Divide a linha em colunas separadas por vírgula
            registro = coluna.split(',')
            # Se a linha começa com '+', insere o registro
            if registro[0] == '+':
                registro = [int(x) for x in registro[1:]]
                hashLinear.inserir(registro[0], registro)
            # Se a linha começa com '-', remove o registro
            elif registro[0] == '-':
                registro = [int(x) for x in registro[1:]]
                hashLinear.excluir(registro[0])
        # Marca o tempo de fim
        fim = time()
    # Imprime o tempo total decorrido
    print(f"Tempo total decorrido: {fim - comeco}")

# Função principal do programa
def main():
    # Solicita ao usuário a quantidade inicial de buckets
    qntBuckets = int(input("Informe a quantidade de buckets inicial: "))
    # Solicita ao usuário o tamanho da página em bytes
    tamanhoPagina = int(input("Informe o tamanho da página (em bytes): "))
    # Solicita ao usuário a quantidade de campos do registro
    campos = int(input("Quantidade de campos do registro: "))
    # Cria uma instância da classe HashLinear
    hashLinear = HashLinear(qntBuckets, tamanhoPagina, campos)
    
    # Dicionário de ações possíveis no menu
    acoes = {
        1: lambda: casosDeTeste(hashLinear),
        2: lambda: inserirRegistro(hashLinear, campos),
        3: lambda: removerRegistro(hashLinear),
        4: lambda: buscarRegistro(hashLinear),
        5: lambda: mostrarHash(hashLinear),
    }
    
    resp = 0  # Inicializa a variável de resposta do usuário

    # Loop do menu principal
    while resp != 6:
        # Imprime o menu
        print("\n*     HASH LINEAR     *\n")
        print("1. Casos de teste")
        print("2. Inserir registro")
        print("3. Remover registro")
        print("4. Fazer busca")
        print("5. Mostrar hash linear")
        print("6. Voltar")
        
        # Solicita a resposta do usuário
        resp = int(input("Informe sua resposta: "))
        
        # Executa a ação correspondente à resposta do usuário
        if resp in acoes:
            acoes[resp]()

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    main()  # Chama a função principal