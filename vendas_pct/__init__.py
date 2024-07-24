# Importações necessárias para o pacote.
from clientes_pct import cadastrar_cliente, clientes
from compras_pct import exibir_adicionais
from dados_pct import (
    DATA,
    HORA,
    adicionais_dict,
    almoxarifado,
    cardapio,
    funcionarios,
    pedidos,
    ranking_vendas,
    save_data,
    vendas,
)
from estilização_pct import error_msg, linha, print_alinhado, sucess_msg, titulo
from ferramentas_pct import (
    input_tratado,
    leia_float,
    leia_int,
    leiaCPF,
    limpar_tela,
)

# Definição do ID do pedido.
ID_PEDIDO = 1 if len(pedidos) == 0 else len(pedidos) + 1

def salvar_pedido(pedido, codigo):
    """
    Função para salvar o pedio nos pedidos.

    Args:
        pedido (dict): Pedido do cliente.
        codigo (int): Chave que será guardada o pedido.
    """
    pedidos[codigo] = pedido
    save_data("arquivo_pedidos.dat", pedidos)


def criar_pedido():
    """
    Função principal que cria um pedido e adiciona na lista de pedidos.

    Returns:
        booleano: False caso o pedido tenha falhado;
        dict: Caso o pedido tenha sido feito corretamente.
    """
    global ID_PEDIDO
    limpar_tela()
    titulo("INFORMAÇÕES DO PEDIDO")

    # Inicializações de dicionários necessários.
    pedido = {} 
    adicional = {}

    # Entrada dos usuário.
    hamburguer = input_tratado("Nome ou ID do Hambúrguer:")
    quantidade = leia_int("Quantidade:  ")
    existe, hamburguer_nome = existencia_hamburguer(hamburguer)

    if existe:
        ingredientes = extrair_ingredientes(hamburguer_nome, quantidade)
        if verificar_ingredientes(ingredientes):
            if adicionais():
                adicional = adicionar_adicionais()
            
            cpf = informacoes_cliente()

            pedido = {
                "nome": clientes[cpf]["Nome"],
                "endereco": clientes[cpf]["Endereço"],
                "hamburguer": hamburguer_nome,
                "quantidade": quantidade,
                "preco": pegar_preco(hamburguer_nome, quantidade), 
                "adicionais": adicional,
                "status": False
            }
            salvar_pedido(pedido, ID_PEDIDO)
            ID_PEDIDO += 1
            return True
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
            for hamb in detalhes:
                if hamb == hamburguer:
                    return True, hamb
    
    # Se não encontrou o hambúrguer
    return False, False


def extrair_ingredientes(hamburguer, quantidade):
    """
    Função para extrair os ingredientes do hambúrguer e atualizar suas respectivas 
    quantidades.

    Args:
        hamburguer (str): Nome do hambúrguer
        quantidade (int): Quantidade solicitada.

    Returns:
        dict: Dicionário com os ingredientes atualizados.
    """
    ingredientes_menu = {}

    for detalhes in cardapio.values():
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
    adicional = input_tratado("Adicionais (SIM/NÃO):")
    return adicional == "SIM"


def adicionar_adicionais():
    adicionais = {}
    exibir_adicionais()
    while True:
        adicional = input_tratado("(SAIR) - Adicional/Código:")
        if adicional == "SAIR":
            break
        quantidade = leia_int("Quantidade:")
        possivel, nome_adicional = verificar_adicionais(adicional, quantidade)
        if possivel:
            preco = leia_float("Preço:  ")
            preco_real = preco * quantidade
            adicionais[nome_adicional] = [quantidade, preco_real]
        else:
            error_msg(" AQUI? Adicional não disponível!")
            input()

    return adicionais


def verificar_adicionais(adicional, quantidade):
    """
    Função que verifica se os adicionais no almoxarifado existeme  são suficientes.

    Args:
        adicional (str): Nome do item.
        quantidade (int): Quantidade solicitada.

    Returns:
        tuple: True e Nome do adicional para possível; False e False para
        não possível.
    """
    # Verifica se o adicional está disponível.
    exitir, nome = verificar_lista_adicionais(adicional)
    if exitir:
        # Faz um novo dict com os itens do almoxarifado.
        itens_dict = {itens[0]: itens[1] for itens in almoxarifado.values()}

        # Compara se o nome existe e se sua quantidade é suficiente.
        if nome not in itens_dict or quantidade > itens_dict[nome]:
            return False, False
        return True, nome
    else:
        error_msg("Adicional não disponível!")
        input(">> Enter")
        return False, False


def verificar_lista_adicionais(codigo):
    """
    Função que verifica se o adicional escolhido está disponível nos adicionais
    liberados para opção.

    Args:
        codigo (str): Nome do adicional ou sua chave.

    Returns:
        tuple: Tupla com o nome do adicional e seu valor booleano.
    """
    try:
        # Verifica se o argumento pode ser a chave do dicionário.
        id_adicional = int(codigo) 
        # Retorna um booleano e seu nome correspondente.
        return id_adicional in adicionais_dict, adicionais_dict[id_adicional] 
    
    except ValueError:
        # Se não for possível converter, faz uma list comprehension em adicionais_dict
        # e verifica se o nome do adicional existe nessa lista.
        lista_adicionais = [i for i in adicionais_dict.values()]
        return codigo in lista_adicionais, codigo



