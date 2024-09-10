menu = """

[1] Depositar
[2] Sacar
[4] Extrato
[0] Sair

=> """

saldo = 0
limite = 550
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor para depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação negada, o valor digitado não é válido.")

    elif opcao == "2":
        valor = float(input("Digite o valor para sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação negada, o valor digitado não está disponível para sacar.")

        elif excedeu_limite:
            print("Operação negada, o valor digitado está acima do permitido para sacar.")

        elif excedeu_saques:
            print("Operação negada, só é permitido sacar 3 vezes por dia.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação negada, o valor digitado não é válido.")

    elif opcao == "4":
        print("\n================ EXTRATO ================")
        print("Sem registro de movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Operação negada, por favor escolha uma das opções abaixo.")