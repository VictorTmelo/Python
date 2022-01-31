from Peso import Peso
from Vertice import Vertice

class Aresta:

    def __init__(self, *values):

        for e in values:

            if isinstance(e,Vertice):
                self.vertice = e
                self.peso = 0

            if isinstance(e, Peso):
                self.peso = e


    def getVertice(self):
        return self.vertice.nome

    def getPeso(self):
        return self.peso.p