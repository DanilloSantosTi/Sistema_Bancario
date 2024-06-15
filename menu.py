import textwrap


def menu():
    menu = """\n
    ----------- MENU -----------
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar conta
    [nu]\tNovo usuário
    [q]\tSair do sistema
    """
    return input(textwrap.dedent(menu))

