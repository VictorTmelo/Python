from Banco.Historico import Historico

class Conta:

    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

        def deposita(self, valor):
            self.saldo += valor
            self.historico.transacoes.append("depósito de {}".format(valor))

        def saca(self, valor):
            if (self.saldo < valor):
                return False
            else:
                self.saldo -= valor
                self.historico.transacoes.append("saque de {}".format(valor))

        def extrato(self):
            print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))
            self.historico.transacoes.append("tirou extrato - saldode {}".format(self.saldo))

        def transfere_para(self, destino, valor):
            retirou = self.saca(valor)
            if (retirou == False):
                return False
            else:
                destino.deposita(valor)
                self.historico.transacoes.append("transferencia de {} para conta {}".format(valor, destino.numero))
                return True
