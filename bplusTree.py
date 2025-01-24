"""""
---------------------------------------------------------
       Trabalho Final - Banco de Dados II

    Implementação de Árvore B e Hash Linear
    Andressa Caroline Lopes de Assis - RA:0072749
    Hugo César Leal - RA:0072753
---------------------------------------------------------
"""

from math import floor, ceil
from sys import getsizeof, maxsize

# Classe que representa um nó da árvore B+
class No:
    def __init__(self, ordem) -> None:
        self.ordem = ordem  # Ordem do nó
        self.eFolha = False  # Indica se o nó é uma folha
        self.pai = None  # Referência ao nó pai
        self.proximo = None  # Referência ao próximo nó (usado em folhas)
        self.anterior = None  # Referência ao nó anterior (usado em folhas)
        self.registros = []  # Lista de registros/chaves do nó
        self.filhos = []  # Lista de filhos do nó

    def getOrdem(self):
        return self.ordem  # Retorna a ordem do nó

    # Insere uma chave no nó (não folha)
    def inserir(self, chave) -> None:
        if not self.registros:
            self.registros.append(chave)
        else:
            for i in range(len(self.registros)):
                if chave < self.registros[i]:
                    self.registros.insert(i, chave)
                    break
            else:
                self.registros.append(chave)

    # Insere uma chave e registro no nó folha
    def inserirFolha(self, chave, registro) -> None:
        if not self.registros:
            self.registros.append(registro)
        else:
            for i in range(len(self.registros)):
                if chave < self.registros[i][0]:
                    self.registros.insert(i, registro)
                    break
            else:
                self.registros.append(registro)

    # Exclui uma chave do nó
    def excluir(self, chave) -> None:
        for i in range(len(self.registros)):
            if self.registros[i][0] == chave:
                self.registros.pop(i)
                break

    # Rotaciona chaves entre nós irmãos
    def rotacionarChaves(self, esquerda, direita, indice, lado):
        if lado == 0:
            direita.inserir(self.registros.pop(indice))
            self.inserir(esquerda.registros.pop(-1))
            no_ = esquerda.filhos.pop(-1)
            no_.pai = direita
            direita.filhos.insert(0, no_)
        elif lado == 1:
            esquerda.inserir(self.registros.pop(indice - 1))
            self.inserir(direita.registros.pop(0))
            no_ = direita.filhos.pop(0)
            no_.pai = esquerda
            esquerda.filhos.append(no_)

    # Junta dois nós
    def juntar(self, no):
        self.registros.extend(no.registros)
        self.proximo = no.proximo
        if no.proximo:
            no.proximo.anterior = self
        del no
        return self

    # Divide um nó folha
    def dividir(self, chave, registro):
        direita = No(self.getOrdem())
        direita.eFolha = True
        meio = ceil(self.ordem / 2)
        self.inserirFolha(chave, registro)
        direita.registros = self.registros[meio:]
        self.registros = self.registros[:meio]
        direita.pai = self.pai
        direita.proximo = self.proximo
        direita.anterior = self
        self.proximo = direita
        if direita.proximo:
            direita.proximo.anterior = direita
        return direita

    # Empresta uma chave para um nó irmão
    def emprestar(self, no, lado) -> None:
        if lado == 0:
            no.inserirFolha(self.registros[-1][0], self.registros.pop())
        elif lado == 1:
            no.inserirFolha(self.registros[0][0], self.registros.pop(0))

