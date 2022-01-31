import math

class GrafosMatriz:
    grafo = [[0, 2, 5, 1, 0, 0],
             [2, 0, 3, 2, 0, 0],
             [5, 3, 0, 3, 1, 5],
             [1, 2, 3, 0, 1, 0],
             [0, 0, 1, 1, 0, 2],
             [0, 0, 5, 0, 2, 0]]

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

    estados = ["u", "v", "w", "x", "y", "z"]
    estados2 = ["a", "b", "c", "d", "e", "f", "g"]
    estados3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]


    def dijkstraVictor(self, u):

        values = []

        for i in range(0, len(self.estados)):
            values.append(i)

        custo = []

        N = [u]

        values.remove(u)

        for i in range(0, len(self.grafo[u])):

            if self.grafo[u][i] != 0:
                custo.insert(i, self.grafo[u][i])

            else:
                custo.insert(i, math.inf)

        while len(N) != len(self.grafo[u]):

            for w in values:

                if w not in N and custo[w] == self.minimo(custo, N):
                    N.append(w)
                    values.remove(w)

                for v in range(0, len(self.grafo[w])):

                    if self.grafo[w][v] != 0 and v not in N:
                        custo[v] = min(custo[v], custo[w] + self.grafo[w][v])

        #Deixar raiz igual a 0 caso queira deixa igual ao dijkstra
        #print(N)
        print(custo)

    def dijkstra(self, grafo, estados, u):

        values = []

        custo = []

        N = [u]

        for i in range(0, len(estados)):
            values.append(i)

        caminho = []

        for i in range(0, len(estados)):
            caminho.append(0)

        values.remove(u)

        for i in range(0, len(grafo[u])):

            if grafo[u][i] != 0:
                custo.insert(i, grafo[u][i])

            else:
                custo.insert(i, math.inf)

        while len(N) != len(grafo[u]):

            for w in values:

                if w not in N and custo[w] == self.minimo(custo, N):
                    N.append(w)
                    values.remove(w)

                for v in range(0, len(grafo[w])):

                    if grafo[w][v] != 0 and v not in N:
                        if custo[v] > custo[w] + grafo[w][v]:
                            custo[v] = custo[w] + grafo[w][v]
                            caminho[v] = w

        custo[u] = 0
        self.printCaminho(u, custo, caminho, estados)

    def printDijsktraRecursive(self, caminho, proximo, estados):

        if caminho[proximo] == 0:
            print(estados[proximo], end=' ')

            return
        self.printDijsktraRecursive(caminho, caminho[proximo], estados)
        print("->", estados[proximo], end=' ')

    def printDijsktraNonRecursive(self, caminho, proximo, estados):

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

            self.printDijsktraNonRecursive(caminho, i, estados)
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

    def minimo(self, custo, N):

        res = []

        for i in range(0, len(custo)):

            if i not in N:
                res.append(custo[i])

        return min(res)
