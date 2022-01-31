import networkx as nx
import matplotlib.pyplot as plt

class GrafosMatriz:
    grafos = []

    estados = ["1", "2", "3", "4", "5", "6", "7"]

    grafo1 = [[0, 1, 1, 0, 0, 1, 1],
              [1, 0, 1, 1, 0, 1, 0],
              [1, 1, 0, 1, 1, 0, 0],
              [0, 1, 1, 0, 1, 0, 1],
              [0, 0, 1, 1, 0, 1, 1],
              [1, 1, 0, 0, 1, 0, 1],
              [1, 0, 0, 1, 1, 1, 0]]

    grafo2 = [[0, 1, 1, 0, 0, 1, 1],
              [1, 0, 1, 1, 0, 1, 0],
              [1, 1, 0, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 1],
              [0, 0, 0, 1, 0, 1, 1],
              [1, 1, 0, 0, 1, 0, 1],
              [1, 0, 0, 1, 1, 1, 0]]

    grafo3 = [[0, 1, 1, 0, 0, 1, 1],
              [1, 0, 1, 0, 0, 0, 0],
              [1, 1, 0, 1, 0, 0, 0],
              [0, 0, 1, 0, 1, 0, 0],
              [0, 0, 0, 1, 0, 1, 1],
              [1, 0, 0, 0, 1, 0, 1],
              [1, 0, 0, 0, 1, 1, 0]]

    grafo4 = [[0, 1, 1, 0, 0, 1, 1],
              [1, 0, 1, 0, 0, 0, 0],
              [1, 1, 0, 1, 0, 0, 0],
              [0, 0, 1, 0, 1, 0, 0],
              [0, 0, 0, 1, 0, 1, 0],
              [1, 0, 0, 0, 1, 0, 1],
              [1, 0, 0, 0, 0, 1, 0]]

    grafo5 = [[0, 1, 1, 0],
              [1, 0, 0, 1],
              [1, 0, 0, 1],
              [0, 1, 1, 0]]

    grafos.append(grafo1)
    grafos.append(grafo2)
    grafos.append(grafo3)
    grafos.append(grafo4)
    grafos.append(grafo5)

    def dirac(self, num):

        if len(self.grafos[num]) < 3:
            print(f"O grafo {num} não satisfaz o Teorema de Dirac.")
            return

        for i in range(0, len(self.grafos[num])):

            cont = 0

            for j in range(0, len(self.grafos[num][i])):

                if self.grafos[num][i][j] == 1:
                    cont += 1

            if cont < len(self.grafos[num]) / 2:
                print(f"O grafo {num} não satisfaz o Teorema de Dirac.")
                return

        print(f"O grafo {num} satisfaz o Teorema de Dirac!")

    def ore(self, num):

        graus = []

        if len(self.grafos[num]) < 3:
            print(f"O grafo {num} não satisfaz o Teorema de Ore.")
            return

        for i in range(0, len(self.grafos[num])):

            cont = 0

            for j in range(0, len(self.grafos[num][i])):

                if self.grafos[num][i][j] == 1:
                    cont += 1

            graus.append(cont)

        for i in range(0, len(self.grafos[num])):

            for j in range(0, len(self.grafos[num][i])):

                if self.grafos[num][i][j] == 0 and i != j:

                    if graus[i] + graus[j] < len(self.grafos[num]):
                        print(f"O grafo {num} não satisfaz o Teorema de Ore.")
                        return

        print(f"O grafo {num} satisfaz o Teorema de Ore!")

    def bondy(self, num):
        gLen = len(self.grafos[num])

        if gLen < 3:
            print(f"O grafo {num} não satisfaz o Teorema de Bondy e Chvatal.")
            return

        aux = []

        for i in range(0, len(self.grafos[num])):
            temp = []

            for j in range(0, len(self.grafos[num][i])):
                temp.append(self.grafos[num][i][j])

            aux.append(temp)

        tryClosules = True
        hasClosures = True

        while hasClosures and tryClosules:
            graus = []

            for i in range(0, gLen):

                cont = 0

                for j in range(0, len(aux[i])):

                    if aux[i][j] == 1:
                        cont += 1

                graus.append(cont)

            tryClosules = False

            for i in range(0, gLen):

                for j in range(0, len(aux[i])):

                    if aux[i][j] == 0 and i != j:

                        if graus[i] + graus[j] >= gLen:
                            aux[i][j] = 1
                            aux[j][i] = 1

                            tryClosules = True

            hasClosures = False

            for i in range(0, gLen):
                for j in range(0, len(aux[i])):
                    if aux[i][j] == 0 and i != j:
                        hasClosures = True

        for i in range(0, len(aux)):
            cont = 0

            for j in range(0, len(aux[i])):
                cont += aux[i][j]

            if cont < gLen - 1:
                print(f"O grafo {num} não satisfaz o Teorema de Bondy e Chvatal.")

                x = nx.Graph()
                x.add_edges_from(self.getTupla(aux))
                nx.draw_networkx(x)
                plt.show()

                return

        x = nx.Graph()
        x.add_edges_from(self.getTupla(aux))
        nx.draw_networkx(x)
        plt.show()

        print(f"O grafo {num} satisfaz o Teorema de Bondy e Chvatal!")

    def getTupla(self, grafo):
        x = []

        for i in range(0, len(grafo)):
            for j in range(0, len(grafo[0])):
                if grafo[i][j] != 0:
                    x.append([i, j])

        return x