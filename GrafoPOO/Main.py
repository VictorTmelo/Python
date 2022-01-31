from Vertice import Vertice

if __name__ == '__main__':

    a = Vertice("A")
    b = Vertice("B")
    c = Vertice("C")

    a.addVizinhos(b, c)

    a.addVizinhos("B","C")

    a.getVizinhos()
