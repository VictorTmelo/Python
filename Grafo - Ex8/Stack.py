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