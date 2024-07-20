from tools import *
from views import *


cardapio = {
    1: {
        'HAMBÚRGUER CLÁSSICO': {
            'CARNE BOVINA': 1,
            'OVO': 1,
            'PÃO': 2,
            'TOMATE': 1
        },
        'PRECO': 6.99
    }
}

almoxarifado = {
    1: ['CARNE BOVINA', 100],
    2: ['OVO', 100],
    3: ['PÃO', 100],
    4: ['TOMATE', 100]
}

def criar_pedido():
    hamburguer = input_tratado("Nome ou ID do Hambúrguer: ")
    quantidade = leia_int("Quantidade:  ")
    burguer = verifica_entrada(hamburguer)
    validar_burguer = validar_hamburguer(burguer)

    if validar_burguer:
        hamburguer_menu = pegar_ingredientes(burguer, quantidade)
        pedido_hamburguer, ingredientes = verficiar_ingredientes(hamburguer_menu)

        if pedido_hamburguer:
            adicionais_pedido = adicionais()
            if adicionais_pedido:
                for adicional, (qtd, preco) in adicionais_pedido.items():
                    if not verificar_adicional(adicional, qtd):
                        return print(f"Adicional {adicional} em falta para a quantidade solicitada.")
            print("Pedido realizado com sucesso!")
        else:
            print(f"Ingredientes em falta: {ingredientes}")

    else:
        return print("Hambúrguer não cadastrado.")


def adicionais():
    adicional = input_tratado("Adicionais (SIM/NÃO):  ")
    adicionais_pedido = {}

    if adicional == 'SIM':
        while True:
            adicional = leia_item("(SAIR) - Adicional:   ").upper().strip()
            if adicional == "SAIR":
                break
            quantidade = leia_int("Quantidade:  ")
            preco = leia_float("Preço p/unidade:    ")
            preco_real = preco * quantidade
            adicionais_pedido[adicional] = [quantidade, preco_real]
        return adicionais_pedido
    
    else:
        return False   


def verifica_entrada(prompt):
    try:
        hamburguer_cod = int(prompt)
        return hamburguer_cod
    
    except ValueError:
        return prompt


def validar_hamburguer(prompt):
    if isinstance(prompt, int):
        return prompt in cardapio
    else:
        for codigo, detalhes in cardapio.items():
            hamburguer_menu = list(detalhes)[0]
            if prompt.replace(" ", "") == hamburguer_menu.replace(" ", ""):
                return True
    return False


def pegar_ingredientes(pedido, quantidade):
    ingredientes_reais = {}
    ingredientes_menu = {}
    if isinstance(pedido, int):
        ingredientes = list(cardapio[pedido].values())[0]
        ingredientes_menu = ingredientes
    else:
        for codigo, detalhes in cardapio.items():
            hamburguer_menu = list(detalhes)[0]
            if pedido.replace(" ", "") == hamburguer_menu.replace(" ", ""):
                ingredientes = list(detalhes.values())[0]
                ingredientes_menu = ingredientes
                break

    for nome, quantia in ingredientes_menu.items():
        ingredientes_reais[nome] = quantia * quantidade

    return ingredientes_reais
            

def verficiar_ingredientes(dicionario):
    itens_falta = []

    for ingrediente, quantidade in dicionario.items():
        for itens in almoxarifado.values():
            item_almoxarifado = itens[0]
            item_quantidade = itens[1]
            
            if ingrediente == item_almoxarifado:
                if quantidade > item_quantidade:
                    itens_falta.append([item_almoxarifado, item_quantidade])
    
    if len(itens_falta) == 0:
        return True, itens_falta
    else:
        return False, itens_falta


def verificar_adicional(adicional, quantidade):
    for itens in almoxarifado.values():
        item_almoxarifado = itens[0]
        item_quantidade = itens[1]
        if adicional == item_almoxarifado:
            if quantidade > item_quantidade:
                return False
    
    return True


criar_pedido()



