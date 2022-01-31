import networkx as nx
import matplotlib.pyplot as plt

from GrafosMatriz import GrafosMatriz

if __name__ == '__main__':
    grafos = GrafosMatriz()

    grafos.dirac(0)
    grafos.ore(0)
    grafos.bondy(0)

    print("")

    grafos.dirac(1)
    grafos.ore(1)
    grafos.bondy(1)

    print("")

    grafos.dirac(2)
    grafos.ore(2)
    grafos.bondy(2)

    print("")

    grafos.dirac(3)
    grafos.ore(3)
    grafos.bondy(3)

    print("")

    grafos.dirac(4)
    grafos.ore(4)
    grafos.bondy(4)