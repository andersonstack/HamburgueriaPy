from views import *
from data import *
from tools import *
id_counter = 0 if len(almoxarifado) == 0 else max(almoxarifado.keys()) + 1  # Define o próximo ID a ser usado


def atualizar_compras(id_item, quantidade):
    """
    Atualiza a quantidade de itens existentes no almoxarifado.

    Args:
        id_item (int): Chave no dicionário almoxarifado que armazena os detalhes do item.
        quantidade (int): Quantidade a ser adicionada ao item existente no almoxarifado[id_item].
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
    """
    global id_counter
    limpar_tela()
    titulo("Cadastramento de Mercadorias")

    nome = leia_item(" - Nome: \n ").upper().strip()
    quantidade = leia_int("- Quantidade: \n ")
    preco = leia_float("- Preço: \n R$ ")

    id_item, detalhes = check_buy(nome)  # Retornar os itens
    
    if detalhes:  # Se existir
        atualizar_compras(id_item, quantidade)
    else:
        almoxarifado[id_counter] = [nome, quantidade]
        id_counter += 1  # Incrementa o contador de ID
    
    processamento_relatorio(nome, quantidade, preco)  # Processar as compras para o relatório
    save_data("arquivo_almoxarifado.dat", almoxarifado)  # Salvar os arquivos
    sucess_msg("Mercadorias cadastradas")

    return input(">> Enter")

def excluir_item(id_item):
    """
    Exclui um item do almoxarifado.

    Args:
        id_item (int): Chave no dicionário almoxarifado que armazena os detalhes do item.
    """
    if id_item in almoxarifado:
        del almoxarifado[id_item]
        save_data("arquivo_almoxarifado.dat", almoxarifado)  # Atualiza o arquivo
        sucess_msg("Item excluído com sucesso")
    else:
        print("ID não encontrado")

def processamento_relatorio(nome, quantidade, preco):
    """
    Função cadastrar no relatorio.

    O processo pegar como argumentos os parâmetros vindo de cadastrar_compras,
    nome, quantidade, preco. A partir de deles, os dados são colocados em um dicionários
    e adicionados em compras.
    """
    entrada_relatorio = {
        "hora": hora,
        "nome": nome, 
        "quantidade": quantidade,
        "preço": preco
    }
    
    if data not in compras:
        compras[data] = []  # Criação de nova data caso não exista

    compras[data].append(entrada_relatorio)  # Adicionando arquivos em compras
    save_data("arquivo_relatorio_compras.dat", compras)  # Salvando as compras