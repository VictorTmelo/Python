import networkx as nx
import matplotlib.pyplot as plt

from GrafosMatriz import GrafosMatriz

if __name__ == '__main__':

    grafos = GrafosMatriz()

    grafos.euler(0)
    grafos.euler(1)
    grafos.euler(2)
    grafos.euler(3)
    grafos.euler(4)
