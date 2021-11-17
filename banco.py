from typing import List

from time import sleep

from models.cliente import Cliente

from models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    print("-----------------------------------------------------")
    print("------------------------ATM--------------------------")
    print("-----------------------------------------------------")
    print("----------------------VINIBANK-----------------------")
    print("-----------------------------------------------------")
    print("Selecione a opção no MENU:")
    print("1 - Criar Conta")
    print("2 - Efetuar Saque")
    print("3 - Efetuar Depósito")
    print("4 - Efetuar Transferência")
    print("5 - Listar Contas")
    print("6 - Sair do ATM")

    opcao: int = int(input())

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
        print("Volte Sempre!!")
        sleep(2)
        exit(0)
    else:
        print("Opção invalida")
        sleep(2)
        menu()


def menu() -> None:
    main()

def criar_conta() -> None:
    print("Informe os dados do Cliente")
    print("-----------------------------------------------------")
    nome: str = input("Nome do Cliente: ")
    email: str = input("email do Cliente: ")
    cpf: str = input("Cpf do Cliente: ")
    data_nascimento: str = input("Digite a data de nascimento do Cliente: ")

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print("-----------------------------------------------------")
    print("Conta criada com sucesso!")
    print("Dados da conta: ")
    print("-----------------------------------------------------")
    print(conta)
    sleep(2)
    main()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input("Informe o número da sua conta: "))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input("Informe o valor do saque: "))
            conta.sacar(valor)
        else:
            print(f"Não foi encontrado a conta com o número {numero}")
    else:
        print("Ainda não existem contas cadastradas")
        sleep(2)
        main()
    main()

def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input("Informe o número da sua conta: "))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input("Informe o valor do deposito: "))
            conta.depositar(valor)
        else:
            print(f"Não foi encontrado a conta com o número {numero}")
    else:
        print("Ainda não existem contas cadastradas")
        sleep(2)
        main()
    main()

def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input("Informe o número da sua conta: "))

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input("Informe o número da conta destino: "))

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input("Informe o valor da transferencia: "))
                conta_o.transferir(conta_d, valor)
            else:
                print(f"A conta {conta_d} não foi encontrada")

        else:
            print(f"Não foi encontrado a conta com o número {numero_o}")
    else:
        print("Ainda não existem contas cadastradas")
        sleep(2)
        main()
    main()

def listar_contas() -> None:
    if len(contas) > 0:
        print("Listagem de Contas")
        print("-----------------------------------------------------")
        for conta in contas:
            print(conta)
            print("-----------------------------------------------------")
            sleep(1)
    else:
        print("Ainda não existem contas cadastradas")
        sleep(2)
        main()
    main()

def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c
    main()


if __name__ == '__main__':
    main()



