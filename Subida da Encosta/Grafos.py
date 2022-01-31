import random

class Grafo:
    def __init__(self, N):
        self.n = N
        self.posicoes = [0] * self.n

        for i in range(0, N):
            aux = random.randint(0, N - 1)
            self.posicoes[i] = aux

        self.matriz = self.gerarMatriz(self.posicoes)


    def printEstado(self, matriz):
        for i in matriz:
            print(i)
        print("")


    def encosta(self):
        sucessorEstado = self.posicoes.copy()
        sucessorMatriz = self.gerarMatriz(sucessorEstado)

        while True:
            self.posicoes = sucessorEstado.copy()
            self.matriz = self.gerarMatriz(self.posicoes)

            aux = self.getSucessor(sucessorEstado)
            sucessorEstado = aux[0]
            sucessorMatriz = aux[1]

            print("Tentativas")
            self.printEstado(sucessorMatriz)
            print(f"Ataques: {self.heuristica(sucessorMatriz, sucessorEstado)}\n")

            if self.posicoes == sucessorEstado:
                print("Resultado Final")
                self.printEstado(self.matriz)
                print(f"Ataques: {self.heuristica(self.matriz, self.posicoes)}\n")
                break
            elif self.heuristica(self.matriz, self.posicoes) == self.heuristica(sucessorMatriz, sucessorEstado):
                print("Ombro")
                self.printEstado(sucessorMatriz)
                print(f"Ataques: {self.heuristica(sucessorMatriz, sucessorEstado)}\n")

                i = random.randint(0, self.n - 1)
                j = random.randint(0, self.n - 1)
                sucessorEstado[i] = j
                sucessorMatriz = self.gerarMatriz(sucessorEstado)


    def gerarMatriz(self, sucessorEstado):
        sucessorMatriz = []

        for i in range(self.n):
            sucessorMatriz.append([0] * self.n)

        for i in range(0, len(sucessorEstado)):
            sucessorMatriz[sucessorEstado[i]][i] = 1

        return sucessorMatriz

    def getSucessor(self, estado):
        melhorEstado = estado.copy()
        melhorMatriz = self.gerarMatriz(melhorEstado)

        melhorHeuristica = self.heuristica(melhorMatriz, melhorEstado)

        auxEstado = estado.copy()
        auxMatriz = self.gerarMatriz(auxEstado)

        for i in range(0, self.n):
            for j in range(0, self.n):
                if j != estado[i]:
                    auxEstado[i] = j
                    auxMatriz[auxEstado[i]][i] = 1
                    auxMatriz[estado[i]][i] = 0

                    auxHeuristica = self.heuristica(auxMatriz, auxEstado)

                    if auxHeuristica <= melhorHeuristica:
                        melhorHeuristica = auxHeuristica
                        melhorEstado = auxEstado.copy()
                        melhorMatriz = self.gerarMatriz(melhorEstado)

                    auxMatriz[auxEstado[i]][i] = 0
                    auxEstado[i] = estado[i]
                    auxMatriz[estado[i]][i] = 1

        return melhorEstado, melhorMatriz


    def heuristica(self, matriz, estado):
        ataques = 0

        for i in range(0, self.n):
            #esquerda
            linha = estado[i]
            coluna = i - 1

            while coluna >= 0 and matriz[linha][coluna] != 1:
                coluna -= 1

            if coluna >= 0 and matriz[linha][coluna] == 1:
                ataques += 1

            #direita
            linha = estado[i]
            coluna = i + 1

            while coluna < self.n and matriz[linha][coluna] != 1:
                coluna += 1

            if coluna < self.n and matriz[linha][coluna] == 1:
                ataques += 1

            #diagonal esquerda cima
            linha = estado[i] - 1
            coluna = i - 1

            while linha >= 0 and coluna >= 0 and matriz[linha][coluna] != 1:
                linha -= 1
                coluna -= 1

            if linha >= 0 and coluna >= 0 and matriz[linha][coluna] == 1:
                ataques += 1

            #diagonal direita cima
            linha = estado[i] - 1
            coluna = i + 1

            while linha >= 0 and coluna < self.n and matriz[linha][coluna] != 1:
                linha -= 1
                coluna += 1

            if linha >= 0 and coluna < self.n and matriz[linha][coluna] == 1:
                ataques += 1

            #diagonal esquerda baixo
            linha = estado[i] + 1
            coluna = i - 1

            while linha < self.n and coluna >= 0 and matriz[linha][coluna] != 1:
                linha += 1
                coluna -= 1

            if linha < self.n and coluna >= 0 and matriz[linha][coluna] == 1:
                ataques += 1

            # diagonal direita baixo
            linha = estado[i] + 1
            coluna = i + 1

            while linha < self.n and coluna < self.n and matriz[linha][coluna] != 1:
                linha += 1
                coluna += 1

            if linha < self.n and coluna < self.n and matriz[linha][coluna] == 1:
                ataques += 1

        return ataques // 2
