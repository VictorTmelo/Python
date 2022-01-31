from Banco.Cliente import Cliente
from Banco.Conta import Conta

if __name__ == '__main__':
    cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
    cliente2 = Cliente('José', 'Azevedo', '222222222-22')
    conta1 = Conta('123-4', cliente1, 1000.0, float('inf'))
    conta2 = Conta('123-5', cliente2, 1000.0, float('inf'))
    conta1.deposita(100.0)
    conta1.saca(50.0)
    conta1.transfere_para(conta2, 200.0)
    conta1.extrato

    # numero: 123-4
    # saldo: 850.0

    conta1.historico.imprime()

    # data abertura: 2018-05-10 19:44:07.406533
    # transações:
    # - depósito de 100.0
    # - saque de 50.0
    # - saque de 200.0
    # - transferencia de 200.0 para conta 123-5
    # - tirou extrato - saldo de 850.0

conta2.historico.imprime()

# data abertura: 2018-05-10 19:44:07.406553
# transações:
# - depósito de 200.0
