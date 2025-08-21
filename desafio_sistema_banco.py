menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500.0
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().lower()  # remove espaços e converte para minúscula

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: R$ ").replace(",", "."))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R${valor:.2f}")
                print(f"Depósito de R${valor:.2f} realizado com sucesso!")
            else:
                print("Operação inválida! O valor deve ser positivo.")
        except ValueError:
            print("Erro! Digite um valor numérico válido.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: R$ ").replace(",", "."))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if valor <= 0:
                print("Operação inválida! O valor deve ser positivo.")
            elif excedeu_saldo:
                print("Saldo insuficiente para realizar o saque.")
            elif excedeu_limite:
                print(f"Saque excede o limite de R${limite:.2f} por operação.")
            elif excedeu_saques:
                print("Limite de saques diários atingido!")
            else:
                saldo -= valor
                numero_saques += 1
                extrato.append(f"Saque: R${valor:.2f}")
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
        except ValueError:
            print("Erro! Digite um valor numérico válido.")

    elif opcao == "e":
        print("\n=== EXTRATO ===")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for registro in extrato:
                print(registro)
        print(f"Saldo atual: R${saldo:.2f}")
        print("===============\n")

    elif opcao == "q":
        print("Saindo... Obrigada por usar nosso sistema!")
        break

    else:
        print("Operação inválida! Por favor selecione novamente.")