def informacoes_cliente():
    """
    Função que pega as informações do cliente.

    Returns:
        str: CPF do cliente.
    """
    cpf = leiaCPF("CPF do cliente:  ")
    if cpf not in clientes:
        cpf_cliente = cadastrar_cliente()
        return cpf_cliente
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


def extrair_informacoes(codigo):
    """
    Função para extrair as informações necessária do pedido.

    Args:
        codigo (int): Chave que acessa o pedido dentro do dicionário de pedidos.

    Returns:
        str, int, dict: Nome do hambúrguer; Quantidade do hambúrguer; 
        Adicionais pedidos.
    """

    pedido = pedidos[codigo]
    hamburguer = pedido['hamburguer']
    quantidade = pedido['quantidade']
    adicional = pedido['adicionais']
    return hamburguer, quantidade, adicional


def atualizar_ingredientes(prompt, acao):
    """
    Função que atualiza os ingredientes no almoxarifado.

    Args:
        prompt (tuple): Tupla com o nome do hambúrguer e sua quantidade.
        acao (incrementar/decrementar): Ação que irá diminuir ou voltar para o estoque 
        normal dos ingredientes.
    """
    # Definição das variáveis.
    quantidade = prompt[1]

    # Intera sobre os elementos do cardápio.
    for detalhes in cardapio.values():
        dic_ingredientes = list(detalhes.values())[0]
        for ingrediente, quantidades in dic_ingredientes.items():
            for item, infor in almoxarifado.items():
                if ingrediente == infor[0]: # Comparação de vaores.
                    if acao == "decrementar":
                        nova_quantidade = infor[1] - (quantidade * quantidades)
                        almoxarifado[item] = [infor[0], nova_quantidade]
                    elif acao == "incrementar":           
                        nova_quantidade = infor[1] + (quantidade * quantidades)
                    almoxarifado[item] = [infor[0], nova_quantidade]


def atualizar_adicional(adicionais, acao):
    """
    Função que atualiza os adicionais no almoxarifado.

    Args:
        prompt (dict): Dicionário com os ingredientes.
        acao (incrementar/decrementar): Ação que irá diminuir ou voltar para o estoque 
        normal dos ingredientes.
    """
    if len(adicionais) == 0:
        return 
    for adicional, detalhes in adicionais.items():
        quantidade = detalhes[0]
        for item, infor in almoxarifado.items():
            if adicional == infor[0]:
                if acao == "decrementar":
                    nova_quantidade = infor[1] - quantidade
                    almoxarifado[item] = [infor[0], nova_quantidade]
                elif acao == "incrementar":           
                    nova_quantidade = infor[1] + quantidade
                almoxarifado[item] = [infor[0], nova_quantidade]


def deletar_pedido(codigo):
    """
    Função que deleta um pedido dos pedidos.

    Args:
        codigo (int): Chave do hambúrguer.

    Returns:
        booleano: True se o pedido tiver sido deletado. False se não encontrado.
    """
    if codigo in pedidos:
        del pedidos[codigo]
        save_data("arquivo_pedidos.dat", pedidos)
        return True
    else:
        return False


def listar_pedidos():
    """Função para exibir os pedidos."""
    limpar_tela()
    linha()
    if len(pedidos) != 0:
        for codigo, detalhes in pedidos.items():
            print_alinhado("N° Pedido:", codigo)
            print_alinhado("Cliente:", detalhes["nome"])
            print_alinhado("Endereço:", detalhes["endereco"])
            print_alinhado("Hamburguer:", detalhes["hamburguer"])
            print_alinhado("Quantidade:", detalhes["quantidade"])
            print()
            print_alinhado("Prç. Hambúrguer's:", f"R$ {detalhes['preco']:.2f}")
            print()
            adicionais = detalhes["adicionais"]
            preco_adc = 0

            if adicionais:
                for nome, infor in adicionais.items():
                    print(f"Adicional: {nome}")
                    print(f"\tQuantidade: {infor[0]} unidade(s)")
                    print(f"\tPreço: R$ {infor[1]}")
                    preco_adc += infor[1]
            print(f"Total: R$ {preco_adc + detalhes['preco']}")
            linha()
    else:
        error_msg("Não há pedidos para listar.")
        return


