from views import * 
from data import *
from tools import *

def adm(acesso): # Função não utilizada diretamente por main.
  """
  Validar acesso para a área administrativa.

  Args:
      acesso (str): senha

  Returns:
      Booleana: Acesso autorizado ou negado
  """
  chave = input(acesso)
  if chave == "cpD13":
    return True
  else:
    return False 
  

def contratar():
  """
  Função para contratar novos funcionários.

  Solicita primeiro o CPF, se o CPF existir, retorna um input de pessoa já cadastrada.
  Se não, solicita nome, idade, rua, bairro, numero, cidade, uf e retorna um input
  de "Contratação realizada com sucesso."

  Returns:
      input: Mostrar ação finalizada e seguir o código.

  Fluxo:
      1. Solicita o CPF.
      2. Verifica existência do CPF em dicionário de funcionarios.
        2.1 Se existe:
          - Retorna input("Pessoa já cadastrada.")
        2.2 Se não existe:
          - Solicita nome, idade, rua, bairro, numero, cidade, uf.
      3. Insere, a partir do cpf, os dados no dicionários de funcionários.
      4. Salva os dados no arquivo.
      5. Retorna input("Contratação realizada com sucesso.")
  
  Forma de funcionarios:
      funcionarios = {
        "11122233300": {
          "Nome": Anderson,
          "Idade": 22,
          "Endereço": f"{rua}, {bairro}, {numero}. {cidade}/{uf}"
        }      
      }
      
  """
  limpar_tela()
  subtitulo("Contratação")

  cpf = leiaCPF("CPF: ")
  if cpf in funcionarios:
    return input("Pessoa já cadastrada.")
  
  else:
    nome = leia_nome("Nome:  ")
    idade = leia_int("Idade: ")
    rua = leia_nome("Rua:  ")
    bairro = leia_nome("Bairro: ")
    if "Rua" in rua:
       rua.replace("Rua", "")

    numero = leia_int("Número: ")
    cidade = leia_nome("Cidade:  ")
    uf = leia_item("Estado:  ").upper()
    endereco = f"{rua}, {bairro}, {numero}. {cidade}/{uf}"

    funcionarios[cpf] =  {"Nome": nome, "Idade": idade, "Endereço": endereco}

    save_data("arquivo_funcionarios.dat", funcionarios)
    
    return input("Contratação realizada com sucesso.")
  

def demitir():
  """
  Função para demitir funcionários.

  Solicita primeiro o CPF. Se o CPF não existir, retorna um input informando que a pessoa não foi encontrada.
  Se o CPF existir, mostra os dados do funcionário a ser demitido e solicita confirmação. 
  Se confirmado, remove o funcionário do dicionário e salva as alterações no arquivo. 
  Caso contrário, a operação é cancelada.

  Returns:
      input: Mostrar ação finalizada e seguir o código.

  Fluxo:
      1. Solicita o CPF.
      2. Verifica existência do CPF no dicionário de funcionários.
        2.1 Se não existe:
          - Retorna input("Pessoa não encontrada nos registros de funcionários. >> Enter")
        2.2 Se existe:
          - Mostra dados do funcionário a ser demitido.
          - Solicita confirmação (S/N).
            2.2.1 Se confirmado (S):
              - Remove o funcionário do dicionário.
              - Salva os dados no arquivo.
              - Retorna input("Funcionário desligado da empresa com sucesso! >> Enter")
            2.2.2 Se não confirmado (N):
              - Retorna input("Operação cancelada. >> Enter")

  Forma de funcionarios:
      funcionarios = {
        "11122233300": {
          "Nome": Anderson,
          "Idade": 22,
          "Endereço": "Rua X, Bairro Y, 123. Cidade/ZF"
        }      
      }
      
  """
  limpar_tela()
  subtitulo("Demissão")

  cpf = leiaCPF("CPF: ")
  if cpf not in funcionarios:
    return input(f"Pessoa não encontrada nos registros de funcionários << Enter >>")
  
  else:
    error_msg(f"Funcionário a ser desligado:  {funcionarios[cpf]['Nome']}")
    while True: 
      confirmacao = input_tratado("Confirmar[S/N]:  ")
      if confirmacao[0].upper() not in 'SN':
        error_msg("Opção inválida")

      else:
        if confirmacao[0].upper() in 'S':
          funcionarios.pop(cpf)
          save_data("arquivo_funcionarios.dat", funcionarios)
          
          return input(f"Funcionário desligado da empresa com sucesso! >> Enter")
        
        elif confirmacao[0].upper() in 'N':
          return input("Operação cancelada. >> Enter")


