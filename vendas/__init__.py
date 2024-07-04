from data import *
from views import *
from datetime import datetime
from tools import *
from clientes import clientes, cadastrar_cliente
from menu import exibir_cardapio

def criar_pedido():
    """
    Função para criar um pedido de hambúrguer, adicionando-o ao sistema de pedidos.

    Gera um ID para o pedido, permite selecionar um hambúrguer no cardápio,
    verifica a disponibilidade de ingredientes, adiciona opcionais, solicita o CPF do
    cliente cadastro se necessário, e regista o pedido no sistema.
    
    Se ingredientes estiverem disponíveis e o pedido for concluído com sucesso, exibe uma
    mensagem de sucesso e salva os dados do pedido em um arquivo.   

    Retorna: None 

    Fluxo da função:
        1. Solicita o nome do hamburguer e sua quantidade, define o id_pedido, a lista de pedido_cliente e a lista de adicionais.
        2. Extrai os ingredientes usando a função extrair_ingredientes(nome_hamburguer, quantidade).
        3. Verifica a existência dos ingredientes.
        4. Verifica a quantidade suficiente dos ingredientes e o jogo em uma lista.
            4.1 Se houver ingredientes insuficientes, exibe um error_msg e uma intera sobre a lista de itens_insuficientes.
            4.2 Se não houver, solicita os adicionais. Caso sim, o processo da função adicinar_adicionais é ativada.
        5. Verifica o preço total, quantidade de hambúrguer pelo seu preço.
        6. Intera sobre os adicionais para atualizar o preço total com o preço dos adicionais.
        7. Solicita o CPF do cliente.
            7.1 Caso não esteja cadastrado, o cliente deve ser cadastrado.
        8. Insere todos os dados em pedido_cliente.
        9. Exibe mensagem de sucesso.
        10. Insere pedido_cliente em pedidos a partir do ID definido dinâmicamente.
        11. Salva os arquivos.
        12. Incrementa o id em 1.
    
    Formato de pedido_cliente e adicionais:
        pedido_cliente = [
                id_pedido,
                clientes[cpf_cliente]['Nome'],
                clientes[cpf_cliente]['Endereço'],
                nome_hamburguer,
                quantidade, 
                adicionais, 
                preco_total
            ]
        adicionais = [
            ['ITEM', 2, 4] 
                # adicionais[0] -> nome do item
                # adicionais[1] -> quantidade do item
                # adicionais[2] -> preço unitário
        ]
        
        Ex.:
        pedido_cliente = [
                1,
                "Anderson",
                "Rua X, Bairro Y, 78",
                "HAMBÚRGUER CLÁSSICO",
                "1", 
                [['COCA', 2, 4]],  
                14
            ]
    """
    limpar_tela()
    id_pedido = 1 if len(pedidos) == 0 else list(pedidos.keys())[-1] + 1 # Criação de um ID com base no dict() de pedidos
    pedido_cliente = [] # Lista para o pedido
    adicionais = [] # Lista para os adicionais
    exibir_cardapio() # Exibir o cardápio
    nome_hamburguer = leia_item("Nome: ").upper()
    quantidade = leia_int("Quantidade: ")

    ingredientes = extrair_ingredientes(nome_hamburguer, quantidade) # Extrair os ingredientes do hambúrguer caso ele exista

    if ingredientes:
        itens_insuficientes = verificar_ingredientes(ingredientes)

        if itens_insuficientes:
            error_msg("Pedido não pode ser feito. Ingredientes insuficientes.")
            for item in itens_insuficientes:
                print(item)
        else:
            adicionar_adicionais(adicionais) # Adicionais caso necessário

            preco_total = cardapio[nome_hamburguer][
                                "Preço"] * quantidade

            for i in adicionais:
                preco_total += i[1] * i[2]

            cpf_cliente = leiaCPF("CPF: ")                                      
            if cpf_cliente not in clientes:
                cadastrar_cliente()

            pedido_cliente = [
                id_pedido,
                clientes[cpf_cliente]['Nome'],
                clientes[cpf_cliente]['Endereço'],
                nome_hamburguer,
                quantidade, 
                adicionais, 
                preco_total
            ]

            sucess_msg("Pedido lançado no sistema")

            pedidos[id_pedido] = pedido_cliente # Pedido colocado no dict() pedidos
            save_data("arquivo_pedidos.dat", pedidos) # Salvamento de dados
            id_pedido += 1

    input("Pressione << Enter >> para continuar...")


