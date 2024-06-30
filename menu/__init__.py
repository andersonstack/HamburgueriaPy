from tools import *
from data import *
from views import *

def exibir_cardapio():
    """
    Exibe o cardápio da hamburgueria, mostrando os hambúrgueres disponíveis e seus ingredientes.
    """
    limpar_tela()
    for nome_hamburguer, ingrediente_hamburguer in cardapio.items():
        print()
        subtitulo(nome_hamburguer) # Nome do hambúrguer 
        print('\033[1;37m')
        for ingrediente, quantidade in ingrediente_hamburguer.items():
            
            if ingrediente == 'Preço':
                print(f"{ingrediente} {'-' * (116 - (len(ingrediente)))} R$ {quantidade:.2f}")
            else:
                print(f"{ingrediente} {'-' * (122 - (len(ingrediente)))} {quantidade}")
    print()
    print('\033[m') 
    input(">> Enter")


def verificar_hamburguer_existente():
    """
    Verifica se o hambúrguer já existe no cardápio.

    Solicita o nome do hambúrguer e verifica se o nome existe no cardápio. Caso exista, retorna o hamburguer
    para continuar o processo.
    Caso não exista, retorna um mensagem de erro.
    
    Returns:
        hamburguer: nome do hambúrguer no cardápio
        error_msg: mensagem de que o hamburuger não foi encontrado.
    
    Fluxo:
        1. Solicita o nome do hamburguer.
        2. Verifica se o hamburguer existe no cardápio.
            2.1 Se existe, retorna o próprio hamburguer.
            2.2 Se não existe, retorna um error_msg.

    Formato do cardápio:
        cardapio = {
            'HAMBURGUER': {
                'INGREDIENTE 1': quantidade
                ...
                'INGREDIENTE n': quantidade
                'Preço': 6.0
            }
        }
    """
    hamburguer = leia_item("Nome:   ").upper()

    for nome, _ in cardapio.items(): # Verificação
        if hamburguer.replace(" ", "") in nome.replace(" ", ""): # Comparação da entrada do hambúrguer com o nome do cardápio
            return hamburguer
    return error_msg("Hambúrguer não existe no cardápio")


def atualizar_hamburguer(hamburguer):
    """
    Atualiza um hambúrguer existente no cardápio.

    Args:
        hamburguer (str): O nome do hambúrguer a ser atualizado.

    Fluxo:
        1. Recebe como parâmetro o nome do hambúrguer a ser atualizado.
        2. Intera sobre os elementos do cardápio.
        3. Compara o hambúrguer com os hambúrguer do cardápio.
        4. Intera sobre os ingredientes desse hambúrguer.
        5. Faz um laço de repetição para atualizar os ingredientes.
        6. Solicita o novo preço.
        7. Atualiza os dados do novo hambúrguer.
        8. Exibe mensagem de sucesso.
        9. Salva os novos dados em arquivo.
    
    Formato do cardápio:
        cardapio = {
            'HAMBURGUER': {
                'INGREDIENTE 1': quantidade
                ...
                'INGREDIENTE n': quantidade
                'Preço': 6.0
            }
        }
    """
    
    limpar_tela()
    for nome, ingredientes in cardapio.items(): # Intera sobre os itens do cardápio
        if hamburguer.replace(" ", "") in nome.replace(" ", ""): # Comparação
            print(f"Atualizando o hambúrguer '{nome}':") # Hambúrguer escolhido para ser atualizado
            print("Ingredientes Atuais:")
            for ingrediente, quantidade in ingredientes.items(): # Intera sobre os itens desse hambúrguer
                print(f"{ingrediente}: {quantidade}")

            while True: # Laço para atualizar/add novos ingredientes
                ingrediente = leia_item("[SAIR] Ingrediente:    ")
                if ingrediente == "SAIR": # Quebra de laço
                    break

                quantidade = leia_int("Quantidade:   ")
                cardapio[nome][ingrediente] = quantidade
            
            preco = leia_float("Preço:   ")
            cardapio[nome]["Preço"] = preco

            sucess_msg(f"Hambúrguer '{nome}' atualizado com sucesso!") # Mensagem de retorno
            save_data("arquivo_cardapio.dat", cardapio)
    
    input(">> Enter")