def buscar():
  """
  Função para buscar funcionário.

  Solicita primeiro o CPF. Se o CPF existir no dicionário de funcionários, exibe os dados do funcionário.
  Se o CPF não existir, retorna um input informando que o funcionário não foi encontrado.

  Returns:
      input: Mostrar ação finalizada e seguir o código.

  Fluxo:
      1. Solicita o CPF.
      2. Verifica existência do CPF no dicionário de funcionários.
        2.1 Se existe:
          - Exibe os dados do funcionário (CPF, Nome, Idade, Endereço).
          - Retorna input(">> Enter.")
        2.2 Se não existe:
          - Retorna input("Funcionário não encontrado.")
  
  Forma de funcionarios:
      funcionarios = {
        "11122233300": {
          "Nome": Anderson,
          "Idade": 22,
          "Endereço": "Rua X, Bairro Y, 123. Cidade/ZF"
        }      
      }
      
  """
  limpar_tela()
  cpf = leiaCPF("CPF: ")

  if cpf in funcionarios:

    subtitulo("Funcionário")
    nome = funcionarios[cpf]['Nome']
    idade = funcionarios[cpf]['Idade']
    endereco = funcionarios[cpf]['Endereço']
    
    linha()
    quadro(cpf, nome, idade, endereco)
    linha()

    return input(">> Enter.")
    
  else:
    return input("Funcionário não encontrado.")
  

def editar_funcionario():
  """
  Função para edição dos dados do funcionário.

  Solicita primeiro o CPF. Se o CPF existir no dicionário de funcionários, permite a edição dos dados (Nome, Idade, Rua, Número, Cidade, Estado).
  Se o CPF não existir, retorna False.

  Returns:
      str: CPF do funcionário se a edição for bem-sucedida.
      bool: False se o funcionário não for encontrado.

  Fluxo:
      1. Solicita o CPF.
      2. Verifica existência do CPF no dicionário de funcionários.
        2.1 Se existe:
          - Solicita os novos dados do funcionário (Nome, Idade, Rua, Número, Cidade, Estado).
          - Atualiza o dicionário com os novos dados.
          - Salva os dados no arquivo.
          - Retorna o CPF do funcionário.
        2.2 Se não existe:
          - Retorna False.

  Forma de funcionarios:
      funcionarios = {
        "11122233300": {
          "Nome": Anderson,
          "Idade": 22,
          "Endereço": "Rua X, Bairro Y, 123. Cidade/ZF"
        }      
      }
      
  """
  cpf = leiaCPF("CPF: ")

  if cpf in funcionarios:
    nome = leia_nome("Nome:  ")
    idade = leia_int("Idade: ")
    rua = leia_nome("Rua:  ")
    if "Rua" in rua:
       rua.replace("Rua", "")

    numero = leia_int("Número: ")
    cidade = leia_nome("Cidade:  ")
    uf = leia_nome("Estado:  ").upper()
    endereco = f"{rua}, {numero}. {cidade}/{uf}"

    funcionarios[cpf] =  {"Nome": nome, "Idade": idade, "Endereço": endereco}

    save_data("arquivo_funcionarios.dat", funcionarios)

    return cpf
  else:
    return False
  