def adicionar_adicionais(adicionais):
    """
    Função para acrescentar os adicionais caso necessário

    Args:
        adicionais (lista): Lista de adicionais adicionado ao pedido do cliente
    """
    adicional = input_tratado("Deseja adicionar algum adicional? [S/N] ").upper()
    if adicional[0] == 'S':
        while True:
            nome_adicional = leia_item("[SAIR] Nome: ").upper()
            if nome_adicional.upper() == 'SAIR':
                break

            quantidade_adicional = leia_int("Quantia: ")

            ids, checagem = check_buy(nome_adicional)
            if checagem:
                if verificar_acrescimos(checagem, quantidade_adicional):
                    preco = leia_float("Preço: ")
                    adicionais.append([nome_adicional, quantidade_adicional, preco])
            else:
                error_msg("Acréscimo em falta")


def listar_pedidos():
    """
    Lista todos os pedidos armazenados no dicionário de pedidos.

    Esta função limpa a tela, imprime uma linha de separação, e então itera sobre
    cada pedido no dicionário de pedidos, imprimindo detalhes como número do pedido,
    nome do cliente, endereço, nome do hambúrguer, quantidade, adicionais e o preço total.
    """
    limpar_tela()
    linha()
    for id_pedido, pedido in pedidos.items():
        nome_cliente = pedido[1]
        endereco = pedido[2]
        nome_hamburguer = pedido[3]
        quantidade_hamburguer = pedido[4]
        adicionais = pedido[5]
        preco_pedido = pedido[-1]

        print_alinhado("N° Pedido", id_pedido)
        print_alinhado("Cliente:", nome_cliente)
        print_alinhado("Endereço:", endereco)
        print_alinhado("Hambúrguer:", nome_hamburguer)
        print_alinhado("Quantidade:", quantidade_hamburguer)
        for detalhes in adicionais:
            nome_adicional = detalhes[0]
            quantidade_adicional = detalhes[1]
            preco_adicional = detalhes[2]

            print_alinhado(f"{nome_adicional}:", f"{quantidade_adicional}un. R$ {preco_adicional}")
            print_alinhado("Preço Total:", f"R$ {preco_pedido}")

        linha()


def verificar_pedido(id_pedido):
    """
    Função que verifica se o pedido existe no dicionário de pedidos.

    Args:
        id_pedido (int): ID do pedido em pedidos.

    Returns:
        booleano: True se existir
                    False se não existir
    """
    return id_pedido in pedidos


def extrair_ingredientes(nome, quantidade):
    """
    Extrai os ingredientes e dados do hambúrguer.

    Args:
        nome (str): Nome do hambúrguer.
        quantidade (int): Quantidade solicitada.

    Returns:
        dict or None: Dicionário com os detalhes dos ingredientes ajustados pela quantidade solicitada.
                      Retorna None se o hambúrguer não for encontrado no cardápio.
    """
    if nome in cardapio: # Verificação se o hambúrguer está no cardápio
        ingredientes = cardapio[nome]
        ingredientes_ajustados = {k: v * quantidade for k, v in ingredientes.items() if k != 'Preço'} # Atualização de quantidade
        ingredientes_ajustados['Preço'] = ingredientes.get('Preço', 0) * quantidade # Atualização de preço
        return ingredientes_ajustados

    else:
        error_msg("Hambúrguer não encontrado no cardápio") # Caso não exista retorna None
        return None
    

def verificar_ingredientes(detalhes):
    """
    Verifica a disponibilidade dos ingredientes no almoxarifado para um determinado item do cardápio.

    Args:
        detalhes (dict): Um dicionário contendo os detalhes do item do cardápio. As chaves são os nomes dos ingredientes
                         e os valores são as quantidades necessárias de cada ingrediente.

    Returns:
        list: Uma lista contendo os nomes dos ingredientes que estão em falta ou com quantidade insuficiente no almoxarifado.
    """
    itens_insuficientes = []

    for nome, quantidade in detalhes.items():
        if nome == 'Preço':  # Ignora o preço, pois não é um ingrediente
            continue
        ids, dados = check_buy(nome)
        if dados:
            quantia = dados[1]  # A quantidade está na segunda posição da lista
            if quantia >= quantidade:
                continue
            else:
                itens_insuficientes.append(nome)
        else:
            itens_insuficientes.append(nome)
    
    return itens_insuficientes


