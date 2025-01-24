from sys import getsizeof, maxsize

class Bucket:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.registros = []
        self.overflow = []
        self.eOverflow = False

    def vazio(self):
        return not self.registros

    def cheio(self):
        return len(self.registros) >= self.tamanho

    def getOverflow(self):
        return self.eOverflow

    def setOverflow(self, eOverflow):
        self.eOverflow = eOverflow

class HashLinear:
    def __init__(self, buckets, tamanho, campos) -> None:
        self.bucketsN0 = buckets
        self.tamanhoBucket = self.calcularTamanhoBucket(tamanho, campos)
        self.buckets = [Bucket(self.tamanhoBucket) for _ in range(buckets)]
        self.nivel = 0
        self.proximo = 0

    def calcularTamanhoBucket(self, tamanho, campos):
        vetor = [maxsize] * campos
        return tamanho // getsizeof(vetor)

    def calcularPosicao(self, chave, nivel):
        if nivel == self.nivel:
            return chave % (self.bucketsN0 * (2 ** self.nivel))
        return chave % (self.bucketsN0 * (2 ** (self.nivel + 1)))

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

    def dividirBucketOverflow(self, overflowBucket, newBucket):
        i = 0
        while i < len(overflowBucket.registros):
            registro = overflowBucket.registros[i]
            posicao = self.calcularPosicao(registro[0], self.nivel + 1)
            if posicao != self.proximo:
                newBucket.registros.append(overflowBucket.registros.pop(i))
            else:
                i += 1

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

    def excluir(self, chave):
        i, bucket = self.procurar(chave)
        if bucket:
            bucket.registros.pop(i)

    def mostrarHash(self):
        for i, bucket in enumerate(self.buckets):
            if bucket.overflow:
                print(f"{i} - {bucket.registros} -> ", end="")
                for overflowBucket in bucket.overflow:
                    print(f"{overflowBucket.registros} -> Overflow", end=" ")
                print()
            else:
                print(f"{i} - {bucket.registros}")