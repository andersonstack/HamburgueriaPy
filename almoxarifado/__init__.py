from data import *
from views import *
from tools import *

def buscar_item():
    """
    Função para buscar itens no almoxarifado.
    
    O usuário pode buscar um item pelo seu nome ou pelo seu ID. A função exibe os 
    detalhes do item se ele for encontrado no almoxarifado.
    
    Exceções:
        - A função não lida explicitamente com exceções; entradas inválidas devem ser tratadas
          pelas funções auxiliares.
    
    Entradas:
        - O usuário é solicitado a inserir o nome ou ID do item.
    
    Saídas:
        - Exibição dos detalhes do item se ele for encontrado no almoxarifado.
        - Se o item não for encontrado, nenhuma saída específica é definida.
    """
    item = input_tratado("Item ou ID:   ")

    limpar_tela()
    # Verifica se o prompt é o ID
    if item.isnumeric():
        id_num = int(item) # Converte o id em int
        item_details = check_id(id_num)
        if item_details: # Verificação se existe no almoxarifado
            exibir_item(item_details, item) # Exibir dados do item 
    
    # Verifica se é nome
    else:
        id_item, item_details = check_buy(item) # Checa a existência, retorna uma lista
        if item_details:
             exibir_item(item_details, id_item)

    input(">> Enter")       


def excluir_item():
    """
    Função para excluir um item do almoxarifado.
    
    O usuário deve fornecer o ID do item a ser excluído. A função verifica se o item
    existe no almoxarifado, exibe seus detalhes e solicita confirmação antes de 
    removê-lo. Se confirmado, o item é removido do almoxarifado e os dados são salvos.

    Exceções:
        - A função não lida explicitamente com exceções; entradas inválidas devem ser tratadas
          pelas funções auxiliares.

    Entradas:
        - O usuário é solicitado a inserir o ID do item a ser excluído.
        - O usuário deve confirmar a exclusão do item.

    Saídas:
        - Exibição dos detalhes do item a ser excluído.
        - Mensagem de sucesso se o item for removido.
        - Mensagem de operação cancelada se a exclusão não for confirmada.
    """
    item = leia_int("ID: ")
    details = check_id(item)

    if details:
        error_msg(f"Item a ser excluido: {details[0]}")
        confirmar = input("Confirmação[S/N] ")
        if confirmar in 'Ss':
            almoxarifado.pop(item)
            save_data("arquivo_almoxarifado.dat", almoxarifado)
            sucess_msg("Item removido!")
        else:
            error_msg("Operação cancelada")
            
    input(">> Enter")
