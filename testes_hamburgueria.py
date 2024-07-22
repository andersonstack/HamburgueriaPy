from dados_pct import vendas
from estilização_pct import *
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
            print(f"Cliente: {pedido_detalhes['nome']}")
            print(f"Endereço: {pedido_detalhes['endereco']}")
            print(f"Produto: {pedido_detalhes['hamburguer']}")
            print(f"Quantidade: {pedido_detalhes['quantidade']}")

            if pedido_detalhes['adicionais']:  # Verifica se há adicionais
                print("Adicionais:")
                for adicional, info in pedido_detalhes['adicionais'].items():
                    print(f"  - Item: {adicional}, Quantidade: {info[0]}, Preço: {info[1]}")
            else:
                print("Adicionais: Nenhum")

            print(f"Preço: R$ {pedido_detalhes['preco']:0.2f}")
            linha()

    input(">> Enter para continuar")


print(pedidos)