# Hamburgueria do Py

## Descrição
Este projeto é uma aplicação de gestão para uma hamburgueria, desenvolvida em Python. Permite gerenciar compras, vendas, almoxarifado, funcionários, clientes e geração de relatórios.

## Funcionalidades Principais
- **Compras**: Cadastro de mercadorias.
- **Almoxarifado**: Busca e exclusão de itens.
- **Vendas**: Exibição do cardápio, administração e fechamento de vendas.
- **Funcionários**: Gerenciamento de quadro de funcionários, contratação e demissão.
- **Clientes**: Cadastro e edição de informações de clientes.
- **Relatórios**: Geração de relatórios de compras, vendas e itens mais vendidos.
- **Informações**: Detalhes sobre o projeto e a equipe de desenvolvimento.

## Modularização
O projeto é totalmente modularizado, com os seguintes pacotes:

- **almoxarifado**: Funcionalidades relacionadas ao controle de estoque.
- **clientes**: Funcionalidades relacionadas ao cadastro e gerenciamento de clientes.
- **compras**: Funcionalidades relacionadas ao cadastro de compras e mercadorias.
- **data**: Módulo de dados utilizado para armazenamento e manipulação de informações.
- **funcionarios**: Funcionalidades relacionadas ao gerenciamento de funcionários.
- **menu**: Interface de usuário para navegação e interação com o sistema.
- **relatorios**: Funcionalidades para geração e exibição de relatórios estatísticos.
- **tools**: Ferramentas auxiliares para tratamento de dados e interface.
- **vendas**: Funcionalidades relacionadas ao gerenciamento de vendas e cardápio.
- **views**: Componentes de interface gráfica e textual utilizados nas interações com o usuário.

## Requisitos de Instalação
Para executar o projeto localmente, é necessário ter Python instalado. As dependências estão listadas nos arquivos `data.py`, `views.py`, `tools.py` e outros módulos específicos nas pastas.


## Uso
Para iniciar o programa, execute o arquivo principal `main.py`. O programa apresentará um menu interativo com as opções disponíveis.

```python
python main.py
