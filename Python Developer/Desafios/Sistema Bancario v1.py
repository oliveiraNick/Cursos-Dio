from time import sleep

menu = """
 s | Fazer um Saque
 d | Fazer um Depositar
 e | Ver Extrato
 
 f | Finalizar Atendimento
-> """

saldo = 0
limite = 500.00
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(f"{' BANCO TESTE ':=^25}")
    print(f"saldo atual R${saldo:.2f}")
    print(f"-"*25)
    opcao = input(menu)

    if opcao == "s":
        while True:
            if numero_saques == LIMITE_SAQUES:
                print("\033[31mLimite de saque diário atingido! Tente novamente amanhã.\033[m")
                print(f"{'-' * 25}\n\n")
                break

            print("\n\033[4m| Digite '0' para volar ao menu |\033[m")
            saque = float(input("Valor que deseja sacar (R$000.00): R$"))

            if saque == 0:
                break

            if saque > limite:
                print("\033[31mValor excede o limite de saque (R$500.00)\033[m")

            elif saque < 0:
                print("\033[31mDigite um valor maior que R$000.00!\033[m")

            elif saldo < saque:
                print("\033[31mSaldo insuficiente! Tente outro valor ou adicione dinheiro a sua conta.\033[m")

            else:
                saldo -= saque
                numero_saques += 1
                extrato.append(str(f"\033[31mR${saque:.2f}\033[m"))

                print(f"\033[32mValor \033[4mR${saque:.2f}\033[m\033[32m retirado com sucesso!\033[m")
                print(f"{'-' * 25}\n\n")
                break

    elif opcao == "d":
        while True:
            valor = float(input("Valor a ser depositado (R$xxx.xx): R$"))

            if valor <= 0:
                print("\033[31mValor Inválido!\033[m Adicione um valor válido.")
                print(f"{'-' * 25}\n\n")

            else:
                saldo += valor
                extrato.append(str(f"\033[32mR${valor:.2f}\033[m"))
                print(f"\033[32mO valor de \033[4mR${valor:.2f}\033[m\033[32m foi depositado com sucesso!\033[m")
                break

        print(f"{'-' * 25}\n\n")

    elif opcao == "e":
        if len(extrato) == 0:
            print("Não foram realizadas movimentações.")
            print(f"{'-' * 25}\n\n")

        else:
            print(f"\n{'_'*15}\nEXTRATO")

            for v in extrato:
                print(f"| {v}")

            print(f"{'_'*15}\nSaldo atual: R${saldo:.2f}")
            sleep(3)
            print(f"{'-' * 25}\n\n")

    elif opcao == "f":
        print("\033[4mServiço finalizado! Volte Sempre\033[m")
        break

    else:
        print("\033[31mOperação Inválida!\033[m Tente novamente")
        print(f"{'-' * 25}\n\n")
