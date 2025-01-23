from math import ceil

class No:
    def __init__(self, ordem) -> None:
        self.ordem = ordem
        self.eFolha = False
        self.pai = None
        self.proximo = None
        self.anterior = None
        self.registros = []
        self.filhos = []

    def getOrdem(self):
        return self.ordem

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

    def excluir(self, chave) -> None:
        for i in range(len(self.registros)):
            if self.registros[i][0] == chave:
                self.registros.pop(i)
                break

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

    def juntar(self, no):
        self.registros.extend(no.registros)
        self.proximo = no.proximo
        if no.proximo:
            no.proximo.anterior = self
        del no
        return self

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

    def emprestar(self, no, lado) -> None:
        if lado == 0:
            no.inserirFolha(self.registros[-1][0], self.registros.pop())
        elif lado == 1:
            no.inserirFolha(self.registros[0][0], self.registros.pop(0))
