class HashLinear:
    def __init__(self, qntBuckets, tamanhoPagina, campos):
        self.qntBuckets = qntBuckets
        self.tamanhoPagina = tamanhoPagina
        self.campos = campos
        self.tabela = [[] for _ in range(qntBuckets)]

    def hash(self, chave):
        return chave % self.qntBuckets

    def inserir(self, chave, registro):
        indice = self.hash(chave)
        self.tabela[indice].append(registro)

    def excluir(self, chave):
        indice = self.hash(chave)
        self.tabela[indice] = [r for r in self.tabela[indice] if r[0] != chave]

    def procurar(self, chave):
        indice = self.hash(chave)
        for registro in self.tabela[indice]:
            if registro[0] == chave:
                return indice, registro
        return None, None

    def mostrarHash(self):
        for i, bucket in enumerate(self.tabela):
            print(f"Bucket {i}: {bucket}")