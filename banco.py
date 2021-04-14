from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def main() -> None:
    menu()


def menu():
    print('='*12)
    print('Banco Python')
    print('='*12)
    print('Selecione uma opção das opções abaixo: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar um depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção Inválida!')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Informe seus dados: ')
    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente:')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de Nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)
    print('Conta criada com sucesso!')
    print('-> Dados da conta')
    print('='*20)
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor de um saque: '))
            conta.sacar(valor)  # Verificação de saldo é feito dentro de sacar()
        else:
            print(f'Não foi encontrada a conta com número: {numero}')
    else:
        print('Por favor cadastre uma conta!')
    sleep(1)
    menu()


def efetuar_deposito():
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor que deseja depositar: '))
            conta.depositar(valor)  # Verificação de saldo é feito dentro de depositar()
        else:
            print(f'Não foi encontrada a conta com número: {numero}')

    else:
        print('Por favor cadastre uma conta!')
    sleep(1)
    menu()


def efetuar_transferencia():
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da sua conta: '))
        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('Informe o número da conta de destino: '))
            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da transferência: '))
                conta_o.transferir(conta_d, valor)
            else:
                print(f'A conta {conta_d} não existe')

        else:
            print(f'A sua conta {conta_o} não foi encontrada')

    else:
        print('Por favor cadastre uma conta!')
    sleep(1)
    menu()


def listar_contas():
    if len(contas) > 0:
        print('Listagem de contas')

        for i in contas:
            print(i)
            print('='*12)
            sleep(1)

    else:
        print('Não existem contas cadastradas!')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
