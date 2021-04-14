from models.cliente import Cliente
from utils.helper import formata_float_str_moeda


class Conta:

    codigo = 1001

    def __init__(self, cliente: Cliente):
        self.__numero = Conta.codigo
        self.__cliente = cliente
        self.__saldo = 0.0
        self.__limite = 100.00
        self.__saldo_total = self.calcula_saldo_total
        Conta.codigo += 1

    def __str__(self):
        return f'Número da conta: {self.numero} \nCliente: {self.cliente.nome} \'' \
               f'\nSaldo Total: {formata_float_str_moeda(self.saldo_total)}'

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @property
    def saldo_total(self):
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self, valor: float) -> None:
        self.__saldo_total = valor

    @property
    def calcula_saldo_total(self):
        return self.saldo + self.limite

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self.calcula_saldo_total
            print('Depósito efetuado com sucesso!')
        else:
            print('Erro ao efetuar o depósito. Tente novamente')

    def sacar(self, valor):
        if 0 < valor <= self.saldo_total:

            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self.calcula_saldo_total
            else:
                restante: float = self.saldo - valor  # irá retornar um valor negativo
                self.limite = self.limite + restante
                self.saldo_total = self.calcula_saldo_total
            print('Saque efetuado com sucesso.')

        else:
            print('Saque não realizado. Tente novamente')

    def transferir(self, destino: object, valor):
        if 0 < valor <= self.saldo_total:

            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self.calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino.calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.saldo = 0
                self.limite = self.limite + restante
                self.saldo_total = self.calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino.calcula_saldo_total
            print('Transferência feita com sucesso!')

        else:
            print('Transferência não realizada.')
