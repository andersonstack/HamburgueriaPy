# Importações necessárias para o pacote.
from dados_pct import DATA, HORA, adicionais_dict, almoxarifado, compras, save_data
from estilização_pct import error_msg, sucess_msg, titulo, print_alinhado, linha
from ferramentas_pct import (
    check_buy,
    leia_float,
    leia_int,
    leia_item,
    limpar_tela,
    input_tratado,
)

# Define o próximo ID a ser usado.
ID_COMPRAS = 1 if len(almoxarifado) == 0 else max(almoxarifado.keys()) + 1  


def atualizar_compras(id_item, quantidade):
    """
    Atualiza a quantidade de itens existentes no almoxarifado.

    Args:
        id_item (int): Chave no dicionário almoxarifado que armazena os detalhes do 
        item.
        quantidade (int): Quantidade a ser adicionada ao item existente no 
        almoxarifado[id_item].
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
    global ID_COMPRAS
    limpar_tela()
    titulo("Cadastramento de Mercadorias")

    nome = leia_item(" - Nome:").upper().strip()
    quantidade = leia_int("- Quantidade:")
    preco = leia_float("- Preço:")

    linha()
    adicional = input_tratado("Deseja adiciona-lo em adicionais? (Sim / Não)")
    linha()
    if adicional == "SIM":
        lista_adicionais(nome)

    id_item, detalhes = check_buy(nome)  # Retornar os itens.
    
    if detalhes:  # Se existir
        atualizar_compras(id_item, quantidade)
    else:
        almoxarifado[ID_COMPRAS] = [nome, quantidade]
        ID_COMPRAS += 1  # Incrementa o contador de ID.

    # Processar as compras para o relatório.
    processamento_relatorio(nome, quantidade, preco)  
    save_data("arquivo_almoxarifado.dat", almoxarifado)  # Salvar os arquivos.
    sucess_msg("Mercadorias cadastradas")

    return input(">> Enter")


def lista_adicionais(nome):
    if nome not in adicionais_dict.values():
        adicionais_dict[ID_COMPRAS] = nome
        save_data("arquivo_adicionais.dat", adicionais_dict)
    else:
        error_msg("Adicional já existe.")
        print()
        input(">> Enter")
    return 


def deletar_adicional():
    exibir_adicionais()
    codigo = leia_int("(0) Código do adicional:")
    if codigo == 0:
        return
    
    if codigo in adicionais_dict:
        adicionais_dict.pop(codigo)
        save_data("arquivo_adicionais.dat", adicionais_dict)
    else:
        error_msg("Código não encontrado!")
        print()
        input(">> Enter")
    return


def exibir_adicionais():
    limpar_tela()
    titulo("Lista de adicionais")
    linha()
    for codigo, item  in adicionais_dict.items():
        print_alinhado(f"Código: {codigo} ", f"Nome: {item}")
    linha()


def excluir_item(id_item):
    """
    Exclui um item do almoxarifado.

    Args:
        id_item (int): Chave no dicionário almoxarifado que armazena os detalhes do 
        item.
    """
    if id_item in almoxarifado:
        del almoxarifado[id_item]
        save_data("arquivo_almoxarifado.dat", almoxarifado)  # Atualiza o arquivo.
        sucess_msg("Item excluído com sucesso")
    else:
        error_msg("ID não encontrado")


def processamento_relatorio(nome, quantidade, preco):
    """
    Função cadastrar no relatorio.

    O processo pegar como argumentos os parâmetros vindo de cadastrar_compras,
    nome, quantidade, preco. A partir de deles, os dados são colocados em um dicionários
    e adicionados em compras.
    """
    entrada_relatorio = {
        "hora": HORA,
        "nome": nome, 
        "quantidade": quantidade,
        "preço": preco
    }
    
    if DATA not in compras:
        compras[DATA] = []  # Criação de nova data caso não exista.

    compras[DATA].append(entrada_relatorio)  # Adicionando arquivos em compras.
    save_data("arquivo_relatorio_compras.dat", compras)  # Salvando as compras.
    