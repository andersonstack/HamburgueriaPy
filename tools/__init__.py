from os import system, name
from data import *
from views import *
def error_msg(text):
    print()
    print("\033[1;31;7m >> " + text + "\033[m")
    print()

def check_id(prompt):
    """
    Função para verificar as chaves em um dicionario.

    Args:
        prompt (key): ID do item no almoxarifado.

    Returns:
        lista: detalhe do item encontrado.
        booleano: False se o item não existe
    
    Formato do almoxarifado:
        almoxarifado = {
            1: ['ITEM', 50]
        }
        # Lista retorna o value da chave, ['ITEM', 50]
    """
    if prompt in almoxarifado: 
        return almoxarifado[prompt]
    else:
        error_msg("ID não encontrado no almoxarifado. Item não cadastrado.")
        return False


def check_buy(nome):
    """
    Função para verificar o nome de um item dentro de uma chave.

    Args:
        nome (str): Nome do item a ser buscado

    Returns:
        tupla: retorna a linha correspondende.
        None: se não houve, não retorna nada.

    Formato do Almoxarifado:
        almoxarifado = {
            1 = ['ITEM', 50]
        }
        # A tupla retorna a chave e seu value (1, ("ITEM", 50))
    
    """
    for ids, detalhes in almoxarifado.items():  # Itera sobre chave e valor do almoxarifado
        if nome in detalhes:  # Verifica se o nome está presente nos detalhes  
            return ids, detalhes
    return None, None 


def checker_fields(texto):
    """
    Função que verifica se o campo de esta esta preenchido ou é uma espaço.

    Args:
        texto (prompt): Inserção de dados do usuário.

    Returns:
        booleano: True se o texto é valido / False se inválido.
    """
    if not texto or texto.isspace():
        return False
    else:
        return True


def input_tratado(prompt):
    """
    Função para input_tratado, impede que o usuário deixe o tempo em branco.

    Args:
        prompt (str): Texto do usuário.

    Returns:
        text: Texto que o usuário digitou.
    """
    while True:
        text = input(prompt).upper().strip()
        if not text:
            error_msg("Operação inválida")
        else:
            break
    return text


def limpar_tela():
    """Função para limpar a tela"""
    system('cls' if name == 'nt' else 'clear')


def leia_int(prompt):
    """
    Solicita ao usuário que digite um número inteiro.

    Args:
        prompt (str): A mensagem a ser exibida ao solicitar a entrada.

    Returns:
        int: O número inteiro digitado pelo usuário.

    Trata o erro ValueError se o valor fornecido não for um inteiro e 
    solicita ao usuário que digite novamente até que um número válido seja fornecido.
    """
    while True:
        try:
            inteiro_input = input(prompt)
            inteiro_input = int(inteiro_input)
            return inteiro_input
        except ValueError:
            print()
            error_msg("É preciso um número válido para prosseguir.")
            print()


def leia_float(prompt):
    """
    Solicita ao usuário que digite um número float.

    Args:
        prompt (str): A mensagem a ser exibida ao solicitar a entrada.

    Returns:
        float: O número float digitado pelo usuário.

    Trata o erro ValueError se o valor fornecido não for um float e 
    solicita ao usuário que digite novamente até que um número válido seja fornecido.
    """
    while True:
        try:
            float_input = input(prompt).replace(",", ".")
            float_input = float(float_input)
            return float_input
        except ValueError:
            error_msg("Para prosseguir digite um número válido.")


def leia_item(prompt):
    """
    Solicita ao usuário que digite o nome de um item.

    Args:
        prompt (str): A mensagem a ser exibida ao solicitar a entrada.

    Returns:
        str: O nome do item digitado pelo usuário.

    Valida que o nome do item contenha apenas letras, espaços ou '-' e não esteja vazio.
    """
    while True:
        texto = input(prompt)
        
        if checker_fields(texto):
            if texto.isalpha() or '-' in texto or ' ' in texto:
                return texto
            else:
                error_msg("O nome do item deve conter apenas letras, espaços ou '-'")
        else:
            error_msg("O nome do item não pode estar vazio. Por favor, preencha o nome.")


def leiaCPF(prompt):
    """
    Solicita ao usuário que digite um CPF.

    Args:
        prompt (str): A mensagem a ser exibida ao solicitar a entrada.

    Returns:
        str: O CPF digitado pelo usuário no formato XXX.XXX.XXX-XX.

    Valida que o CPF tenha 11 dígitos e esteja no formato correto.
    """
    while True:
        cpf_func = input(prompt).strip()
        cpf_limpar = cpf_func.replace(".", "").replace("-", "")
        if len(cpf_limpar) == 11 and cpf_limpar.isdigit():
            return cpf_func
        else:
            error_msg("CPF inválido, formato: XXX.XXX.XXX-XX")


def leia_nome(prompt):
    """
    Solicita ao usuário que digite um nome.

    Args:
        prompt (str): A mensagem a ser exibida ao solicitar a entrada.

    Returns:
        str: O nome digitado pelo usuário.

    Valida que o nome contenha apenas letras e espaços, e o formata em título.
    """
    while True:
        nome = input(prompt).strip().title()
        if nome.replace(" ", "").isalpha():
            return nome
        else:
            error_msg("Nome inválido!")
