def criar_usuario(usuarios):
    cpf = input("Informe o CPF(Somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Usuário já cadastrado")
        return

    nome = input("Informe o nome: ")
    data_nascimento = input("Informe o data de nascimento: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf})

    print("Usuário cadastrado com sucesso!")


def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
