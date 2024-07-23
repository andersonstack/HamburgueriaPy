# Importações necessárias para o pacote.
from ferramentas_pct import limpar_tela


def principal():
    """
    Função para mostrar as opções possíveis de main.
    """
    print("1 ↪︎ Módulo Compras")
    print("2 ↪︎ Módulo Almoxarifado")
    print("3 ↪︎ Módulo Vendas")
    print("4 ↪︎ Módulo Funcionários")
    print("5 ↪︎ Módulo Clientes")
    print("6 ↪︎ Módulo Relatórios")
    print("7 ↪︎ Módulo Informações")
    print("0 ↪︎ Sair")
    linha()


def operacoes_clientes():
    """
    Função auxiliar que mostra as operações possíveis em módulos de clientes.
    """
    limpar_tela()
    titulo("Clientes")
    print("1 ↪︎ Cadastrar Cliente")
    print("2 ↪︎ Lista de Clientes")
    print("3 ↪︎ Editar Clientes")
    print("4 ↪︎ Excluir Clientes")
    print("0 ↪︎ Sair")


def operacoes_funcionarios():
    """
    Função auxiliar que mostra as operações possíveis em módulos de funcionários.
    """
    limpar_tela()
    titulo("Funcionários")
    print("↪︎ 1.  Quadro de funcionários      ")
    print("↪︎ 2.  Gerenciar funcionários      ")
    print("↪︎ 0.  Sair      ")
    linha()


def exibir_item(informacoes, prompt):
    print(f"\033[1;33;7m{'Código':^10}|{'Nome':^55}|{'Quantidade':^55}")
    item = informacoes[0]
    quantidade = informacoes[1]
    print(f"{prompt:^10}|{item:^55}|{quantidade:^55}\033[m")


def quadro_almoxarifado(almoxarifado):
    titulo("Almoxarifado")
    print(f"\033[1m{'ID':^5}|{'Nome':^60}|{'Quantidade':^60}\033[m")
    print('-' * 125)
    for chave, valor in almoxarifado.items():
        id_item = chave
        nome = valor[0]
        quantidade = valor[1]
        print(f"{id_item:^5}|{nome:^60}|{quantidade:^60}")
        print('-' * 125)


def print_alinhado(text, valor=""):
    print(f"{text:<15}", valor)


def cabecalho(text):
    print("\033[1m=\033[m" * 125)
    print(f"\033[1m{text.center(125)}\033[m")
    print("\033[1m=\033[m" * 125)
    print()


def titulo(text):
    """Função para padronização de títulos no código principal"""
    print("═" * 125)
    print(f"\033[1m▶  {text}\033[m")
    print("═" * 125)
    print()


def subtitulo(text):
    print("\033[31m=\033[m" * 125)
    print(f"\033[1;31m{text.center(125)}")
    print("\033[31m=\033[m" * 125)


def quadro(cpf, nome, idade, endereco=False):
    """Função para exibir quadros"""
    columns_cpf = 15
    columns_nome = 50
    columns_idade = 10
    columns_endereco = 50 if endereco else 0

    if columns_endereco == 0:  # Fazer um quadro "Responsivo"
        columns_cpf = 30
        columns_nome = 80
        columns_idade = 15

        total_columns = columns_cpf + columns_nome + columns_idade + columns_endereco
    else:
        total_columns = columns_cpf + columns_nome + columns_idade + columns_endereco

    print("=" * total_columns)
    if endereco:
        print(
            f"{'CPF':^{columns_cpf}}|{'Nome':^{columns_nome}}|{'Idade':^{columns_idade}}|{'Endereço':^{columns_endereco}}"
        )
    else:
        print(
            f"{'CPF':^{columns_cpf}}|{'Nome':^{columns_nome}}|{'Idade':^{columns_idade}}"
        )
    print("=" * total_columns)

    if endereco:
        print(
            f"{cpf:^{columns_cpf}}|{nome:^{columns_nome}}|{idade:^{columns_idade}}|{endereco:^{columns_endereco}}"
        )
    else:
        print(
            f"{cpf:^{columns_cpf}}|{nome:^{columns_nome}}|{idade:^{columns_idade}}"
        )
    print("=" * total_columns)


def linha():
    print()
    print("\033[1m¨\033[m" * 125)
    print()


def error_msg(text):
    print()
    print("\033[1;31;7m >> " + text + "\033[m")
    print()


def sucess_msg(text):
    print()
    print("\033[1;32;7m >> " + text + "\033[m")
    print()
