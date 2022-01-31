import networkx as nx
import matplotlib.pyplot as plt

from GrafoLista import GrafoLista
from GrafoMatriz import GrafoMatriz

if __name__ == '__main__':
    def plotGrafoMatrix():
        x.add_edges_from(matriz.getTupla())
        nx.draw_networkx(x)
        plt.show()


    def plotGrafoLista():
        x.add_edges_from(lista.getTupla())
        nx.draw_networkx(x)
        plt.show()


    matriz = GrafoMatriz()
    lista = GrafoLista()
    x = nx.Graph()

    # Alternar entre matrix e lista, para os respectivos grafos.
    plotGrafoMatrix()
    # plotGrafoLista()

    # Alternar entre matrix e lista, para os respectivos Histogramas.
    a = matriz.generateHistogram()
    # a = lista.generateHistogram()

    plt.title("Histograma")
    plt.ylabel("Quantidade")
    plt.xlabel("Grau")
    plt.axis([1, 8, 0, 8])
    plt.hist(a, 8, rwidth=0.7, histtype='bar', facecolor='green')
    plt.show()