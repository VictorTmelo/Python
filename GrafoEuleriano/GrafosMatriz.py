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

    grafo5 = [[0,1,1,1],
              [1,0,1,1],
              [1,1,0,1],
              [1,1,1,0]]

    grafos.append(grafo1)
    grafos.append(grafo2)
    grafos.append(grafo3)
    grafos.append(grafo4)
    grafos.append(grafo5)

    def euler(self, num):

        graus = []

        for i in range(0, len(self.grafos[num])):

            cont = 0

            for j in range(0, len(self.grafos[num][i])):

                if self.grafos[num][i][j] == 1:
                    cont += 1

            graus.append(cont)

        print(graus)

        cont = 0

        for i in range(0, len(graus)):

            if graus[i] % 2 != 0:
                cont += 1

        print("Quantidade de impares: " , cont)

        if cont == 0:
            print(f"O grafo {num} é euleriano")
            print()
            return

        if cont == 2:
            print(f"O grafo {num} é semi-euleriano.")
            print()
            return

        if cont > 2:
            print(f"O grafo {num} não é euleriano.")
            print()
            return
