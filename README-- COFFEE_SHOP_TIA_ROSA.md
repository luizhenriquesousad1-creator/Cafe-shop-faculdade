1 - DISCRIÇÃO DO PROJETO

  O projeto consiste no desenvolvimento de um sistema em Python destina a auxiliar o gerenciamento de uma cafeteria,
  simulando funcionalidades e atendimento e organização interna.
  A proposta do sistema apresenta uma situação problema que destaca as dificuldades relacionadas ao controle de pedidos,
  organização das informações dos produtos e cadastro de clientes.
  O sistema busca oferecer uma solução simples, organizada e fácil de utilizar.

2 - OBJETIVO DO PROJETO

  O projeto tem como objetivo desenvolver uma solução em Python que simule funcionalidades de gerenciamento e atendimento
  de uma cafeteria, incluindo cadastro de produtos, clientes e pedidos. O desenvolvimento também busca aplicar na pratica 
  os conceitos estudados na disciplina de Lógica- Algoritmos e Programação de Computadores utilizando estruturas como listas,
  dicionários e funções, além de uma interface simples para interação com o usuário.

 3 - TECNOLOGIASS E RECURSOS UTILIZADOS

   * Python
   * PyCharm
   * Git
   * GitHub
   * Listas
   * Dicionários
   * Funções
   * Estrutura condicional
   * Estrutura de repetição

  O código foi organizado em módulos para facilitar a manutenção e a compreensão do projeto.

4 - ESTRUTURA DO PROJETO

  cafe_shop_faculdade/
  │
  ├── main.py
  ├── funcoes.py
  ├── arquivos.py
  ├── interface.py
  └── .gitignore

  main.py
  É responsável pelo fluxo principal da aplicação, controlar a execução do menu e utilizar as funções responsáveis pelas
  operações do sistema.

  funcoes.py
  Contém as funções responsáveis pelas principais operações do sistema, como cadastro, linguagem e busca de produtos.

  arquivos.py
  Modulo reservado para as operações relacionadas ao armazenamento de dados em arquivos.

  interface.py
  Módulo destinado á organização da interface e da interação com o usuário.

  .gitignore
  Arquivo utilizado para impedir que arquivos e diretórios desnecessários sejam enviados ao repositório Git.

  5 - ESTRUTURA DE DADOS

  Os produtos são armazenados em uma lista de dicionários
  EXEMPLO: produto = [{"ID": 1, "nome': 'cafe', "preco": 8.50, "estoque": 50}, {"ID": 1, "nome': 'capuccino',
  "preco": 10.00, "estoque": 50}]

  Os clientes também são representados por listas de dicionarios.

  5.1 - FUNÇÃO cadastrar_produtos()

  A função cadastra_produto() é responsável por coletar os dados de um novo produto e organizar essas informações em um
  dicionário que posteriormente será armazenado em uma lista de produtos.

  ASSINATURA:
  
  def cadastrar_produtos(produtos):

  a função recebe como parâmetro a lista de produtos que contém os produtos já cadastrados, essa lista é usada para 
  determinar o identificador do novo produto.

  RESUMO DO FLUXO

  recebe lista de produtos > Gera ID > Cria dicionário > recebe nome > recebe preço > recebe estoque > retorna produto.



  







  
  
