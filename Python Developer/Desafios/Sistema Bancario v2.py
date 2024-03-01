from time import sleep
import textwrap

def menu(): 
    print("""------------ MENU ------------
          
nu | Novo Usuário
nc | Nova Conta
lc | Listar Contas
s | Saque
d | Depositar
e | Extrato

f | Finalizar Atendimento
-----------------------------""")

    return input("-> ")

def deposito(saldo, valor, extrato):
    saldo += valor
    extrato.append(str(f"\033[32mR${valor:.2f}\033[m"))

    print(f"\033[32mO valor de \033[4mR${valor:.2f}\033[m\033[32m foi depositado com sucesso!\n\n\033[m")
    sleep(1)

    return saldo, extrato

def saque(*, saldo, extrato, limite, numero_saques, limite_saques):

    while True:

        if numero_saques >= limite_saques:
            print("\033[31mLimite de saque diário atingido! Tente novamente amanhã.\033[m")
            print(f"{'-' * 25}\n\n")
            break

        valor = float(input("| R$"))

        if valor == 0:
            break

        elif valor > limite:
            print("\033[31mValor excede o limite de saque (R$500.00)\033[m")

        elif valor < 0:
            print("\033[31mDigite um valor maior que R$000.00!\033[m")

        elif valor > saldo:
            print("\033[31mSaldo insuficiente! Tente outro valor ou adicione dinheiro a sua conta.\033[m")

        else:
            saldo -= valor
            extrato.append(str(f"\033[31mR${valor:.2f}\033[m"))
            numero_saques += 1

            print(f"\033[32mValor \033[4mR${valor:.2f}\033[m\033[32m retirado com sucesso!\033[m")
            print(f"{'-' * 25}\n\n")
            break

    return saldo, extrato, numero_saques

def ver_extrato(saldo, *, extrato):
    if len(extrato) == 0:
            print("Não foram realizadas movimentações.")
            print(f"{'-' * 25}\n\n")

    else:
        print(f"\n{'_'*15}\nEXTRATO")

        for v in extrato:
            print(f"| {v}")

        print(f"{'_'*15}\nSaldo atual: R${saldo:.2f}")
        sleep(1)
        print(f"{'-' * 25}\n\n")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def novo_usuario(usuarios):
    while True:
        cpf = input("Informe o CPF (somente número): ")
        usuario = filtrar_usuario(cpf, usuarios)

        if usuario:
            print("\n\033[31mJá existe usuário com esse CPF! tente novamente\033[m")

        else:
            nome = input("| Informe o nome completo: ")
            data_nascimento = input("| Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input("| Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

            usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

            print("\033[32mUsuário criado com sucesso!\033[m")
            sleep(1)
            break
    return

def nova_conta(agencia, numero_conta, usuarios):
    
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n\033[32mConta criada com sucesso!\033[m")
        sleep(1)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n\033[31mUsuário não encontrado!\033[m")

def listar_contas(contas):

    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        sleep(1)

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500.00
    numero_saques = 0
    extrato = []
    contas = []
    usuarios = []

    while True:
        print(f"{'-'*30}\n\033[32mSaldo atual: R${saldo:.2f}\033[m")
        opcao = menu()

        # Operação: Depósito
        if opcao == "d":
            while True:
                valor = float(input("| R$"))

                if valor <= 0:
                    print("\033[31mValor Inválido!\033[m Tente novamente.")

                saldo, valor = deposito(saldo, valor, extrato)
                break

        # Operação: Saque
        elif opcao == "s":

            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques = numero_saques,
                limite_saques=LIMITE_SAQUES
                )

        # Operação: Visualizar Extrato
        elif opcao == "e":
            ver_extrato(saldo, extrato=extrato)

        # Operação: Novo Usuário
        elif opcao == "nu":
            novo_usuario(usuarios)

        # Operação: Nova Conta
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        # Operação: Listar contas
        elif opcao == "lc":
            listar_contas(contas)

        # Operação: Finalizar atendimento
        elif opcao == "f":
            print("="*29)
            print("\033[32m| Atendimanto Finalizado! Até a próxima |\033[m")
            sleep(2)
            break
        
        # Erro: Operação Inválida
        else:
            print(f"\033[31m| Comando '{opcao}' inválido! Tente novamente |\033[m")
            print("-"*29)
            sleep(1)

main()
