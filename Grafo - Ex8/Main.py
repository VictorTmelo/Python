import networkx as nx
import matplotlib.pyplot as plt

from GrafosMatriz import GrafosMatriz

if __name__ == '__main__':
    x = nx.Graph()
    z = nx.Graph()
    y = nx.Graph()

    grafo = GrafosMatriz()

    x.add_edges_from(grafo.getTupla())
    nx.draw_networkx(x)
    plt.show()

    z.add_edges_from(grafo.stackDFS(3))
    nx.draw_networkx(z)
    plt.show()

    y.add_edges_from(grafo.getTuplaConexo())
    nx.draw_networkx(y)
    plt.show()

    grafo.checkConexos()