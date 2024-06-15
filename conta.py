import textwrap
import usuario


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    filtrar_usuario = usuario.filtrar_usuarios(cpf, usuarios)

    if filtrar_usuario:
        print("Conta cadastrada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": filtrar_usuario}

    else:
        print("Usuário não encontrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta["agencia"]}
            Numero de Conta:\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("-" * 100)
        print(textwrap.dedent(linha))