def verificar_acrescimos(detalhes, quantia):
    """
    Verifica se há quantidade suficiente de um item no almoxarifado.

    Args:
        detalhes (list): Detalhes do item no almoxarifado, onde o segundo elemento (índice 1) representa a quantidade disponível.
        quantia (int): Quantidade requerida do item.

    Returns:
        bool: Retorna True se a quantidade disponível for suficiente. Retorna False e exibe uma mensagem de erro se a quantidade for insuficiente.
    """
    if detalhes[1] >= quantia:
        return True
    else:
        error_msg(f"Quantia insuficiente: {detalhes[1]} quantidades no almoxarifado ")
        return False
    

def decrementar_ingredientes(codigo):
    """
    Decrementa a quantidade de ingredientes utilizados em um pedido no almoxarifado.

    Utilizada para confirmação de pedidos.

    Args:
        codigo (int): ID do pedido no dicionário `pedidos`.

    Returns:
        str: Retorna uma mensagem de aviso se o pedido não for encontrado.

    Fluxo da função:
        1. Verifica se o pedido existe.
        2. Decrementa os adicionais se houver.
        3. Calcula a quantidade total de cada ingrediente do hambúrguer.
        4. Atualiza as quantidades de ingredientes no almoxarifado.
    """
    if verificar_pedido:

        adicionais = pedidos[codigo][-2]
        
        if len(adicionais) != 0:
            decrementar_adicionais(codigo)

        pedido_cliente = pedidos[codigo]
        nome_hamburguer = pedido_cliente[3]  # Acessar nome do hambúrguer
        ingredientes_hamburguer = cardapio[nome_hamburguer]  # Acessar o dict de ingredientes do hambúrguer no cardápio
        quantidade_hamburguer = pedido_cliente[4]  # Acessar quantidade solicitada pelo cliente

        for ingrediente in ingredientes_hamburguer:  # Acessar os ingredientes
            if ingrediente == 'Preço':
                continue
            quantidade_ingrediente = ingredientes_hamburguer[ingrediente] # Definir quantidade de ingredientes
            quantidade_total = quantidade_hamburguer * quantidade_ingrediente # Quantidade total dos ingredientes 
            
            for ids, detalhes in almoxarifado.items():
                item_almoxarifado = detalhes[0]

                if ingrediente == item_almoxarifado:  # Verificar se o adicional existe no almoxarifado
                    almoxarifado[ids][1] -= quantidade_total
            
    else:
        return error_msg("Pedido não encontrado!")


def decrementar_adicionais(codigo):
    """
    Decrementa a quantidade de adicionais utilizados em um pedido no almoxarifado.

    Utilizada para confirmação de pedidos.

    Args:
        codigo (int): Keys do dict() de pedidos

    Fluxo da função:
        1. Verifica se o pedido existe.
        2. Acessa a lista de adicionais do pedido.
        3. Itera sobre cada adicional na lista e decrementa a quantidade no almoxarifado.
        4. Salva os dados atualizados do almoxarifado.
    """

    if verificar_pedido:
        pedido_cliente = pedidos[codigo]
        lista_adicionais = pedido_cliente[5]  # Acessar a lista dos adicionais
        for adicional in lista_adicionais:  # Iterar sobre os adicionais da lista
            nome_adicional = adicional[0]
            quantidade_adicional = adicional[1]

            for ids, detalhes in almoxarifado.items():
                item_almoxarifado = detalhes[0]
                if nome_adicional == item_almoxarifado:  # Verificar se o adicional existe no almoxarifado
                    almoxarifado[ids][1] -= quantidade_adicional
        
    else:
        return error_msg("Pedido não encontrado!")
    
    save_data("arquivo_almoxarifado.dat", almoxarifado)


def perca_de_ingredientes(codigo):
    """
    Função que recebe o código de um pedido já confirmado e feito. Como os ingredientes de uma hambúrguer real
    não podem voltar para cozinha, eles são gerados como perca a não ser que outro cliente escolha esse hambúrguer.

    Args:
        codigo (int): Chave a qual está armazenado o pedido em pedidos.

    Returns:
        input: Solicita enter para continuar o código.
    
    Fluxo:
        1. A função define o hamburguer e a quantidade do pedido
        2. Intera sobre o cardapio para encontrar os valores correspondentes.
        3. Compara se o hamburguer no cardaio é igual ao hamburguer definido na função.
        4. Intera sobre os ingredientes desse hamburguer.
        5. Se ingrediente for igual a "Preço", ignore.
        6. Pega a quasntia do cardapio e multiplica pela quantia pedida pelo cliente.
        7. Ingrediente e quantia é colocado em gerar_percas.
        8. Pedido é removido de pedidos.
        9. Arquivos são salvos.
        10. Exibe mensagem de sucesso.
    """
    hamburguer = pedidos[codigo][3]
    quantidade = pedidos[codigo][4]
    for hamburguers, ingredientes in cardapio.items():
        if hamburguers == hamburguer:
            for ingrediente, quantia in ingredientes.items():
                
                if ingrediente == 'Preço':
                    continue

                quantia *= quantidade
                gerar_percas(ingrediente, quantia)
    
    pedidos.pop(codigo)
    save_data("arquivo_pedidos.dat", pedidos)
    sucess_msg("Pedido removido e anexado em percas.")
    return input(">> Enter")


