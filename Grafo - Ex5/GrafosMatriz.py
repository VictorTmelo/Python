import math
from Queue import Queue

class GrafosMatriz:

    '''grafo = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
                 [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

        estados = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]'''

    grafo = [[0, 1, 0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 1, 0, 1, 1, 0],
             [0, 0, 1, 0, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 0, 0, 0, 1, 0],
             [0, 0, 1, 1, 0, 1, 0, 1],
             [0, 0, 0, 1, 0, 0, 1, 0]]

    estados = ["r", "s", "t", "u", "v", "w", "x", "y"]


    def BFS(self, s):

        color = []
        distancia = []
        anterior = []

        arvore = []

        for i in range(0, len(self.estados)):
            color.append("white")
            distancia.append(math.inf)
            anterior.append(None)

        color[s] = "gray"
        distancia[s] = 0
        anterior[s] = None

        queue = Queue()
        queue.enqueue(self.estados[s])
        print(queue.queue)

        while queue.size() != 0:
            u = queue.dequeue()
            u = self.estados.index(u)

            for j in range(0, len(self.grafo[u])):
                if self.grafo[u][j] == 1:
                    if color[j] == "white":
                        color[j] = "gray"
                        distancia[j] = distancia[u] + 1
                        anterior[j] = u
                        queue.enqueue(self.estados[j])

                        arvore.append([self.estados[u], self.estados[j]])

            color[u] = "black"
            print(queue.queue)

        return arvore

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
