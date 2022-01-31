import math
from queue import Queue
import time
import random


class Node:
    id = -1
    pai = None
    peso = 0
    heuristica = 0

    def __init__(self, id):
        self.id = id

    def getF(self):
        return self.peso + self.heuristica


class PriorityQueueAStar:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None

        aux = (0, self.queue[0])

        for i in range(len(self.queue)):
            if self.queue[i].getF() < self.queue[aux[0]].getF():
                aux = (i, self.queue[i])

        return self.queue.pop(aux[0])

    def size(self):
        return len(self.queue)

    def empty(self):
        return True if len(self.queue) < 1 else False

    def clear(self):
        self.queue.clear()

class PriorityQueue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None

        aux = 0

        for i in range(len(self.queue)):
            if self.queue[i][0] < self.queue[aux][0]:
                aux = i

        return self.queue.pop(aux)

    def size(self):
        return len(self.queue)

    def empty(self):
        return True if len(self.queue) < 1 else False

    def clear(self):
        self.queue.clear()


class Stack:

    def __init__(self):
        self.stack = []

    def add(self, item):
        self.stack.append(item)

    def remove(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop(len(self.stack) - 1)

    def get(self):
        if len(self.stack) < 1:
            return None
        return self.stack[(len(self.stack) - 1)]

    def size(self):
        return len(self.stack)

    def print(self):
        for i in range(0, len(self.stack)):
            print(self.stack[i])


class Grafo:
    def __init__(self, linhas, colunas, ponderado, elementos):
        self.linhas = linhas
        self.colunas = colunas
        self.n = linhas * colunas
        self.isPonderado = True if ponderado == 1 else False
        self.elementos = elementos
        self.matriz = []

        for i in range(self.n):
            self.matriz.append([0] * self.n)

        for i in range(0, self.linhas):
            for j in range(0, self.colunas):
                peso = random.randint(60, 1000) if self.isPonderado else 1

                auxIndexOrigem = j + (i * self.colunas)

                if self.elementos[i][j]["background"] != "black":
                    if not (j - 1 < 0):
                        AuxIndexDestino = j - 1 + (i * self.colunas)

                        if self.elementos[i][j - 1]["background"] != "black":
                            self.matriz[auxIndexOrigem][AuxIndexDestino] = peso

                    if not (j + 1 > self.colunas - 1):
                        AuxIndexDestino = j + 1 + (i * self.colunas)

                        if self.elementos[i][j + 1]["background"] != "black":
                            self.matriz[auxIndexOrigem][AuxIndexDestino] = peso

                    if not (i - 1 < 0):
                        AuxIndexDestino = j + ((i - 1) * self.colunas)

                        if self.elementos[i - 1][j]["background"] != "black":
                            self.matriz[auxIndexOrigem][AuxIndexDestino] = peso

                    if not (i + 1 > self.linhas - 1):
                        AuxIndexDestino = j + ((i + 1) * self.colunas)

                        if self.elementos[i + 1][j]["background"] != "black":
                            self.matriz[auxIndexOrigem][AuxIndexDestino] = peso

    def paintElement(self, origem, destino, atual, flag):
        origemX = origem // self.colunas
        origemY = origem % self.colunas
        destinoX = destino // self.colunas
        destinoY = destino % self.colunas
        atualX = atual // self.colunas
        atualY = atual % self.colunas

        if not (origemX == atualX and origemY == atualY):
            if not (destinoX == atualX and destinoY == atualY):
                aux = self.elementos[atualX][atualY]

                if flag == 0:
                    aux.configure(bg="#ADD8E6")
                    aux.update()
                if flag == 1:
                    aux.configure(bg="#DA70D6")
                    aux.update()
                if flag == 2:
                    aux.configure(bg="#0F52BA")
                    aux.update()

    def bl(self, s, t):
        color = []

        for i in range(0, self.n):
            color.append("white")

        color[s] = "gray"

        node = Node(s)
        node.pai = Node(-1)

        queue = Queue()
        queue.put(node)

        while not queue.empty():
            u = queue.get()
            self.paintElement(s, t, u.id, 2)

            if u.id == t:
                caminho = []

                while u.pai is not None:
                    caminho.append(u.id)
                    u = u.pai

                caminho.reverse()

                for it in caminho:
                    #print(it)
                    self.paintElement(s, t, it, 1)

                tamanhoCaminho = len(caminho)

                return tamanhoCaminho

            for j in range(0, len(self.matriz[u.id])):
                if self.matriz[u.id][j] >= 1:
                    if color[j] == "white":
                        color[j] = "gray"
                        newNode = Node(j)
                        newNode.pai = u
                        queue.put(newNode)
                        self.paintElement(s, t, newNode.id, 0)

            color[u.id] = "black"

        return None

    def bp(self, s, t):
        color = []

        for i in range(0, self.n):
            color.append("white")

        color[s] = 'gray'

        node = Node(s)
        node.pai = Node(-1)

        pilha = Stack()
        pilha.add(node)

        while pilha.size() > 0:
            u = pilha.remove()
            self.paintElement(s, t, u.id, 2)

            if u.id == t:
                caminho = []

                while u.pai is not None:
                    caminho.append(u.id)
                    u = u.pai

                caminho.reverse()

                for it in caminho:
                    self.paintElement(s, t, it, 1)

                tamanhoCaminho = len(caminho)

                return tamanhoCaminho

            for i in range(0, len(self.matriz[u.id])):
                if self.matriz[u.id][i] >= 1:
                    if color[i] == 'white':
                        color[i] = 'gray'
                        newNode = Node(i)
                        newNode.pai = u
                        pilha.add(newNode)
                        self.paintElement(s, t, newNode.id, 0)

            color[u.id] = 'black'

        return None

    def bcu(self, s, t):
        q = PriorityQueue()
        visitados = []
        node = Node(s)
        node.pai = Node(-1)
        q.enqueue((0, node))

        for i in range(0, len(self.matriz)):
            visitados.append(False)

        while not q.empty():
            aux = q.dequeue()
            visitados[aux[1].id] = True
            self.paintElement(s, t, aux[1].id, 2)

            # Teste de Objetivo
            if aux[1].id == t:
                caminho = []
                aux = aux[1]
                pesoTotal = 0

                while aux.pai is not None:
                    caminho.append(aux.id)
                    pesoTotal += aux.peso
                    aux = aux.pai

                caminho.reverse()

                for it in caminho:
                    self.paintElement(s, t, it, 1)

                tamanhoCaminho = len(caminho)

                return tamanhoCaminho, pesoTotal

            # Expans達o de vizinhos
            for i in range(0, len(self.matriz)):
                if self.matriz[aux[1].id][i] > 0 and not visitados[i]:
                    node = Node(i)
                    node.pai = aux[1]
                    node.peso = aux[1].peso + self.matriz[aux[1].id][i]
                    q.enqueue((aux[0] + self.matriz[aux[1].id][i], node))
                    self.paintElement(s, t, node.id, 0)

        return None

    def bgme(self, s, t, tCoords):
        q = PriorityQueue()
        visitados = []
        node = Node(s)
        node.pai = Node(-1)
        q.enqueue((0, node))

        for i in range(0, len(self.matriz)):
            visitados.append(False)

        while not q.empty():
            aux = q.dequeue()
            visitados[aux[1].id] = True
            self.paintElement(s, t, aux[1].id, 2)

            # Teste de Objetivo
            if aux[1].id == t:
                caminho = []
                aux = aux[1]
                pesoTotal = 0

                while aux.pai is not None:
                    caminho.append(aux.id)
                    pesoTotal += aux.peso
                    aux = aux.pai

                caminho.reverse()

                for it in caminho:
                    self.paintElement(s, t, it, 1)

                tamanhoCaminho = len(caminho)

                return tamanhoCaminho, pesoTotal

            # Expans達o de vizinhos

            for i in range(0, len(self.matriz)):
                if self.matriz[aux[1].id][i] > 0 and not visitados[i]:
                    atualX = aux[1].id // self.colunas
                    atualY = aux[1].id % self.colunas

                    heuristic = int(math.fabs(atualX - tCoords[0]) + math.fabs(atualY - tCoords[1]))

                    node = Node(i)
                    node.pai = aux[1]
                    node.peso = aux[1].peso + self.matriz[aux[1].id][i]

                    q.enqueue((heuristic, node))
                    self.paintElement(s, t, node.id, 0)

        return None

    def aStar(self, s, t, tCoords):
        q = PriorityQueueAStar()
        visitados = []
        node = Node(s)
        node.pai = Node(-1)
        q.enqueue(node)

        for i in range(0, len(self.matriz)):
            visitados.append(False)

        while not q.empty():
            aux = q.dequeue()
            visitados[aux.id] = True
            self.paintElement(s, t, aux.id, 2)

            # Teste de Objetivo
            if aux.id == t:
                caminho = []
                aux = aux
                pesoTotal = 0

                while aux.pai is not None:
                    caminho.append(aux.id)
                    pesoTotal += aux.peso
                    aux = aux.pai

                caminho.reverse()

                for it in caminho:
                    self.paintElement(s, t, it, 1)

                tamanhoCaminho = len(caminho)

                return tamanhoCaminho, pesoTotal

            # Expans達o de vizinhos
            for i in range(0, len(self.matriz)):
                if self.matriz[aux.id][i] > 0 and visitados[i] is False:
                    atualX = aux.id // self.colunas
                    atualY = aux.id % self.colunas

                    heuristic = int(math.fabs(atualX - tCoords[0]) + math.fabs(atualY - tCoords[1]))

                    node = Node(i)
                    node.pai = aux
                    node.peso = aux.peso + self.matriz[aux.id][i]
                    node.heuristica = heuristic

                    q.enqueue(node)
                    self.paintElement(s, t, node.id, 0)

        return None