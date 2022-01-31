import queue

class Node:
    id = -1
    pai = None

    def __init__(self, id):
        self.id = id

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
    matriz = []
    n = 0
    direcionado = False

    def __init__(self, n, direcionado):
        self.n = n
        self.direcionado = direcionado
        for i in range(n):
            self.matriz.append([0] * n)

    def addAresta(self, s, t):
        if (not self.direcionado):
            self.matriz[t][s] = 1
        self.matriz[s][t] = 1

    def printMatriz(self):
        print()
        print('##########')
        for i in range(self.n):
            for j in range(self.n):
                print(self.matriz[i][j], end=' ')
            print()
        print('##########')
        print()

    def bl(self, s, t):

        q = queue.Queue()

        node = Node(s)
        node.pai = Node(-1)

        q.put(node)

        while not q.empty():
            aux = q.get()

            # Teste de Objetivo
            if aux.id == t:
                return aux
            # Teste de Objetivo

            # Expansão de vizinhos
            for i in range(self.n):

                if self.matriz[aux.id][i] == 1 and i != aux.pai.id:
                    node = Node(i)
                    node.pai = aux
                    q.put(node)
            # Expansão de vizinhos

        return aux

    def bp(self, s, t):

        q = Stack()

        node = Node(s)
        node.pai = Node(-1)

        q.add(node)

        while q.size() != 0:

            aux = q.remove()

            # Teste de Objetivo
            if aux.id == t:
                return aux
            # Teste de Objetivo

            # Expansão de vizinhos
            for i in range(self.n):

                if self.matriz[aux.id][i] == 1 and i != aux.pai.id:
                    node = Node(i)
                    node.pai = aux
                    q.add(node)
            # Expansão de vizinhos

        return aux

    def bcu(self, s, t):

        q = queue.Queue()

        node = Node(s)
        node.pai = Node(-1)

        q.put(node)

        while (not q.empty()):
            aux = q.get()

            # Teste de Objetivo
            if (aux.id == t):
                return aux
            # Teste de Objetivo

            # Expansão de vizinhos
            for i in range(self.n):
                if (self.matriz[aux.id][i] == 1 and i != aux.pai.id):
                    node = Node(i)
                    node.pai = aux
                    q.put(node)
            # Expansão de vizinhos

        return aux



g = Grafo(10, False)

g.printMatriz()

g.addAresta(0, 2)
g.addAresta(1, 3)
g.addAresta(2, 3)
g.addAresta(3, 5)
g.addAresta(5, 4)
g.addAresta(3, 6)
g.addAresta(6, 9)
g.addAresta(4, 7)
g.addAresta(4, 8)
g.addAresta(8, 9)

g.printMatriz()

objetivo = g.bl(0, 9)

while (objetivo.id != -1):
    print(objetivo.id)
    objetivo = objetivo.pai