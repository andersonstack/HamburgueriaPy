# Importações necessárias para a modularização.
from tools import limpar_tela, input_tratado, leia_float, leia_int, leiaCPF
from views import titulo
from data import cardapio, almoxarifado, clientes, pedidos, save_data
from clientes import cadastrar_cliente

cardapio = {1: {
    "X-TUDO": {
        "PÃO DE HAMBÚRGUER": 2,
        "HAMBURGUER BOVINO": 1
    },
    "PRECO": 12
}}

def criar_pedido():
    """
    Função principal que cria um pedido e adiciona na lista de pedidos.

    Returns:
        booleano: False caso o pedido tenha falhado;
        dict: Caso o pedido tenha sido feito corretamente.
    """
    limpar_tela()
    titulo("INFORMAÇÕES DO PEDIDO")

    # Inicializações de dicionários necessários.
    pedido = {} 
    adicional = {}

    # Definição do ID do pedido.
    ID_PEDIDO = 1 if len(pedidos) == 0 else len(pedidos) + 1

    # Entrada dos usuário.
    hamburguer = input_tratado("Nome ou ID do Hambúrguer: ")
    quantidade = leia_int("Quantidade:  ")
    existe, hamburguer_nome = existencia_hamburguer(hamburguer)

    if existe:
        ingredientes = extrair_ingredientes(hamburguer_nome, quantidade)
        if verificar_ingredientes(ingredientes):
            if adicionais():
                adicional = adicinonar_adicionais()
            
            cpf = informacoes_cliente()

            pedido = {
                "nome": clientes[cpf]["Nome"],
                "endereco": clientes[cpf]["Endereço"],
                "hamburguer": hamburguer_nome,
                "quantidade": quantidade,
                "preco": pegar_preco(hamburguer_nome, quantidade), 
                "adicionais": adicional
            }
            pedidos[ID_PEDIDO] = pedido
            save_data("arquivo_pedidos.dat", pedidos)
            return pedido
        else:
            return False
    else:
        return False


def existencia_hamburguer(hamburguer):
    """
    Verifica se o hambúrguer existe no cardápio.

    Args:
        hamburguer (int/str): Valor que corresponde o hambúrguer no cardápio.

    Returns:
        booleano: True caso exista; False caso não.
    """
    try:
        # Tenta converter a entrada para um inteiro (ID)
        hamburguer_id = int(hamburguer)
        if hamburguer_id in cardapio:
            # Retorna o nome do hambúrguer usando o ID
            return True, list(cardapio[hamburguer_id].keys())[0]
    except ValueError:
        # Se a conversão falhar, trata como nome
        for detalhes in cardapio.values():
            for hamb in detalhes.keys():
                if hamb == hamburguer:
                    return True, hamb
    
    # Se não encontrou o hambúrguer
    return False, False


def extrair_ingredientes(hamburguer, quantidade):
    """
    Função para extrair os ingredientes do hambúrguer e atualizar suas respectivas quantidades.

    Args:
        hamburguer (str): Nome do hambúrguer
        quantidade (int): Quantidade solicitada.

    Returns:
        dict: Dicionário com os ingredientes atualizados.
    """
    ingredientes_menu = {}

    for codigo, detalhes in cardapio.items():
        hamburguer_menu = list(detalhes)[0]
        ingredientes = list(detalhes.values())[0]

        if hamburguer == hamburguer_menu:
            for ingrediente, quantidades in ingredientes.items():
                ingredientes_menu[ingrediente] = quantidades * quantidade
    
    return ingredientes_menu


def verificar_ingredientes(ingredientes):
    """
    Função que verifica se os ingredientes são suficientes para concluir o pedido.


    Args:
        ingredientes (dict): Dicionário com os ingredientes do hamburguer.

    Returns:
        booleano: False caso os ingredientes sejam insuficientes.
    """
    # Definindo list comprehension em itens_dict
    itens_dict = {itens[0]: itens[1] for itens in almoxarifado.values()}
    
    # Intera sobre o dicionário de ingredientes.
    for ingrediente, quantidade in ingredientes.items():
        if ingrediente not in itens_dict or quantidade > itens_dict[ingrediente]:
            return False
    return True


def adicionais():
    adicional = input_tratado("Adicionais (SIM/NÃO):    ")
    return True if adicional == "SIM" else False


def adicinonar_adicionais():
    adicionais = {}
    while True:
        adicional = input_tratado("(SAIR) - Adicional:  ")
        quantidade = leia_int("Quantidade:  ")
        if adicional == "SAIR":
            break
        if verificar_adicionais(adicional, quantidade):
            preco = leia_float("Preço:  ")
            adicionais[adicional] = preco * quantidade

    return adicionais


def verificar_adicionais(adicional, quantidade):
    """
    Função que verifica se os adicionais no almoxarifado existeme  são suficientes.

    Args:
        adicional (str): Nome do item.
        quantidade (int): Quantidade solicitada.

    Returns:
        booleano: True para possível adicionar adicional; False para o contrário.
    """
    itens_dict = {itens[0]: itens[1] for itens in almoxarifado.values()}
    
    if adicional not in itens_dict or quantidade > itens_dict[adicional]:
        return False
    return True


def informacoes_cliente():
    """
    Função que pega as informações do cliente.

    Returns:
        str: CPF do cliente.
    """
    cpf = leiaCPF("CPF do cliente:  ")
    if cpf not in clientes:
        cadastrar_cliente()
    return cpf


def pegar_preco(hamburguer, quantidade):
    """
    Função que pega o preço do hambúrguer no cardápio.

    Args:
        hamburguer (str): Nome do hambúrguer.
        quantidade (int): Quantidade solicitada.

    Returns:
        float: Preço do hambúrguer.
    """
    for detalhes in cardapio.values():
        if hamburguer == list(detalhes.keys())[0]:
            return detalhes['PRECO'] * quantidade

