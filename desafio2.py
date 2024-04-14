def menu():
    menu = """
    d = depositar
    s = sacar
    e = extrato
    nu= criar usuario
    nc= nova conta
    lc= listar contas
    q = sair

    =>"""
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"deposito: R${valor:.2f}\n"
        return saldo
    else:
        print("valor inválido, tente novamente")

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
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
        return saldo

def extrato_conta(saldo, *, extrato, numero_saques):
    print(extrato)
    print(f"seu saldo é R${saldo:.2f}")
    print(f"você fez {numero_saques} saques")

def criar_usuario(usuarios):
    cpf = input("qual seu cpf? (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("usuário ja existente")
        return

    nome = input("qual seu nome? ")
    data_nascimento = input("qual sua data de nascimento? (dd-mm-aaaa): ")
    endereco = input("qual seu endereço? (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("usuário criado com sucesso")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("qual seu cpf? (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, por isso não foi possível criar a conta")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: {conta["agencia"]}
            C/C: {conta["numero_conta"]}
            Titular: {conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("quanto deseja depositar? "))
            saldo = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("quanto deseja sacar? "))
            saldo = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
        elif opcao == "e":
            extrato_conta(saldo, extrato=extrato, numero_saques=numero_saques)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break 
        else:
            print("opção invalida, tente novamente")

main()