from hashLinear import HashLinear
from time import time, sleep
import os

def inserirRegistro(hashLinear, campos):
    registro = [int(x) for x in input("Registro completo (campos separados por -): ").split('-')]
    if len(registro) == campos:
        hashLinear.inserir(registro[0], registro)
    else:
        print("Tamanho incompatível com o valor informado.")

def removerRegistro(hashLinear):
    chave = int(input("Chave do registro a ser removido: "))
    hashLinear.excluir(chave)

def buscarRegistro(hashLinear):
    chave = int(input("Chave do registro a ser buscado: "))
    i, r = hashLinear.procurar(chave)
    if r:
        print(r)

def mostrarHash(hashLinear):
    hashLinear.mostrarHash()

def casosDeTeste(hashLinear):
    basePath = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(basePath, 'testes/teste1.csv')
    with open(filePath, 'r') as arquivo:
        comeco = time()
        for coluna in arquivo:
            registro = coluna.split(',')
            if registro[0] == '+':
                registro = [int(x) for x in registro[1:]]
                hashLinear.inserir(registro[0], registro)
            elif registro[0] == '-':
                registro = [int(x) for x in registro[1:]]
                hashLinear.excluir(registro[0])
        fim = time()
    print(f"Tempo total decorrido: {fim - comeco}")

def main():
    qntBuckets = int(input("Informe a quantidade de buckets inicial: "))
    tamanhoPagina = int(input("Informe o tamanho da página (em bytes): "))
    campos = int(input("Quantidade de campos do registro: "))
    hashLinear = HashLinear(qntBuckets, tamanhoPagina, campos)
    
    acoes = {
        1: lambda: inserirRegistro(hashLinear, campos),
        2: lambda: removerRegistro(hashLinear),
        3: lambda: buscarRegistro(hashLinear),
        4: lambda: mostrarHash(hashLinear),
        5: lambda: casosDeTeste(hashLinear),
        0: lambda: print("====== SAINDO ======") or sleep(2)
    }
    
    while True:
        print("====== MENU DE AÇÕES (HASH LINEAR) ======")
        print("1. Inserir registro")
        print("2. Remover registro")
        print("3. Fazer busca por igualdade")
        print("4. Mostrar hash linear")
        print("5. Casos de teste")
        print("0. Sair do menu")
        
        resp = int(input("Informe sua resposta: "))
        
        if resp in acoes:
            acoes[resp]()
            if resp == 0:
                break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
