from data import *
from views import *
from tools import *

def processo_compras():
    """
    Função para exibir detalhes de compras com base em uma data específica ou todas as compras.

    Permite ao usuário selecionar uma data específica ou exibir um relatório completo de compras.
    Se a data especificada não existir no dicionário de compras, exibe uma mensagem de erro.
    Para cada data ou todas as compras exibidas, mostra detalhes como hora, nome do item,
    quantidade e preço unitário.

    Retorna: None
    """
    data_compra = input_tratado("Data [XX/XX/XXXX] | Todo [Relatorio completo]:  ")
    limpar_tela()

    if data_compra.strip() != 'TODO':
        if data_compra not in compras.keys():
          error_msg("Data não encontrada")
          return input("<< Enter >>")

        else:
          data = {data_compra: compras[data_compra]}
    else:
        data = compras

    for data, compra in data.items():
        print_alinhado("\033[1mDATA:",f"{data}\033[m")
        print("=" * 50)
        for detalhes in compra:
            print_alinhado("Hora:",detalhes['hora'])
            print_alinhado("Nome:", detalhes['nome'])
            print_alinhado("Quantidade:", f"{detalhes['quantidade']} unidades")
            print_alinhado("Preço",f"R$ {detalhes['preço']}")
            print("=" * 50)
    linha()
    input(">> Enter para continuar")


def processos_vendas():
    """
    Função para exibir relatório de vendas com base em uma data específica ou todas as vendas.

    Permite ao usuário selecionar uma data específica ou exibir um relatório completo de vendas.
    Se a data especificada não existir no dicionário de vendas, exibe uma mensagem de erro.
    Para cada data ou todas as vendas exibidas, mostra detalhes como pedidos realizados, 
    informações adicionais (se houver), e informações dos funcionários envolvidos.

    Retorna: None
    """

    limpar_tela()
    data_venda = input_tratado("Data [XX/XX/XXXX] | Todo [Relatorio completo]:  ")
    limpar_tela()

    if data_venda.strip().upper() != 'TODO':
        if data_venda not in vendas.keys():
            error_msg("Data não encontrada")
            input(">> Enter para continuar")
            return
        
        else:
            data = {data_venda: vendas[data_venda]}
    else:
        data = vendas
     
    for data, detalhes in data.items():
        subtitulo(data)
        print(f"Hora: {detalhes['Hora']}")
        print(f"Funcionário: {detalhes['Funcionário']}")
        print(f"CPF: {detalhes['CPF']}")
        linha()
        
        pedidos = detalhes['Pedidos Realizados']
        for pedido_id, pedido_detalhes in pedidos.items():
            print(f"\nPedido ID: {pedido_id}")
            print(f"Cliente: {pedido_detalhes[1]}")
            print(f"Endereço: {pedido_detalhes[2]}")
            print(f"Produto: {pedido_detalhes[3]}")
            print(f"Quantidade: {pedido_detalhes[4]}")

            if pedido_detalhes[5]:  # Verifica se há adicionais
                print("Adicionais:")
                for adicional in pedido_detalhes[5]:
                    print(f"  - Item: {adicional[0]}, Quantidade: {adicional[1]}, Preço: {adicional[2]}")
            else:
                print("Adicionais: Nenhum")

            print(f"Preço: R$ {pedido_detalhes[6]:0.2f}")
            linha()

    input(">> Enter para continuar")


def ordenar_vendas(dict):
    """
    Ordena um dicionário de vendas com base nos valores em ordem decrescente.

    Args:
        dict (dict): Dicionário contendo as vendas a serem ordenadas.

    Returns:
        dict: Dicionário ordenado com as vendas, onde as chaves são mantidas intactas.
    """
    sorted_items = sorted(dict.items(), key=lambda item: item[1], reverse=True)

    dict_ordenado = {}
    for keys, values in sorted_items:
        dict_ordenado[keys] = values

    return dict_ordenado


def imprimir_ranking():
    """
    Imprime o ranking de vendas ordenado por quantidade de forma formatada.

    Utiliza a função ordenar_vendas para obter um dicionário ordenado de vendas e imprime
    os resultados formatados em uma tabela.

    Retorna: None
    """
    limpar_tela()
    dict = ordenar_vendas(ranking_vendas)
    cabecalho("Ranking de Vendas")
    print(f"{'QUANTIDADE':^62}|{'HAMBÚRGUER':^62}")
    linha()
    for values, keys in dict.items():
        print(f"{keys:^62}{values:^62}")
        print("¨" * 125)
    
    input(">> Enter")

def exibir_percas():
    """
    Função que exibe as percas de determinado turno ou período completo de vendas.

    Returns:
        input: Solicita que o usuário aperte enter para continuar o processo.
    """
    limpar_tela()
    data_percas = input_tratado("Data [XX/XX/XXXX] | Todo [Relatorio completo]:  ")
    limpar_tela()


    if data_percas.strip() != 'TODO':
        if data_percas not in percas_ingredientes.keys():
            error_msg("Data não encontrada")
            return input(">> Enter")
        else:
            data = {data_percas: percas_ingredientes[data_percas]}
    else:
        data = percas_ingredientes

    for data, infor in data.items():
        cabecalho("RELATÓRIO DE PERCAS")
        subtitulo(f"Data: {data}")
        for item, quantidade in infor.items():
           print_alinhado(f"{item}{'-' * (124 - (len(item)))}{quantidade}")
    linha()
    return input(">> Enter")
