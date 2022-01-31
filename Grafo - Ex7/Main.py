import networkx as nx
import matplotlib.pyplot as plt

from GrafosMatriz import GrafosMatriz

if __name__ == '__main__':

    x = nx.Graph()
    z = nx.Graph()

    grafo = GrafosMatriz()

    x.add_edges_from(grafo.getTupla())
    nx.draw_networkx(x)
    plt.show()

    z.add_edges_from(grafo.DFS(0))
    nx.draw_networkx(z)
    plt.show()