def criar_novo_hamburguer(hamburguer):
    """
    Cria um novo hambúrguer no cardápio.

    Args:
        hamburguer (str): O nome do hambúrguer a ser atualizado.

    Fluxo:
        1. Cria um novo hambúrguer no cardápio.
        2. Exibe uma mensagem de que um Hambúrguer foi criado e para inserir os dados..
        3. Faz um laço de repetição para adicionar os ingredientes.
        4. Solicita o preço do hambúrguer.
        5. Insere os dados no cardápio.
        6. Exibe mensagem de sucesso.
        7. Salva os dados em arquivo.
        8. Solicita que o usuário dê input para continuar.
    
    Formato do cardápio:
        cardapio = {
            'HAMBURGUER': {
                'INGREDIENTE 1': quantidade
                ...
                'INGREDIENTE n': quantidade
                'Preço': 6.0
            }
        }
    """
    limpar_tela()
    cardapio[hamburguer] = {}  # Cria um novo hambúrguer no cardápio
    titulo("HAMBÚRGUERES")
    sucess_msg(f"Hambúrguer '{hamburguer}' criado. Por favor, adicione os ingredientes e preço:")

    while True:
        ingrediente = leia_item("[SAIR] Ingrediente:    ").upper()
        if ingrediente == "SAIR":
            break

        quantidade = leia_int("Quantidade:   ")
        cardapio[hamburguer][ingrediente] = quantidade
            
    preco = leia_float("Preço:   ")
    cardapio[hamburguer]["Preço"] = preco

    sucess_msg(f"Hambúrguer '{hamburguer}' criado com sucesso!")
    save_data("arquivo_cardapio.dat", cardapio)
    input(">> Enter")


def excluir_hamburguer():
    """
    Exclui um hambúrguer específico do cardápio.

    Fluxo:
        1. Solicita o nome do hambúrguer a ser excluido.
        2. Define ham_excluido como False.
        3. Intera os elementos do cardapio.
        4. Verifica se o hamburguer existe no cardapio.
            4.1 Se existe exibe mensagem que foi encontrado.
                4.1.1 Pede confirmação de exclusão.
                4.1.2 Se confirmação for confirmativa, deleta o hamburguer e hamb_excluido = True.
                Salva os dados no cardápio e sai do for.
                4.1.3 Se confirmação for negativa, cancela a operação e sai for for e define
                hamb_excluido = True para evitar mensagem de hambúrguer não encontrado.
            4.2 Se não existe, exibe mensagem de erro que hambúrguer não encontrado.
        5. Pede input() para prosseguir o código.
            
    Formato do cardápio:
        cardapio = {
            'HAMBURGUER': {
                'INGREDIENTE 1': quantidade
                ...
                'INGREDIENTE n': quantidade
                'Preço': 6.0
            }
        }

    """
    hamburguer = leia_item("Nome:   ")
    limpar_tela()
    hamb_excluido = False  # Variável para verificar se o hambúrguer foi excluído

    for nome in cardapio.keys(): # Verificação de o hambúrguer está no cardápio
        if hamburguer.replace(" ", "") in nome.replace(" ", ""):
            sucess_msg("Hambúrguer encontrado")
            confirmar_exclusao = input_tratado(f"Deseja realmente excluir o hambúrguer '{nome}' do cardápio? [S/N]: ")
            
            if confirmar_exclusao == "S":
                del cardapio[nome]
                sucess_msg(f"Hambúrguer '{nome}' excluído do cardápio com sucesso!")
                hamb_excluido = True

                save_data("arquivo_cardapio.dat", cardapio)

                break
            else:
                error_msg("Exclusão cancelada.")
                hamb_excluido = True  # Define como True para evitar a mensagem de hambúrguer não encontrado
                break

    if not hamb_excluido: # Caso o hambúrguer não seja encontrado, o hamb_excluido terá valor booleano False
        error_msg(f"Hambúrguer '{hamburguer}' não encontrado no cardápio.")

    input(">> Enter")
