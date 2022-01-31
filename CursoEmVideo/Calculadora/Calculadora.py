class Calculadora:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    #SEM CONSTRUTOR
    def soma(self, a, b):
        return a + b

    def subtrai(self, a, b):
        return a - b

    def multiplica(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


    #COM CONSTRUTOR
    def soma(self):
        return self.a + self.b

    def subtrai(self):
        return self.a - self.b

    def multiplica(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b