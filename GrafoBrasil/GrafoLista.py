from GrafoMatriz import GrafoMatriz
from No import No


class GrafoLista:
    tupla = []
    estados = []
    grafo = []

    def __init__(self):
        self.estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR",
                        "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

        self.matriz = GrafoMatriz().grafo

        for i in range(0, len(self.estados)):
            self.grafo.append(No(self.estados[i]))

        for i in range(0, len(self.matriz)):
            temp = []

            for j in range(0, len(self.matriz)):
                if self.matriz[i][j] == 1:
                    temp.append(self.estados[j])
            self.grafo[i].addVizinhos(temp)


    def getTupla(self):
        for i in range(0, len(self.grafo)):
            for j in range(0, len(self.grafo[i].vizinhos)):
                for k in range(0, len(self.grafo[i].vizinhos[j])):
                    self.tupla.append([self.grafo[i].linha, self.grafo[i].vizinhos[j][k]])

        return self.tupla


    def generateHistogram(self):
        histogram = []

        for i in range(0, len(self.grafo)):
            histogram.append(len(self.grafo[i].vizinhos[0]))

        return histogram
