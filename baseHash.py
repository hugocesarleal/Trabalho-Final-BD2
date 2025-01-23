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
