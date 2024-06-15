def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\t{saldo:.2f}\n"
        print("\nDeposito realizado com sucesso!")
    else:
        print("Operacao falhou! O valor informado é inválido!")

    return saldo, extrato
