from views import *
from data import *
from tools import *

def quadro_clientes():
    """
    Função auxiliar que mostra lista os clientes de forma de um quadro.
    """
    limpar_tela()
    cabecalho("Lista de Clientes")
    for nome, dados in clientes.items():
        cliente = clientes[nome]['Nome']
        endereco = clientes[nome]['Endereço']

        linha()
        print_alinhado("Nome:", cliente)
        print_alinhado("Endereço:", endereco)
        linha()

    input(">> Enter")


def cadastrar_cliente():
    """
    Função para cadastrar clientes.

    A função solicita o cpf para o cadastro do cliente, verifica se o cliente existe
    e, se não existir, cadastra e armazena as informações.

    Returns:
        input: Finalização da tarefa. Exibe uma mensagem de sucesso ou de já cadastrado.
    
    Fluxo:
        1. Solicita entrada do CPF.
        2. Verifica se CPF existe.
            2.1 Não existe:
                - Solicita entrada de nome, rua, numero e bairro.
                - Insere os dados no dicionário de clientes.
                    Ex.: clientes = {
                        '11133322200': {
                            'Nome': Anderson,
                            'Endereço': f'{Rua}, {bairro}, {numero}'
                        }
                    }
                - Salva os dados em um arquivo.
                - Retorna input("Cliente cadastrado")
            2.2 Já existe:
                - Retorna input("Cliente já está no sistema")
    """
    limpar_tela()
    cpf = leiaCPF("CPF:   ")

    cabecalho("Cadastrar clientes")

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

    A função solicita o CPF a ser editado para fazer as edições do escolhido. Verifica a existência 
    e caso exista, as edições podem ser feitas.

    Returns:
        input: Retorna um input de "Cliente editado" ou um error_msg "Cliente não encontrado".

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