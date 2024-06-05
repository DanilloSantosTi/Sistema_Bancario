import sys

opcao = 0
saldo = 0
saque_quantidade = 0

while opcao != 3:

    opcao = int(input("""
        Qual operacão deseja fazer?
        [0] Depositar
        [1] Sacar
        [2] Extrato
        [3] Sair
        """))

    if opcao == 0:
        deposito = int(input("Quanto você quer depositar? "))
        saldo += deposito
        print("""
        Deposito Realizado com Sucesso!
        Obrigado por utilizar o sistema Bancario!
        """)

    elif opcao == 1:
        valor_saque = int(input("Quanto você quer sacar? "))
        if valor_saque > saldo:
            print(f"Saldo insuficiente! Seu saldo atual é: {saldo}")
        elif saque_quantidade >= 3:
            print("A Quantidade de saques excedeu o limite diário!")
        elif valor_saque > 500:
            print("O valor do saque excedeu o limite de 500 reais!")
        else:
            saldo -= valor_saque
            saque_quantidade += 1
            print("""
                    Saque Realizado com Sucesso!
                    Obrigado por utilizar o sistema Bancario!
                    """)

    elif opcao == 2:
        print(f"""
        Saldo Atual: {saldo}
        Quantidade de saques: {saque_quantidade}
        """)

    elif opcao == 3:
        sys.exit("Obrigado por utilizar o sistema Bancario!")

    else:
        sys.exit("Opcao invalida, Tente novamente")
