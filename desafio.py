menu = """
    d = depositar
    s = sacar
    e = extrato
    q = sair

    =>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("quanto deseja depositar? "))
        if valor > 0:
            saldo += valor
            extrato += f"deposito: R${valor:.2f}\n"
        else:
            print("valor inválido, tente novamente")
    elif opcao == "s":
        valor = float(input("quanto deseja sacar? "))
        if valor > saldo:
            print("saldo insuficiente")
        elif valor > limite:
            print("você só pode sacar R${:.2f}".format(limite))
        elif numero_saques >= LIMITE_SAQUES:
            print("limite de saques excedido")
        else:
            saldo -= valor
            extrato += f"saque: R${valor:.2f}\n"
            numero_saques += 1
    elif opcao == "e":
        print(extrato)
        print(f"seu saldo é R${saldo:.2f}")
        print(f"você fez {numero_saques} saques")
    elif opcao == "q":
        break 
    else:
        print("opção invalida, tente novamente")
