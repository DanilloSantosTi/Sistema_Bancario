def exibir_extrato(saldo, /, *, extrato):
    print("\n-------------Extrato--------------")
    print("Não foram realizadas movimentacoes" if not extrato else extrato)
    print(f"Saldo:\t\tR$ {saldo:.2f}")
    print("--------------------------------------")
