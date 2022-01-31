import networkx as nx
import matplotlib.pyplot as plt

from GrafosMatriz import GrafosMatriz

if __name__ == '__main__':
    x = nx.Graph()

    grafo = GrafosMatriz()

    x.add_edges_from(grafo.getTupla())
    nx.draw_networkx(x)
    plt.show()

    grafo.dijkstraVictor(4)

    grafo.dijkstra(grafo.grafo, grafo.estados, 4)
