from data import *
from views import *

def exibir_percas():
    limpar_tela()
    data_percas = input_tratado("Data [XX/XX/XXXX] | Todo [Relatorio completo]:  ")

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


