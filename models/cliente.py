from datetime import date
from utils.helper import date_para_str, str_para_date


class Cliente:
    contador: int = 101

    def __init__(self, nome: str, email: str, cpf: str, data_nascimento: str):
        self.__codigo: int = Cliente.contador
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__data_nascimento: date = str_para_date(data_nascimento)
        self.__data_cadastro = date.today()
        Cliente.contador += 1

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_nascimento(self):
        return date_para_str(self.__data_nascimento)

    @property
    def data_cadastro(self):
        return date_para_str(self.__data_cadastro)

    def __str__(self):
        return f'Código {self.codigo} \nNome: {self.nome} \nData Nascimento: {self.data_nascimento} \nCadastro: {self.data_cadastro}'
