import networkx as nx
import matplotlib.pyplot as plt

from GrafosMatriz import GrafosMatriz

if __name__ == '__main__':
    x = nx.Graph()

    grafo = GrafosMatriz()

    x.add_edges_from(grafo.BFS(2))
    nx.draw_networkx(x)
    plt.show()