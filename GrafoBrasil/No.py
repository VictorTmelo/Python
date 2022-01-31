class No:

    vizinhos = []

    def __init__(self, nome):
        self.nome = nome

    def addVizinho(self, nome):
        self.vizinhos.append(nome)

    def addVizinhos(self, *nomes):
        self.vizinhos = nomes