import math

from Fila import Fila


class GrafosMatriz:
    grafo = [[0, 16, 13, 0, 0, 0],
             [0, 0, 10, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]]

    estados = ["A", "B", "C", "D", "E", "F"]

    def ford(self, g, s, t):
        flow = 0
        anterior = []
        residuais = []
        fluxos = []
        caminho = []
        minimos = []

        for i in range(0, len(g)):
            anterior.insert(i, 0)

        while self.BFS(g, s, t, anterior):
            c = math.inf
            aux = t

            while aux != s:
                c = min(c, g[anterior[aux]][aux])
                aux = anterior[aux]

            minimos.append(c)

            flow += c
            j = t
            caminhoAtual = []

            while j != s:
                i = anterior[j]
                caminhoAtual.append(i)
                g[i][j] -= c
                g[j][i] += c
                j = anterior[j]

            caminho.append(caminhoAtual.copy())

            aux = []

            for i in range(0, len(g)):
                aux.append(g[i].copy())

            residuais.append(aux)
            fluxos.append(flow)

        for i in range(0, len(residuais)):
            for j in range(len(caminho[i]) - 1, -1, -1):
                print(self.estados[caminho[i][j]], "->", end=' ')

            print(self.estados[t])

            print(residuais[i])
            print("Fluxo", i + 1, ":", fluxos[i])
            print("Minimo:", minimos[i])
            print()

    def BFS(self, g, s, t, anterior):
        color = []
        distancia = []

        for i in range(0, len(g)):
            color.append("white")
            distancia.append(math.inf)

        color[s] = "gray"
        distancia[s] = 0
        anterior[s] = 0

        queue = Fila()
        queue.enqueue(s)

        while queue.size() != 0:
            u = queue.dequeue()

            for j in range(0, len(g[u])):
                if g[u][j] > 0 and color[j] == "white":
                    color[j] = "gray"
                    distancia[j] = distancia[u] + 1
                    anterior[j] = u
                    queue.enqueue(j)

            color[u] = "black"

        if color[t] == "black":
            return True
        else:
            return False

    '''def BFS(self, s, t, caminho):
        # Return True if there is node that has not iterated.
        visited = [False] * len(self.grafo)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind in range(len(self.grafo[u])):
                if visited[ind] is False and self.grafo[u][ind] > 0:
                    queue.append(ind)
                    visited[ind] = True
                    caminho[ind] = u

        return True if visited[t] else False

    def FordFulkerson(self, origem, destino):
        # This array is filled by BFS and to store path
        caminho = [-1] * (len(self.grafo))
        max_flow = 0

        while self.BFS(origem, destino, caminho):
            path_flow = float("Inf")
            s = destino

            while s != origem:
                # Find the minimum value in select path
                path_flow = min(path_flow, self.grafo[caminho[s]][s])
                s = caminho[s]

            max_flow += path_flow
            v = destino

            while v != origem:
                u = caminho[v]
                self.grafo[u][v] -= path_flow
                self.grafo[v][u] += path_flow
                v = caminho[v]

            print(self.grafo)
            print(max_flow)

        #print(max_flow)'''

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
