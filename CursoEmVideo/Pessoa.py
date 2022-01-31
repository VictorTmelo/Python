class Pessoa:

    def __init__(self,nome,idade,cidade):
        self.nome = nome
        self.idade=  idade
        self.cidade = cidade

        fala(nome,idade,cidade)


def fala(nome,idade,cidade):
    print(f"{nome} tem {idade} anos e mora na {cidade}")


p1 = Pessoa("Victor",20,"Fortaleza")