def sacar(*, saldo, valor, limite, extrato, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("Operacao falhou! Não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operacao falhou! O valor do saque excedeu o limite.")

    elif excedeu_saques:
        print("Operacao falhou! O número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t{saldo:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso")
    else:
        print("Operacao falhou!O valor informado é inválido!")

    return saldo, extrato