def gerar_percas(ingrediente, quantidade):
    """
    Função que gera o relataório de percas de pedidos.

    A função recebe como parâmetro o ingrediente e sua quantidade correspondente do pedido. A partir da data,
    as informações são adicionais ao dicionário percas_ingredientes.

    Args:
        ingrediente (str): Nome do ingrediente
        quantidade (int): Quantidade do ingrediente

    Fluxo:
        1. Verifica se a data existe no dicionario, caso não, cria para receber um dict();
        2. Verifica se o ingrediente existe naquele data respectiva no dicionário, caso não, cria e iguala a 0.
        3. Acrescenta as informações em percas_ingredientes a partir de seus dados.

    Formato do dicionário:
        percas_ingredientes = {
            "04/07/2024": {"Ingrediente": quantidade}
            ...
        }
    """
    if data not in percas_ingredientes:
        percas_ingredientes[data] = {}
    
    if ingrediente not in percas_ingredientes[data]:
        percas_ingredientes[data][ingrediente] = 0
    
    percas_ingredientes[data][ingrediente] += quantidade
    save_data("percas_ingredientes.dat", percas_ingredientes)



def deletar_pedido(codigo):
    """
    Função para deletar pedidos que não foram confirmados.

    Args:
        codigo (int): ID do pedido a ser deletado.

    Returns:
        bool: Retorna True se o pedido foi deletado com sucesso, False caso o pedido não seja encontrado.
    """
    if verificar_pedido():
        pedidos.pop(codigo)
        input(">> Enter")
        return True
    else:
        error_msg("Pedido não encontrado")
        input(">> Enter")
        return False


def opcoes_edicao():
    """
    Função para ler e validar a opção de edição escolhida pelo usuário.

    A função continua solicitando uma opção de edição até que o usuário insira uma opção válida entre 1 e 5.

    Returns:
        int: A opção de edição válida escolhida pelo usuário.
    """
    while True:
        opc = leia_int("Opção de edição ")
        if opc < 1 or opc > 5:
            error_msg("Opção fora de alcance")
        else:
            return opc


def mudar_dados_cliente(detalhes):
    """
    Função para mudar os dados do cliente em um pedido.

    Args:
        detalhes (list): Lista contendo os detalhes do pedido. A estrutura esperada é:
            [
                id_pedido (int),
                cliente_nome (str),
                cliente_endereco (str),
                hamburguer (str),
                quantidade (int),
                adicionais (list): Lista de listas onde cada sublista contém [nome_adicional (str), quantidade (int), preço (float)],
                total (float)
            ]
    """
    nome = leia_nome("Nome:    ")
    rua = leia_nome("Rua: ")
    numero = leia_int("N° casa:  ")
    endereco = f"{rua}, {numero}"
    detalhes[1] = nome
    detalhes[2] = endereco


def mudar_pedido(detalhes):
    """
    Função para mudar o hambúrguer em um pedido.

    Args:
        detalhes (list): Lista contendo os detalhes do pedido. A estrutura esperada é:
            [
                id_pedido (int),
                cliente_nome (str),
                cliente_endereco (str),
                hamburguer (str),
                quantidade (int),
                adicionais (list): Lista de listas onde cada sublista contém [nome_adicional (str), quantidade (int), preço (float)],
                total (float)
            ]
    """
    nome = leia_item("Hambúrguer:   ").upper()
    quantidade = leia_int("Quantidade:  ")

    # Extrair os ingredientes
    ingredientes = extrair_ingredientes(nome, quantidade)
    if ingredientes:
        itens_insuficientes = verificar_ingredientes(ingredientes)

        if itens_insuficientes:
            error_msg("Pedido não pode ser feito. Ingredientes insuficientes.")
            for item in itens_insuficientes:
                print(item)
        else:
            detalhes[3] = nome
            detalhes[4] = quantidade
    else:
        # Error de não existência
        error_msg("Hambúrguer não catalogado!")


