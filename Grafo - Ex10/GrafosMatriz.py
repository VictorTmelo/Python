import math

class GrafosMatriz:
    grafo = [[0, 6, 0, 7, 0],
             [0, 0, 5, 8, -4],
             [0, -2, 0, 0, 0],
             [0, 0, -3, 0, 9],
             [0, 0, 7, 0, 0]]

    grafo2 = [[0, 5, 7, 1, 0, 0, 0],
              [0, 0, 2, 0, 0, 0, 0],
              [0, 0, 0, 6, 5, 0, 0],
              [0, 3, 0, 0, 0, 5, 3],
              [0, 0, 0, 0, 0, 4, 0],
              [0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0]]

    grafo3 = [[0, 0, 0, 0, 5, 1, 0, 0, 0, 0, 0, 2, 0, 0],
              [0, 0, 11, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0],
              [0, 0, 0, 3, 0, 3, 5, 0, 0, 6, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
              [0, 1, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 4, 0],
              [0, 0, 0, 4, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0],
              [0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 8, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0]]

    grafo4 = [[0, 3, 0, 5, 0, 2, 0, 0, 0, 0, 0],
              [0, 0, -4, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
              [0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, -3, 0, 0, 0, 8, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, -6, 0, 7, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
              [0, 0, 0, 0, 0, 0, 0, 0, -8, 0, 0]]

    grafo5 = [[0, 3, 0],
              [-5, 0, 3],
              [0, 0, 0]]

    grafo6 = [[0, 2, 0, 0],
              [0, 0, -1, 3],
              [-3, 0, 0, -1],
              [0, 0, 0, 0]]

    grafo7 = [[0, 1, 3, 0, 0, 0],
              [0, 0, 0, 3, 2, 0],
              [0, 0, 0, 2, 0, 0],
              [0, 0, 0, 0, -1, 2],
              [0, 0, 0, -3, 0, 0],
              [0, 0, 0, 0, 3, 0]]

    grafo8 = [[0, 6, 7, 0, 0],
              [0, 0, 8, 5, 0],
              [0, 0, 0, -3, 9],
              [0, -2, 0, 0, 0],
              [0, 0, 0, 7, 0]]

    estados = ["s", "t", "x", "y", "z"]
    estados2 = ["a", "b", "c", "d", "e", "f", "g"]
    estados3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
    estados4 = ["s", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    estados5 = ["u", "v", "w"]
    estados6 = ["1", "2", "3", "4"]
    estados7 = ["1", "2", "3", "4", "5", "6"]
    estados8 = ["1", "2", "3", "4", "5"]

    d = []
    p = []

    def initializeSS(self, grafo, s):
        for i in range(0, len(grafo)):
            self.d.insert(i, math.inf)
            self.p.insert(i, 0)

        self.d[s] = 0

    def relax(self, u, v, w):
        if self.d[u] + w[u][v] < self.d[v]:
            self.d[v] = self.d[u] + w[u][v]
            self.p[v] = u

    def bellman(self, grafo, s, estados):
        self.initializeSS(grafo, s)

        for _ in range(1, len(grafo) - 1):
            for i in range(0, len(grafo)):
                for j in range(0, len(grafo[i])):
                    if grafo[i][j] != 0:
                        self.relax(i, j, grafo)

        for i in range(0, len(grafo)):
            for j in range(0, len(grafo[i])):
                if grafo[i][j] != 0:
                    if self.d[j] > self.d[i] + grafo[i][j]:
                        print("Grafo contem ciclo com peso negativo")
                        return False

        print(self.d)
        self.printCaminho(s, self.d, self.p, estados)
        return True

    def printBellman(self, src, caminho, proximo, estados):

        global prox
        prox = proximo
        vAux = []

        while True:
            aux = caminho[prox]
            if aux != 0:
                vAux.append(estados[prox])
                prox = caminho[prox]

            if aux == 0:
                vAux.append(estados[prox])
                break

        for i in range(len(vAux) - 1, -1, -1):
            if i != 0:
                if vAux[i] != estados[src]:
                    print(vAux[i], '->', end=' ')

            else:
                print(vAux[i], end=' ')

    def printCaminho(self, src, custo, caminho, estados):
        print("Vertices\t\tCusto\t\tCaminho Feito")
        print("")

        for i in range(0, len(custo)):

            print(estados[src], "->", estados[i], "\t\t\t", custo[i], end='')

            if custo[i] != math.inf:
                print("\t\t\t", estados[src], "-> ", end='')
            else:
                print("\t\t", estados[src], "-> ", end='')

            self.printBellman(src, caminho, i, estados)
            print('\n')

    def getTupla(self):
        x = []

        for i in range(0, len(self.grafo)):
            for j in range(0, len(self.grafo[0])):
                if self.grafo[i][j] != 0:
                    x.append([i, j])

        for i in range(0, len(x)):
            for j in range(0, len(x[0])):
                x[i][j] = self.estados[x[i][j]]

        return x
