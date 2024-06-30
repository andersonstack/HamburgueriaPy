from views import *
from data import *
from tools import *

def atualizar_compras(id_item, quantidade):
    """
    Atualiza a quantidade de itens existentes no almoxarifado.

    Args:
        id_item (int): Chave no dicionário almoxarifado que armazena os detalhes do item.
        quantidade (int): Quantidade a ser adicionada ao item existente no almoxarifado[id_item].
    
    Formato geral:
        almoxarifado = {
            id_item: ['ITEM', quantidade]
        }
    
    Exemplo:
        almoxarifado = {
            1: ['PÃO', 50]
        }
        # Para adicionar 20 unidades de PÃO
        atualizar_compras(1, 20)
        # Novo valor no almoxarifado[1] será ['PÃO', 70]
    """
    almoxarifado[id_item][1] += quantidade


def cadastrar_compras():
    """
    Função para cadastrar novos itens.

    A função verifica primeira a existência do item no almoxarifado,
    caso exista, ele atualizará a quantidade, e se não existir, ele criará 
    um novo item. Após atualização ou criação do item, ela processa as 
    informações para o relatório, salva os dados e atualiza e exibe uma mensagem
    de sucesso.

    Detalhes:
        O ID do novo item é definido com o tamanho do dicionário almoxarifado,
        incremetado de 1, Caso o item exista, a quantidade é atualizada.
    
    Fluxo:
        1. Solicita entrada de nome, quantidade, preco.
        2. Define o ID por tamanho do almoxarifado incrementando em 1.
        3. Verifica, a partir do nome, a existência do item no almoxarifado.
            3.1 Se existe:
                - Retorna o ID no almoxarifado e a lista de detalhes ['ITEM', 50].
                - Usa o ID_almoxarifado e os detalhes como parâmetro para atualizar o item.
            3.2 Se não existe:
                - Cria um novo item no almoxarifado.
                - almoxarifado[ID] = ['ITEM', 50] 
                # ID aqui é definido pelo tamanho do almoxarifado.
        4. Usa os parâmetros nome, quantidade e preco para atualizar o relatório de compras.
        5. Salva os dados no arquivo.
        6. Exibe mensagem de sucesso.
        7. Retorna um input.
    """
    limpar_tela()
    titulo("Cadastramento de Mercadorias")

    nome = leia_item(" - Nome: \n ").upper().strip()
    quantidade = leia_int("- Quantidade: \n ")
    preco = leia_float("- Preço: \n R$ ")

    ids = len(almoxarifado) + 1 # Definição do ID
    id_item, detalhes = check_buy(nome) # Retornar os itens
    
    if detalhes: # Se existir
        atualizar_compras(id_item, quantidade)
    else:
        almoxarifado[ids] = [nome, quantidade]
    
    processamento_relatorio(nome, quantidade, preco) # Processar as compras para o relatório
    save_data("arquivo_almoxarifado.dat", almoxarifado) # Salvar os arquivos
    sucess_msg("Mercadorias cadastradas")

    return input(">> Enter")

def processamento_relatorio(nome, quantidade, preco):
    """
    Função cadastrar no relatorio.

    O processo pegar como argumentos os parâmetros vindo de cadastrar_compras,
    nome, quantidade, preco. A partir de deles, os dados são colocados em um dicionários
    e adicionados em compras.

    Args:
        nome (str): Nome do item.
        quantidade (int): Quantidade do item.
        preco (float): Preço do item.
    
    Fluxo: 
        1. Recebe os parâmetros.
        2. Define o dicionário da entrada do relatório.
        3. Verifica a data das compras.
        4. Caso data não exista, é criado uma lista com a data correspondente. 
        5. O dicionário de compras recebe o dicionário.
        6. Os arquivos são salvos.
    
    Exemplo:
        # A função recebe PÃO, 50, 100.00
        entrada_relatorio = {
            "hora": "19:45",
            "nome": PÃO,
            "quantidade": 50,
            "preco": 100.00
        }

        data = 30/06/2024
        compras[data].append(entrada_relatorio)

        compras = {
            "30/06/2024": [{
                "hora": "19:45",
                "nome": PÃO,
                "quantidade": 50,
                "preco": 100.00
            }]
        }          
    """

    # Dicionário que será adicionado em compras 
    entrada_relatorio = {
        "hora": hora,
        "nome": nome, 
        "quantidade": quantidade,
        "preço": preco
    }
    
    if data not in compras:
        compras[data] = [] # Criação de nova data caso não existe

    compras[data].append(entrada_relatorio) # Adicionando arquivos em compras
    save_data("arquivo_relatorio_compras.dat", compras) # Salvando as compras