def mudar_adicionais(detalhes):
    """
    Função para modificar os adicionais de um pedido.

    Args:
        detalhes (list): Lista contendo os detalhes do pedido. A estrutura esperada é:
            [
                id_pedido (int),
                cliente_nome (str),
                cliente_endereco (str),
                hamburguer (str),
                quantidade (int),
                adicionais (list): Lista de listas onde cada sublista contém [nome_adicional (str), quantidade (int), preço (float)],
                total (float)
            ]
    """
    detalhes[5] = []  # Reinicializa os adicionais para atualização
    while True: # Laço para adicionar mais acrescimos
        nome_adicional = leia_item("[SAIR] Nome: ").upper()
        if nome_adicional[0] in 'Ss':
            break

        ids, checagem = check_buy(nome_adicional)

        quantidade_adicional = leia_int("Quantia: ")

        if checagem:
            if verificar_acrescimos(checagem, quantidade_adicional):
                preco = leia_float("Preço: ")
                detalhes[5].append([nome_adicional, quantidade_adicional, preco])
        else:
            error_msg("Acréscimo em falta")


def calcular_total(detalhes, nome):
    """
    Calcula o total do pedido baseado nos detalhes do pedido e no nome do hambúrguer.

    Args:
        detalhes (list): Lista contendo os detalhes do pedido. A estrutura esperada é:
            [
                id_pedido (int),
                cliente_nome (str),
                cliente_endereco (str),
                hamburguer (str),
                quantidade (int),
                adicionais (list): Lista de listas onde cada sublista contém [nome_adicional (str), quantidade (int), preço (float)],
                total (float)
            ]
        nome (str): Nome do hambúrguer para buscar o preço no cardápio.

    Returns:
        float: Total calculado do pedido, incluindo o preço do hambúrguer e dos adicionais.
    """
    preco_hamburguer = cardapio[nome]['Preço']  
    total_hamburguer = preco_hamburguer * detalhes[4]
    total_adicionais = sum([adicional[1] * adicional[2] for adicional in detalhes[5]])
    return total_hamburguer + total_adicionais


def editar_pedido(id_pedido):
    """
    Função para editar um pedido existente.

    Args:
        id_pedido (int): ID do pedido no dicionário `pedidos`.

    Descrição:
    - A função exibe e permite a edição dos detalhes de um pedido específico.
    - Os detalhes do pedido incluem: dados do cliente, pedido de hambúrguer, adicionais e total.
    - A função verifica se o pedido existe, exibe os detalhes e permite que o usuário faça edições.

    Fluxo da função:
    1. Exibe o título "Edição de pedido" e limpa a tela.
    2. Verifica se o pedido com o ID fornecido existe utilizando a função `verificar_pedido`.
    3. Se o pedido não existir, exibe uma mensagem de erro e retorna.
    4. Extrai e exibe os detalhes do pedido, incluindo nome do cliente, endereço, hambúrguer, quantidade, adicionais e total.
    5. Permite ao usuário editar:
        - Dados do cliente
        - Pedido de hambúrguer
        - Adicionais
    6. Atualiza o total do pedido após cada edição utilizando a função `calcular_total`.
    7. Exibe uma mensagem de sucesso após cada edição.
    8. Pergunta ao usuário se deseja continuar editando outras informações do pedido.

    Exemplo de uso:
        editar_pedido(1)
    """
    titulo("Edição de pedido")
    limpar_tela()
    # Encontra o pedido com o id fornecido
    if verificar_pedido(id_pedido): 
        pass
    else:
        error_msg("Pedido não existe")
        return
    
    pedido = pedidos[id_pedido]
    
    while True:
        # Extraindo os detalhes do pedido
        cliente_nome = pedido[1]
        cliente_endereco = pedido[2]
        hamburguer = pedido[3]
        hamburguer_quantidade = pedido[4]
        adicionais = pedido[5]
        total = pedido[6]

        # Exibindo os detalhes do pedido
        print_alinhado(f"\033[1m 1. Dados Cliente:\033[m", f"{cliente_nome}, {cliente_endereco}")
        print_alinhado(f"\033[1m 2. Pedido:\033[m", f"{hamburguer} (x{hamburguer_quantidade})")
        print_alinhado(f"\033[1m 3. Adicionais:\033[m", f"{', '.join([f'{adicional[0]} (x{adicional[1]})' for adicional in adicionais])}")
        print(f"{'Total:'} {'-' * 75} R$ {total:.2f}")

        opc = opcoes_edicao()
        if opc == 1:
            mudar_dados_cliente(pedido)
        elif opc == 2:
            mudar_pedido(pedido)
        elif opc == 3:
            mudar_adicionais(pedido)

        # Calcular novo preço
        pedido[6] = calcular_total(pedido, hamburguer)

        sucess_msg("Pedido atualizado com sucesso.")
        sair = input("Deseja editar outra informação? (s/n): ").lower()

        if sair != 's':
            break