# Classe que representa a árvore B+
class ArvoreBPlus:
    def __init__(self, tamanho, quantidade):
        self.ordem, self.ordemPai = self.calcularOrdem(tamanho, quantidade)
        self.raiz = No(self.ordem)
        self.raiz.eFolha = True
    
    # Calcula a ordem da árvore com base no tamanho e quantidade de campos
    def calcularOrdem(self, tamanho, numCampos):
        vetor = [maxsize] * numCampos
        ordemFolha = tamanho // getsizeof(vetor)
        ordemNFolha = tamanho // getsizeof(maxsize)
        return ordemFolha, ordemNFolha
    
    # Insere uma chave e registro na árvore
    def inserir(self, chave, registro):
        no = self.procurar(chave)
        if not self.procurarChave(no, chave):
            if len(no.registros) < no.getOrdem():
                no.inserirFolha(chave, registro)
            else:
                direita = no.dividir(chave, registro)
                if direita:
                    self.inserirPai(no, direita.registros[0][0], direita)
    
    # Insere uma chave no nó pai
    def inserirPai(self, esquerda, chave, direita):
        if self.raiz == esquerda:
            novaRaiz = No(self.ordemPai)
            novaRaiz.registros.append(chave)
            novaRaiz.filhos.extend([esquerda, direita])
            self.raiz = novaRaiz
            esquerda.pai = novaRaiz
            direita.pai = novaRaiz
        else:
            pai = esquerda.pai
            indice = pai.filhos.index(esquerda)
            pai.registros.insert(indice, chave)
            pai.filhos.insert(indice + 1, direita)
            direita.pai = pai
            if len(pai.registros) > pai.getOrdem():
                meio = ceil(pai.getOrdem() / 2)
                novaChave = pai.registros[meio]
                novoNo = No(self.ordemPai)
                novoNo.registros = pai.registros[meio + 1:]
                novoNo.filhos = pai.filhos[meio + 1:]
                pai.registros = pai.registros[:meio]
                pai.filhos = pai.filhos[:meio + 1]
                for filho in novoNo.filhos:
                    filho.pai = novoNo
                if pai == self.raiz:
                    novaRaiz = No(self.ordemPai)
                    novaRaiz.registros.append(novaChave)
                    novaRaiz.filhos.extend([pai, novoNo])
                    self.raiz = novaRaiz
                    pai.pai = novaRaiz
                    novoNo.pai = novaRaiz
                else:
                    self.inserirPai(pai, novaChave, novoNo)
    
    # Exclui uma chave da árvore
    def excluir(self, chave):
        no = self.procurar(chave)
        if no == self.raiz:
            no.excluir(chave)
        else:
            if len(no.registros) > floor(no.getOrdem() / 2):
                no.excluir(chave)
            else:
                self.excluirAuxiliar(no, chave)
    
    # Auxilia na exclusão de uma chave
    def excluirAuxiliar(self, no, chave):
        if len(no.registros) <= floor(no.getOrdem() / 2):
            vizinhoEsquerda = no.anterior
            vizinhoDireita = no.proximo
            if vizinhoEsquerda and vizinhoEsquerda.pai == no.pai and len(vizinhoEsquerda.registros) > floor(no.getOrdem() / 2):
                vizinhoEsquerda.emprestar(no, 0)
            elif vizinhoDireita and vizinhoDireita.pai == no.pai and len(vizinhoDireita.registros) > floor(no.getOrdem() / 2):
                vizinhoDireita.emprestar(no, 1)
            else:
                if vizinhoEsquerda and vizinhoEsquerda.pai == no.pai:
                    noMerge = vizinhoEsquerda.juntar(no)
                elif vizinhoDireita and vizinhoDireita.pai == no.pai:
                    noMerge = no.juntar(vizinhoDireita)
                noPai = noMerge.pai
                if noPai == self.raiz and len(self.raiz.registros) == 1:
                    self.raiz = noMerge
                    noMerge.pai = None
                else:
                    indice = noPai.filhos.index(no)
                    noPai.filhos.pop(indice)
                    if indice > 0:
                        noPai.registros.pop(indice - 1)
                    else:
                        noPai.registros.pop(0)
                    if len(noPai.registros) < floor(noPai.getOrdem() / 2):
                        self.mudarPai(noPai)
        no.excluir(chave)
    
    # Procura um nó que contém a chave
    def procurar(self, chave):
        no = self.raiz
        while not no.eFolha:
            i = 0
            while i < len(no.registros) and chave > no.registros[i]:
                i += 1
            if i < len(no.registros) and chave == no.registros[i]:
                no = no.filhos[i + 1]
            else:
                no = no.filhos[i]
        return no
    
    # Procura uma chave específica em um nó
    def procurarChave(self, no, chave):
        return next((r for r in no.registros if r[0] == chave), None)
    
    # Procura chaves em um intervalo
    def procurarIntervalo(self, no, c1, c2, operador):
        if operador == '>':
            while no:
                for registro in no.registros:
                    if registro[0] > c1:
                        print(registro, end=" <-> ")
                no = no.proximo
        elif operador == '<':
            while no:
                for registro in reversed(no.registros):
                    if registro[0] < c1:
                        print(registro, end=" <-> ")
                no = no.anterior
        elif operador == '|':
            while no:
                for registro in no.registros:
                    if c1 < registro[0] < c2:
                        print(registro, end=" <-> ")
                no = no.proximo
    
    # Muda o pai de um nó
    def mudarPai(self, no):
        noPai = no.pai
        indice = noPai.filhos.index(no)
        
        vizinhoEsquerda = noPai.filhos[indice - 1] if indice > 0 else None
        vizinhoDireita = noPai.filhos[indice + 1] if indice < len(noPai.filhos) - 1 else None
        
        if vizinhoEsquerda and len(vizinhoEsquerda.registros) > floor(vizinhoEsquerda.getOrdem() / 2):
            noPai.rotacionarChaves(vizinhoEsquerda, no, indice - 1, 0)
        elif vizinhoDireita and len(vizinhoDireita.registros) > floor(vizinhoDireita.getOrdem() / 2):
            noPai.rotacionarChaves(no, vizinhoDireita, indice, 1)
        else:
            if vizinhoEsquerda:
                chave = noPai.registros.pop(indice - 1)
                vizinhoEsquerda.registros.append(chave)
                vizinhoEsquerda.registros.extend(no.registros)
                vizinhoEsquerda.filhos.extend(no.filhos)
                for filho in no.filhos:
                    filho.pai = vizinhoEsquerda
                noPai.filhos.pop(indice)
            elif vizinhoDireita:
                chave = noPai.registros.pop(indice)
                no.registros.append(chave)
                no.registros.extend(vizinhoDireita.registros)
                no.filhos.extend(vizinhoDireita.filhos)
                for filho in vizinhoDireita.filhos:
                    filho.pai = no
                noPai.filhos.pop(indice + 1)
            
            if len(noPai.registros) == 0:
                if noPai == self.raiz:
                    self.raiz = vizinhoEsquerda if vizinhoEsquerda else no
                else:
                    self.mudarPai(noPai)
    
    # Mostra a estrutura da árvore
    def mostrarArvore(self):
        if not self.raiz.registros:
            return
        fila = [(self.raiz, 0)]
        nivelAtual = 0
        while fila:
            no, nivel = fila.pop(0)
            if nivel > nivelAtual:
                print()
                nivelAtual = nivel
            if no.eFolha:
                print(no.registros, end=" <-> ")
            else:
                print(no.registros, end="   ")
            for filho in no.filhos:
                fila.append((filho, nivel + 1))
        print()
