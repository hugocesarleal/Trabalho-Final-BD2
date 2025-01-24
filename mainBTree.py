from bplusTree import ArvoreBPlus
from time import time, sleep
import os

def inserirRegistro(arvore, numCampos):
    registro = [int(r) for r in input("Registro completo (campos separados por '-'): ").split('-')]
    if len(registro) == numCampos:
        arvore.inserir(registro[0], registro)
    else:
        print("Tamanho incompatível com o valor informado.")

def removerRegistro(arvore):
    chave = int(input("Chave do registro a ser removido: "))
    arvore.excluir(chave)

def buscarIgualdade(arvore):
    chave = int(input("Chave do registro a ser buscado: "))
    r = arvore.procurarChave(arvore.procurar(chave), chave)
    if r:
        print(f"Registro: {r}")

def buscarIntervalo(arvore):
    opcao = input("Informe a opção desejada (1 - Maior, 2 - Menor, 3 - Entre dois números): ").upper()
    if opcao == '1':
        valor = int(input("Informe o valor: "))
        arvore.procurarIntervalo(arvore.procurar(valor), valor, 0, '>')
    elif opcao == '2':
        valor = int(input("Informe o valor: "))
        arvore.procurarIntervalo(arvore.procurar(valor), valor, 0, '<')
    elif opcao == '3':
        valor1 = int(input("Informe o primeiro valor: "))
        valor2 = int(input("Informe o segundo valor: "))
        arvore.procurarIntervalo(arvore.procurar(valor1), valor1, valor2, '|')
    else:
        print("Opção inválida.")

def casosTeste(arvore):
    basePath = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(basePath, 'testes/teste1.csv')
    with open(filePath, 'r') as arquivo:
        comeco = time()
        for coluna in arquivo:
            registro = coluna.split(',')
            if registro[0] == '+':
                registro = [int(r) for r in registro[1:]]
                arvore.inserir(registro[0], registro)
            elif registro[0] == '-':
                registro = [int(r) for r in registro[1:]]
                arvore.excluir(registro[0])
        fim = time()
        print(f"Tempo total decorrido: {fim - comeco}")

def main():
    tamanhoPagina = int(input("Informe o tamanho da página em bytes: "))
    numCampos = int(input("Informe quantos campos tem o registro: "))
    
    arvore = ArvoreBPlus(tamanhoPagina, numCampos)
    
    acoes = {
        1: lambda: casosTeste(arvore),
        2: lambda: inserirRegistro(arvore, numCampos),
        3: lambda: removerRegistro(arvore),
        4: lambda: buscarIgualdade(arvore),
        5: lambda: buscarIntervalo(arvore),
        6: lambda: arvore.mostrarArvore(),
    }

    resp = 0
    
    while resp != 7:
        print("\n*     ÁRVORE B+     *\n")
        print("1. Casos de teste")
        print("2. Inserir registro")
        print("3. Remover registro")
        print("4. Busca por igualdade")
        print("5. Busca por intervalo")
        print("6. Mostrar árvore")
        print("7. Sair")
        
        resp = int(input(""))
        
        if resp in acoes:
            acoes[resp]()

if __name__ == '__main__':
    main()
