"""""
---------------------------------------------------------
       Trabalho Final - Banco de Dados II

    Implementação de Árvore B e Hash Linear
    Andressa Caroline Lopes de Assis - RA:0072749
    Hugo César Leal - RA:0072753
---------------------------------------------------------
"""

from sys import getsizeof, maxsize

# Classe que representa um balde (bucket) na tabela hash
class Bucket:
    def __init__(self, tamanho):
        self.tamanho = tamanho  # Tamanho máximo do balde
        self.registros = []  # Lista de registros armazenados no balde
        self.overflow = []  # Lista de baldes de overflow
        self.eOverflow = False  # Indicador de overflow

    # Verifica se o balde está vazio
    def vazio(self):
        return not self.registros

    # Verifica se o balde está cheio
    def cheio(self):
        return len(self.registros) >= self.tamanho

    # Retorna o estado de overflow do balde
    def getOverflow(self):
        return self.eOverflow

    # Define o estado de overflow do balde
    def setOverflow(self, eOverflow):
        self.eOverflow = eOverflow

# Classe que representa a tabela hash com endereçamento linear
class HashLinear:
    def __init__(self, buckets, tamanho, campos) -> None:
        self.bucketsN0 = buckets  # Número inicial de baldes
        self.tamanhoBucket = self.calcularTamanhoBucket(tamanho, campos)  # Tamanho de cada balde
        self.buckets = [Bucket(self.tamanhoBucket) for _ in range(buckets)]  # Lista de baldes
        self.nivel = 0  # Nível atual da tabela hash
        self.proximo = 0  # Próximo balde a ser dividido

    # Calcula o tamanho de cada balde com base no tamanho total e no número de campos
    def calcularTamanhoBucket(self, tamanho, campos):
        vetor = [maxsize] * campos
        return tamanho // getsizeof(vetor)

    # Calcula a posição do balde para uma dada chave e nível
    def calcularPosicao(self, chave, nivel):
        if nivel == self.nivel:
            return chave % (self.bucketsN0 * (2 ** self.nivel))
        return chave % (self.bucketsN0 * (2 ** (self.nivel + 1)))

    # Insere um registro na tabela hash
    def inserir(self, chave, registro):
        posicao = self.calcularPosicao(chave, self.nivel)
        if posicao < self.proximo:
            posicao = self.calcularPosicao(chave, self.nivel + 1)
        
        bucket = self.buckets[posicao]
        if bucket.cheio():
            self.tratarOverflow(posicao, registro)
        else:
            bucket.registros.append(registro)

        if posicao == self.proximo and bucket.cheio():
            self.dividirBucket()
            self.proximo += 1
            if self.proximo == self.bucketsN0 * (2 ** self.nivel):
                self.nivel += 1
                self.proximo = 0

    # Trata o caso de overflow ao inserir um registro
    def tratarOverflow(self, posicao, registro):
        bucket = self.buckets[posicao]
        if not bucket.getOverflow():
            overflowBucket = Bucket(self.tamanhoBucket)
            overflowBucket.registros.append(registro)
            bucket.overflow.append(overflowBucket)
            bucket.setOverflow(True)
        else:
            for overflowBucket in bucket.overflow:
                if not overflowBucket.cheio():
                    overflowBucket.registros.append(registro)
                    return
            newOverflowBucket = Bucket(self.tamanhoBucket)
            newOverflowBucket.registros.append(registro)
            bucket.overflow.append(newOverflowBucket)

    # Divide um balde quando ele está cheio
    def dividirBucket(self):
        bucket = self.buckets[self.proximo]
        newBucket = Bucket(self.tamanhoBucket)
        self.buckets.append(newBucket)
        i = 0
        while i < len(bucket.registros):
            registro = bucket.registros[i]
            posicao = self.calcularPosicao(registro[0], self.nivel + 1)
            if posicao != self.proximo:
                newBucket.registros.append(bucket.registros.pop(i))
            else:
                i += 1
        if bucket.eOverflow:
            for overflowBucket in bucket.overflow:
                self.dividirBucketOverflow(overflowBucket, newBucket)

    # Divide os registros de overflow entre os baldes
    def dividirBucketOverflow(self, overflowBucket, newBucket):
        i = 0
        while i < len(overflowBucket.registros):
            registro = overflowBucket.registros[i]
            posicao = self.calcularPosicao(registro[0], self.nivel + 1)
            if posicao != self.proximo:
                newBucket.registros.append(overflowBucket.registros.pop(i))
            else:
                i += 1

    # Procura um registro na tabela hash pela chave
    def procurar(self, chave):
        posicao = self.calcularPosicao(chave, self.nivel)
        if posicao < self.proximo:
            posicao = self.calcularPosicao(chave, self.nivel + 1)
        
        bucket = self.buckets[posicao]
        for i, registro in enumerate(bucket.registros):
            if registro[0] == chave:
                return i, bucket
        
        for overflowBucket in bucket.overflow:
            for i, registro in enumerate(overflowBucket.registros):
                if registro[0] == chave:
                    return i, overflowBucket
        
        return None, None

    # Exclui um registro da tabela hash pela chave
    def excluir(self, chave):
        i, bucket = self.procurar(chave)
        if bucket:
            bucket.registros.pop(i)

    # Mostra o estado atual da tabela hash
    def mostrarHash(self):
        for i, bucket in enumerate(self.buckets):
            if bucket.overflow:
                print(f"{i} - {bucket.registros} -> ", end="")
                for overflowBucket in bucket.overflow:
                    print(f"{overflowBucket.registros} -> Overflow", end=" ")
                print()
            else:
                print(f"{i} - {bucket.registros}")