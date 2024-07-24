from dados_pct import *
from estilização_pct import *
ID_COMPRAS = 7

def verificar_adicionais(adicional, quantidade):
    """
    Função que verifica se os adicionais no almoxarifado existeme  são suficientes.

    Args:
        adicional (str): Nome do item.
        quantidade (int): Quantidade solicitada.

    Returns:
        booleano: True para possível adicionar adicional; False para o contrário.
    """
    # Verifica se o adicional está disponível.
    exitir, nome = verificar_lista_adicionais(adicional)
    if exitir:  
        # Faz um novo dict com os itens do almoxarifado.
        itens_dict = {itens[0]: itens[1] for itens in almoxarifado.values()}

        # Compara se o nome existe e se sua quantidade é suficiente.
        if nome not in itens_dict or quantidade > itens_dict[nome]:
            return False
        return True
    else:
        error_msg("Adicional não disponível!")
        input(">> Enter")
        return False


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


print(verificar_adicionais("7", 1))
