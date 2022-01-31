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

    grafo = [[0, 0, 1, 1, 0, 0, 0, 0],
             [0, 0, 1, 1, 0, 0, 0, 0],
             [1, 1, 0, 1, 0, 0, 0, 1],
             [1, 1, 1, 0, 0, 1, 1, 0],
             [0, 0, 0, 0, 0, 1, 1, 0],
             [0, 0, 0, 1, 1, 0, 1, 0],
             [0, 0, 0, 1, 1, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0]]

    estados = ["1", "2", "3", "4", "5", "6", "7", "8"]

    vertices = []

    arvore = []

    def __init__(self):
        for i in range(0, len(self.estados)):
            self.vertices.append(False)

    def DFS(self, u):

        self.vertices[u] = True

        for i in range(0, len(self.grafo[u])):
            if self.grafo[u][i] == 1:
                if not self.vertices[i]:
                    self.DFS(i)
                    self.arvore.append([self.estados[u], self.estados[i]])

        return self.arvore

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
