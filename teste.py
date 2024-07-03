from data import *
from views import *

def atualizar_hamburguer(hamburguer, cardapio):
    """
    Atualiza um hambúrguer existente no cardápio, zerando a lista de ingredientes.

    Args:
        hamburguer (str): O nome do hambúrguer a ser atualizado.
        cardapio (dict): Dicionário contendo o cardápio de hambúrgueres.

    Fluxo:
        1. Recebe como parâmetro o nome do hambúrguer a ser atualizado.
        2. Intera sobre os elementos do cardápio.
        3. Compara o hambúrguer com os hambúrguer do cardápio.
        4. Zera a lista de ingredientes do hambúrguer.
        5. Faz um laço de repetição para adicionar novos ingredientes.
        6. Solicita o novo preço por último.
        7. Atualiza os dados do novo hambúrguer.
        8. Exibe mensagem de sucesso.
        9. Salva os novos dados em arquivo.
    
    Formato do cardápio:
        cardapio = {
            'HAMBURGUER': {
                'INGREDIENTE 1': quantidade,
                ...
                'INGREDIENTE n': quantidade,
                'Preço': 6.0
            }
        }
    """
    
    for nome, ingredientes in cardapio.items():
        if hamburguer.replace(" ", "").upper() == nome.replace(" ", "").upper():
            print(f"Atualizando o hambúrguer '{nome}':")
            cardapio[nome] = {}  # Zera a lista de ingredientes
            
            while True:
                ingrediente = input("(SAIR) Ingrediente: ").strip().upper()
                if ingrediente == "SAIR":
                    break

                quantidade = int(input("Quantidade: "))
                cardapio[nome][ingrediente] = quantidade
            
            preco = float(input("Preço: "))
            cardapio[nome]["Preço"] = preco  # Adiciona o preço por último

            print(f"Hambúrguer '{nome}' atualizado com sucesso!")
            save_data("arquivo_cardapio.dat", cardapio)
            break
    else:
        print(f"Hambúrguer '{hamburguer}' não encontrado no cardápio.")

print(cardapio)
input()
atualizar_hamburguer("X-TUDO", cardapio)
print(cardapio)