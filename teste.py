from time import time, sleep
from math import floor, ceil
from sys import getsizeof, maxsize
import os

def calcular_ordem(tamanho, num_campos):
    vetor = [maxsize] * num_campos
    ordem_folha = tamanho // getsizeof(vetor)
    ordem_n_folha = tamanho // getsizeof(maxsize)
    return ordem_folha, ordem_n_folha

def criar_no(ordem):
    return {
        'ordem': ordem,
        'eFolha': False,
        'pai': None,
        'proximo': None,
        'anterior': None,
        'registros': [],
        'filhos': []
    }

def inserir_no(no, chave):
    if len(no['registros']):
        no['registros'].append(chave)
        no['registros'].sort()
    else:
        no['registros'] = [chave]

def inserir_folha(no, chave, registro):
    if len(no['registros']):
        no['registros'].append((chave, registro))
        no['registros'].sort()
    else:
        no['registros'] = [(chave, registro)]

def excluir_no(no, chave):
    if len(no['registros']):
        no['registros'] = [r for r in no['registros'] if r[0] != chave]

def dividir_no(no, chave, registro):
    direita = criar_no(no['ordem'])
    direita['eFolha'] = True
    meio = ceil(no['ordem'] / 2)
    inserir_folha(no, chave, registro)
    direita['registros'] = no['registros'][meio:]
    no['registros'] = no['registros'][:meio]
    direita['pai'] = no['pai']
    direita['proximo'] = no['proximo']
    direita['anterior'] = no
    no['proximo'] = direita
    if direita['proximo']:
        direita['proximo']['anterior'] = direita
    return direita

def procurar_no(raiz, chave):
    no = raiz
    while not no['eFolha']:
        for i, r in enumerate(no['registros']):
            if chave < r:
                no = no['filhos'][i]
                break
        else:
            no = no['filhos'][-1]
    return no

def procurar_chave(no, chave):
    for r in no['registros']:
        if r[0] == chave:
            return r
    return None

def mostrar_arvore(no, nivel=0):
    print(' ' * nivel, no['registros'])
    if not no['eFolha']:
        for filho in no['filhos']:
            mostrar_arvore(filho, nivel + 1)

def main():
    tamanho_pagina = int(input("Informe o tamanho da página em bytes: "))
    num_campos = int(input("Informe quantos campos tem o registro: "))
    ordem_folha, ordem_n_folha = calcular_ordem(tamanho_pagina, num_campos)
    raiz = criar_no(ordem_folha)
    raiz['eFolha'] = True

    while True:
        print("\n====== MENU DE AÇÕES (ÁRVORE B+) ======")
        print("1. Inserir registro")
        print("2. Remover registro")
        print("3. Fazer busca por igualdade")
        print("4. Fazer busca por intervalo")
        print("5. Mostrar árvore B+")
        print("6. Casos de teste")
        print("0. Sair do menu")
        
        resp = int(input("Informe sua resposta: "))
        
        if resp == 1:
            registro = [int(r) for r in input("Registro completo (campos separados por '-'): ").split('-')]
            if len(registro) == num_campos:
                no = procurar_no(raiz, registro[0])
                if not procurar_chave(no, registro[0]):
                    if len(no['registros']) < ordem_folha:
                        inserir_folha(no, registro[0], registro)
                    else:
                        nova_folha = dividir_no(no, registro[0], registro)
                        if no == raiz:
                            nova_raiz = criar_no(ordem_n_folha)
                            nova_raiz['filhos'] = [no, nova_folha]
                            raiz = nova_raiz
                        else:
                            inserir_no(no['pai'], nova_folha['registros'][0][0])
            else:
                print("Tamanho incompatível com o valor informado.")
        
        elif resp == 2:
            chave = int(input("Chave do registro a ser removido: "))
            no = procurar_no(raiz, chave)
            excluir_no(no, chave)
        
        elif resp == 3:
            chave = int(input("Chave do registro a ser buscado: "))
            no = procurar_no(raiz, chave)
            r = procurar_chave(no, chave)
            if r:
                print(f"Registro: {r}")
        
        elif resp == 4:
            print("A - Maior ( > )")
            print("B - Menor ( < )")
            print("C - Entre dois números ( | )")
            opcao = input("Informe a opção desejada, juntamente com o(s) número(s), separados por ',': ").split(',')
            # Implementar busca por intervalo conforme necessário
        
        elif resp == 5:
            mostrar_arvore(raiz)
        
        elif resp == 6:
            arquivo_path = os.path.join(os.path.dirname(__file__), 'testes', 'teste1.csv')
            arquivo = open(arquivo_path, 'r')
            comeco = time()
            for coluna in arquivo:
                # Implementar casos de teste conforme necessário
                pass
            fim = time()
            print(f"Tempo total decorrido: {fim - comeco}")
            arquivo.close()
        
        elif resp == 0:
            print("====== SAINDO ======")
            sleep(2)
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()