def fechar_vendas():
    """
    Fecha as vendas do dia para um funcionário específico, limpa os pedidos e salva os dados no relatório de vendas.

    Parâmetros:
    - cpf (str): CPF do funcionário que está fechando as vendas.

    Estruturas de dados usadas:
    - funcionarios (dict): Dicionário contendo os dados dos funcionários. Cada chave é o CPF e o valor é um dicionário com detalhes do funcionário.
    - vendas (dict): Dicionário onde as chaves são datas e os valores são dicionários com detalhes das vendas daquele dia.
    - pedidos (dict): Dicionário contendo os pedidos realizados. Cada chave é o id_pedido e o valor é um dicionário com detalhes do pedido.

    Fluxo da função:
    1. Solicita o CPF do funcionário e define a data e hora atuais.
    2. Verifica se o funcionário existe no dicionário `funcionarios`.
    3. Se o funcionário for encontrado, cria um relatório de vendas para a data atual contendo a hora, nome do funcionário, CPF e os pedidos realizados.
    4. Limpa os pedidos realizados do dicionário `pedidos`.
    5. Salva os dados atualizados nos arquivos "arquivo_vendas.dat" e "arquivo_pedidos.dat".
    6. Atualiza o ranking de vendas com base nos pedidos realizados.
    7. Exibe uma mensagem de sucesso e aguarda o pressionamento da tecla Enter.

    Exceções:
    - KeyError: Lançada se o CPF fornecido não corresponder a nenhum funcionário no dicionário `funcionarios`.

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
    vendas[data] = {
        "Hora": hora,
        "Funcionário": funcionario_cpf["Nome"],
        "CPF": cpf,
        "Pedidos Realizados": pedidos.copy(),  
    }

    pedidos.clear() # Limpar dos pedidos

    # Salvamento de dados
    save_data("arquivo_vendas.dat", vendas) 
    save_data("arquivo_pedidos.dat", pedidos)
    atualizar_ranking(pedidos)

    sucess_msg("Vendas fechadas com sucesso!")
    input("<< Enter >>")


def atualizar_ranking(pedidos):
    """
    Atualiza o ranking de hambúrgueres mais pedidos com base nos dados fornecidos.

    Args:
        pedidos (dict): Um dicionário contendo os pedidos realizados. A estrutura do dicionário é a seguinte:
            {
                'data': {
                    'Hora': 'hh:mm:ss',
                    'Funcionário': 'nome do funcionário',
                    'CPF': 'cpf do cliente',
                    'Pedidos Realizados': {
                        'codigo do pedido': [
                            1, # Número do pedido
                            'nome do cliente',
                            'endereço de entrega',
                            'nome do hambúrguer',
                            quantidade_pedida,
                            [lista de adicionais],
                            valor_total
                        ]
                    }
                }
            }
    
    Exemplo de uso:
        pedidos = {
            '23/06/2024': {
                'Hora': '10:24:47',
                'Funcionário': 'Anderson Gabriel Pereira Cruz',
                'CPF': '77788899911',
                'Pedidos Realizados': {
                    1: [1, 'Anderson Gabriel', 'Centro, 157', 'HAMBÚRGUER CLÁSSICO', 1, [['COCA-COLA', 1, 4.0]], 10.0]
                }
            }
        }
        ranking_vendas = {}
        atualizar_ranking(pedidos)
        print(ranking_vendas)  # Saída: {'HAMBÚRGUER CLÁSSICO': 1}
    """
    for data, valores in pedidos.items():
        for codigo, detalhes in valores['Pedidos Realizados'].items():
            hambuguer = detalhes[3]
            quantidade = detalhes[4]
            if hambuguer in ranking_vendas:
                ranking_vendas[hambuguer] += quantidade
            else:
                ranking_vendas[hambuguer] = quantidade
    save_data("ranking_vendas.dat", ranking_vendas)
