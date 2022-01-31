from Aresta import Aresta
from Peso import Peso

class Vertice:

    nome = ""

    vizinhos = []

    def __init__(self, nome):
        self.nome = nome

    def addVizinhos(self, *vertice):

        for e in vertice:

            if isinstance(e, Vertice):

                aresta = Aresta(e)

                x = True

                for i in range(0, len(self.vizinhos)):

                    if self.vizinhos[i].getVertice() == e.nome:
                        x = False

                if aresta in self.vizinhos:
                    x = False

                if x:
                    self.vizinhos.append(aresta)

            if isinstance(e, str):

                vertice = Vertice(e)

                aresta = Aresta(vertice)

                x = True

                for i in range(0, len(self.vizinhos)):

                    if self.vizinhos[i].getVertice() == e:
                        x = False

                if aresta in self.vizinhos:
                    x = False

                if x:
                    self.vizinhos.append(aresta)


    def addVizinhosPeso(self, *values):

        for i in range(0, len(values), 2):

            if isinstance(values[i], Vertice) and isinstance(values[i+1], Peso):

                aresta = Aresta(values[i], values[i+1])

                x = True

                for i in range(0, len(self.vizinhos)):

                    if self.vizinhos[i].getVertice() == values[i].linha:
                        x = False

                if aresta in self.vizinhos:
                    x = False

                if x:
                    self.vizinhos.append(aresta)

            if isinstance(values[i], str) and isinstance(values[i], int):

                v = Vertice(values[i])

                p = Peso(values[i])

                aresta = Aresta(values[i], values[i+1])

                x = True

                for i in range(0, len(self.vizinhos)):

                    if self.vizinhos[i].getVertice() == values[i]:
                        x = False

                if aresta in self.vizinhos:
                    x = False

                if x:
                    self.vizinhos.append(aresta)



    def getVizinhos(self):

        for i in range(0, len(self.vizinhos)):
            print(self.vizinhos[i].getVertice() , self.vizinhos[i].getPeso())

    def getPesoPorVizinho(self, vizinho):

        if isinstance(vizinho, str):

            for i in range(0, len(self.vizinhos)):

                if self.vizinhos[i].getVertice() == vizinho:

                    print(self.vizinhos[i].getPeso())
