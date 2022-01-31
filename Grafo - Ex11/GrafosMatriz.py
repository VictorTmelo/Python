import math


class GrafosMatriz:
    grafo = [[0, 4, 11],
             [6, 0, 2],
             [3, 0, 0]]

    grafo2 = [[0, 3, 8, 0, -4],
              [0, 0, 0, 1, 7],
              [0, 4, 0, 0, 0],
              [2, 0, -5, 0, 0],
              [0, 0, 0, 6, 0]]

    grafo3 = [[0, 5, 7, 1, 0, 0, 0],
              [0, 0, 2, 0, 0, 0, 0],
              [0, 0, 0, 6, 5, 0, 0],
              [0, 3, 0, 0, 0, 5, 3],
              [0, 0, 0, 0, 0, 4, 0],
              [0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0]]

    grafo4 = [[0, 0, 0, 0, 5, 1, 0, 0, 0, 0, 0, 2, 0, 0],
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

    estados = ["1", "2", "3"]
    estados2 = ["1", "2", "3", "4", "5"]
    estados3 = ["a", "b", "c", "d", "e", "f", "g"]
    estados4 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]

    def floyd(self, grafo, estados):
        c = []
        p = []

        for i in range(0, len(grafo)):
            aux = []
            aux1 = []

            for j in range(0, len(grafo)):

                if grafo[i][j] != 0:
                    aux.insert(j, grafo[i][j])
                    aux1.insert(j, i)
                if grafo[i][j] == 0 and i != j:
                    aux.insert(j, math.inf)
                    aux1.insert(j, None)
                if i == j:
                    aux.insert(j, 0)
                    aux1.insert(j, None)

            c.insert(i, aux)
            p.insert(i, aux1)

        for k in range(0, len(grafo)):
            print('d', k + 1, end=' ')
            for i in range(0, len(grafo)):
                for j in range(0, len(grafo)):
                    if c[i][j] > c[i][k] + c[k][j]:
                        c[i][j] = c[i][k] + c[k][j]
                        p[i][j] = p[k][j]

            self.printD(c)
            print('\n')
            print('p', k + 1, end='')
            self.printP(p, estados)
            print('\n')

        self.printCaminho(c, p, estados)

    def printD(self, m):
        for i in range(0, len(m)):
            for j in range(0, len(m[i])):
                if i != 0 and j == 0:
                    print("\t\t", m[i][j], ' ', end='')
                else:
                    print("\t", m[i][j], ' ', end='')

            print('')

    def printP(self, m, estados):
        for i in range(0, len(m)):
            for j in range(0, len(m[i])):
                if i == 0 and j == 0 and m[i][j] is None:
                    print("\t\t", m[i][j], ' ', end='')
                else:
                    if i != 0 and j == 0:
                        if m[i][j] is None:
                            print("\t\t", m[i][j], ' ', end='')
                        else:
                            print("\t\t", estados[m[i][j]], ' ', end='')
                    else:
                        if m[i][j] is None:
                            print("\t", m[i][j], ' ', end='')
                        else:
                            print("\t", estados[m[i][j]], ' ', end='')

            print('')

    def printFloyd(self, caminho, current, proximo, estados):

        global prox
        prox = proximo
        vAux = []

        while True:
            aux = caminho[current][prox]

            if aux is None:
                vAux.append(estados[prox])
                break

            if aux != None:
                vAux.append(estados[prox])
                prox = caminho[current][prox]

        for i in range(len(vAux) - 1, -1, -1):
            if i != 0:
                if vAux[i] != estados[current]:
                    print(vAux[i], '->', end=' ')

            else:
                print(vAux[i], end=' ')

    def printCaminho(self, custo, caminho, estados):
        print("Vertices\t\tCusto\t\tCaminho Feito")
        print("")

        for i in range(0, len(custo)):
            for j in range(0, len(custo[i])):

                print(estados[i], "->", estados[j], "\t\t\t", custo[i][j], end='')

                if custo[i][j] != math.inf:
                    print("\t\t\t", estados[i], "-> ", end='')
                else:
                    print("\t\t", estados[i], "-> ", end='')

                self.printFloyd(caminho, i, j, estados)
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
