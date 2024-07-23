# Importações necessárias para o pacote.
from dados_pct import clientes, save_data, clientes_inativos
from estilização_pct import (
    cabecalho,
    error_msg,
    linha,
    print_alinhado,
)
from ferramentas_pct import input_tratado, leia_int, leia_nome, leiaCPF, limpar_tela


def quadro_clientes():
    """
    Função auxiliar que mostra lista os clientes de forma de um quadro.
    """
    limpar_tela()
    cabecalho("Lista de Clientes")
    for cpf in clientes:
        cliente = clientes[cpf]['Nome']
        endereco = clientes[cpf]['Endereço']

        linha()
        print_alinhado("CPF:", cpf)
        print_alinhado("Nome:", cliente)
        print_alinhado("Endereço:", endereco)
        linha()

    input(">> Enter")


def cadastrar_cliente():
    """
    Função para cadastrar clientes.

    A função solicita o cpf para o cadastro do cliente, verifica se o cliente existe
    e, se não existir, cadastra e armazena as informações.
    """
    limpar_tela()
    cabecalho("Cadastrar clientes")

    cpf = leiaCPF("CPF:   ")

    if cpf not in clientes:
        nome = leia_nome("Nome:  ")
        rua = leia_nome("Rua:  ")
        bairro = leia_nome("Bairro:   ")
        numero = leia_int("Número:  ")
        endereco = f"{rua}, {bairro}, {numero}"

        clientes[cpf] = {"Nome": nome, "Endereço": endereco}

        save_data("arquivo_clientes.dat", clientes)

        return input("Cliente cadastrado.")

    else:
        return input("Cliente já está no sistema.")


def editar_clientes():
    """
    Função para edição de clientes.

    A função solicita o CPF a ser editado para fazer as edições do escolhido. Verifica a 
    existência 
    e caso exista, as edições podem ser feitas.

    Returns:
        input: Retorna um input de "Cliente editado" ou um error_msg "Cliente não 
        encontrado".

    Fluxo:
        1. Solicita a entrada de um CPF.
        2. Verifica a existência do CPF.
            2.1 Se existe:
                - Solicita nome, rua, bairro e número.
                - Atualiza os dados no dicionário de clientes[cpf].
                    Ex.: clientes = {
                        '11133322200': {
                            'Nome': Anderson,
                            'Endereço': f'{Rua}, {bairro}, {numero}'
                        }
                    }
                - Salva os dados em um arquivo.
                - Retorna input("Cliente editado").
            2.2 Se não existe:
                - Exibe erro_msg("Cliente não encontrado").
                - Retorna um input(">> Enter") para seguir o programa.

    """
    cpf = leiaCPF("CPF: ")
    if cpf in clientes:
        # Atualização do nome
        nome = leia_nome("Nome: ")

        # Atualização do endereço
        rua = leia_nome("Rua:  ")
        bairro = leia_nome("Bairro: ")
        numero = leia_int("Número:  ")
        endereco = f"{rua}, {bairro}, {numero}"

        # Atualizações dos dados diretamente no dicionário
        clientes[cpf] = {"Nome": nome, "Endereço": endereco}

        save_data("arquivo_clientes.dat", clientes)

        return input("Cliente editado.")
    else:
        error_msg("Cliente não encontrado.")
        return input(">> Enter.")


def excluir_cliente():
    """
    Função para excluir um cliente.

    A função solicita o CPF. Se o CPF estiver em Clientes, pede confirmação de exclusão, 
    casosim, o cliente é removido e os arquivos são salvos. Caso não, a operação é 
    cancelada.

    Returns:
        input: De exclusão do cliente.
                De operação cancelada.
    """
    cpf = leiaCPF("CPF: ")
    if cpf in clientes:
        confirm = input_tratado(
            f"Deseja excluir o cliente {clientes[cpf]['Nome']} (S/N)")
        match confirm:
            case 'S':
                atualizar_clientes_inativos(cpf)
                clientes.pop(cpf)
                save_data("arquivo_clientes.dat", clientes)

                return input("Cliente deletado. >> Enter")
            case 'N':
                return input("Operação cancelada. >> Enter")
    else:
        error_msg("Cliente não encontrado.")
        input(">> Enter")


def atualizar_clientes_inativos(cpf):
    """
    Função que pega os dados dos clientes deletados e coloca-os em um arquivo para manter os dados.

    Args:
        cpf (str): CPF do cliente.
    """
    nome = clientes[cpf]["Nome"]
    endereco = clientes[cpf]["Endereço"]
    if cpf not in clientes_inativos:
        clientes_inativos[cpf] = {}
        
    clientes_inativos[cpf] = {
        "Nome": nome,
        "Endereço": endereco
    }
    save_data("clientes_deletados.dat", clientes_inativos)