def editar_pedido(codigo):
    """
    Função que modifica o pedido do cliente.

    Args:
        codigo (int): Chave que está o pedido do cliente.
    """
    limpar_tela()
    titulo("EDIÇÃO DE PEDIDO")
    if codigo in pedidos:
        adicional = {}

        edicao = ""
        while True:
            edicao = input_tratado("Mudar (1) Hamburguer / (2) Adicionais / (0) Sair \n")

            match edicao:
                case "1" | "HAMBURGUER":
                    hamburguer, quantidade = mudar_hamburguer()
                case "2" | "ADICIONAIS":
                    adicional = mudar_adicionais()
                case "0":
                    break

        pedidos[codigo]["hamburguer"] = hamburguer
        pedidos[codigo]["quantidade"] = quantidade
        pedidos[codigo]["adicionais"] = adicional
        pedidos[codigo]["preco"] = pegar_preco(hamburguer, quantidade)
        save_data("arquivo_pedidos.dat", pedidos)
        return True
    else:
        return False

    
def mudar_hamburguer():
    """
    Função que mudao nome do hambúrguer no pedido realizado.

    Returns:
        tuple: Tupla com o nome do novo hambúrguer e sua quantidade.
    """
    hamburguer = input_tratado("Nome ou ID do Hambúrguer:")
    quantidade = leia_int("Quantidade:  ")
    existe, hamburguer_nome = existencia_hamburguer(hamburguer)

    if existe:
        ingredientes = extrair_ingredientes(hamburguer_nome, quantidade)
        if verificar_ingredientes(ingredientes):
            return hamburguer_nome, quantidade
        
    return False


def mudar_adicionais():
    """
    Função que muda os dicionários

    Returns:
        dict: Dicionário com os adicionais
    """
    adicional = adicionar_adicionais()
    return adicional


def fechar_vendas():
    """
    Fecha as vendas do dia para um funcionário específico, limpa os pedidos e salva os 
    dados no relatório de vendas.

    Parâmetros:
    - cpf (str): CPF do funcionário que está fechando as vendas.

    Estruturas de dados usadas:
    - funcionarios (dict): Dicionário contendo os dados dos funcionários. Cada chave é 
    o CPF e o valor é um dicionário com detalhes do funcionário.
    - vendas (dict): Dicionário onde as chaves são datas e os valores são dicionários 
    com detalhes das vendas daquele dia.
    - pedidos (dict): Dicionário contendo os pedidos realizados. Cada chave é o 
    id_pedido e o valor é um dicionário com detalhes do pedido.

    Fluxo da função:
    1. Solicita o CPF do funcionário e define a data e hora atuais.
    2. Verifica se o funcionário existe no dicionário `funcionarios`.
    3. Se o funcionário for encontrado, cria um relatório de vendas para a data atual 
    contendo a hora, nome do funcionário, CPF e os pedidos realizados.
    4. Limpa os pedidos realizados do dicionário `pedidos`.
    5. Salva os dados atualizados nos arquivos "arquivo_vendas.dat" 
    e "arquivo_pedidos.dat".
    6. Atualiza o ranking de vendas com base nos pedidos realizados.
    7. Exibe uma mensagem de sucesso e aguarda o pressionamento da tecla Enter.

    Exceções:
    - KeyError: Lançada se o CPF fornecido não corresponder a nenhum funcionário no 
    dicionário `funcionarios`.

    Exemplo de uso:
        fechar_vendas("77788899911")
    """
    cpf = leiaCPF("CPF: ")

    funcionario_cpf = ''

    try:
        funcionario_cpf = funcionarios[cpf] # Verificação se o funcionário existe
    except KeyError:
        error_msg("Funcionário não encontrado")
        return

    # Criaças do relatório da data especifica
    vendas[DATA] = {
        "Hora": HORA,
        "Funcionário": funcionario_cpf["Nome"],
        "CPF": cpf,
        "Pedidos Realizados": pedidos.copy(),  
    }

    atualizar_ranking(pedidos)
    pedidos.clear() # Limpar dos pedidos

    # Salvamento de dados
    save_data("arquivo_vendas.dat", vendas) 
    save_data("arquivo_pedidos.dat", pedidos)

    sucess_msg("Vendas fechadas com sucesso!")


def atualizar_ranking(pedidos):
    """
    Atualiza o ranking de hambúrgueres mais pedidos com base nos dados fornecidos.

    Args:
        pedidos (dict): Um dicionário contendo os pedidos realizados.
    """
    for infor in pedidos.values():
        hamburguer = infor["hamburguer"]
        quantidade = infor["quantidade"]
        if hamburguer in ranking_vendas:
            ranking_vendas[hamburguer] += quantidade
        else:
            ranking_vendas[hamburguer] = quantidade
    save_data("ranking_vendas.dat", ranking_vendas)


def mudar_status_hamburguer(codigo):
    """
    Função que modifica o status do hamburguer confirmado

    Args:
        codigo (int): O hamburguer torna True, ou seja, 
        ele foi confirmado.
    """
    pedidos[codigo]['status'] = True
    save_data("arquivo_pedidos.dat", pedidos)


def verificar_pedidos():
    """
    Verifica se todos os pedidos foram confirmados.

    Returns:
        booleano: False para pedidos pendentes; True para o 
        contrário.
    """
    liberar = True
    for detalhes in pedidos.values():
        if detalhes['status'] == True:
            continue
        else:
            detalhes['status'] == False
            liberar = False
            return liberar
    return liberar
