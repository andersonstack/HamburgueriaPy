# Importações necessárias para o pacote.
import pickle as save
from datetime import datetime

DATA = datetime.now().strftime("%d/%m/%Y") # Define data
HORA = datetime.now().strftime("%H:%M:%S") # Define hora

def load_data(filename, default_value):
    """
    Função para carregar dados de um arquivo. Se o arquivo não existir ou estiver vazio,
    retorna um valor padrão e cria o arquivo com esse valor.

    Args:
        filename (str): Nome do arquivo de onde os dados serão carregados.
        default_value (dict): Dicionário com os dados padrão a serem usados se o 
        arquivo não existir ou estiver vazio.

    Returns:
        dict: Dicionário com os dados carregados do arquivo ou o valor padrão.
    """
    try:
        with open(filename, "rb") as file:
            return save.load(file)
    except FileNotFoundError:
        with open(filename, "wb") as file:
            save.dump(default_value, file)
        return default_value
    except EOFError:
        return default_value
    
def save_data(filename, data):
    with open(filename, "wb") as file:
        save.dump(data, file)

# Inicialização dos dicionários carregando os dados dos arquivos 
almoxarifado = load_data("arquivo_almoxarifado.dat", {})
compras = load_data("arquivo_relatorio_compras.dat", {})
clientes = load_data("arquivo_clientes.dat", {})
vendas = load_data("arquivo_vendas.dat", {})
pedidos = load_data("arquivo_pedidos.dat", {})
funcionarios = load_data("arquivo_funcionarios.dat", {})
cardapio = load_data("arquivo_cardapio.dat", {})
ranking_vendas = load_data("ranking_vendas.dat", {})
percas_ingredientes = load_data("percas_ingredientes.dat", {})


# Ex.: save_data("arquivo_almoxarifado.dat", almoxarifado)
