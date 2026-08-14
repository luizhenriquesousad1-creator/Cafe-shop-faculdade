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

  A função cadastra_produto() é responsável por coletar os dados de um novo produto e organizar essas informações em   um
  dicionário que posteriormente será armazenado em uma lista de produtos.

  ASSINATURA:
  
  def cadastrar_produtos(produtos):

  a função recebe como parâmetro a lista de produtos que contém os produtos já cadastrados, essa lista é usada para 
  determinar o identificador do novo produto.

  ETAPAS DE EXECUÇÃO

  1. Exibição do título da operação:
     
     A função inicia apresentando uma mensagem informando que o usuário está realizando o cadastro de um produto.
     print("Cadastro de Produto")
     Essa mensagem tem a finalidade de orientar o usuário durante a execução do sistema.
     
  2. Criação do dicionário do produto:

     Um dicionário vazio é criado para armazenar os dados referentes ao novo produto.
     produto ={}
     A partir desse momento, as informações coletadas serão adicionadas ao dicionário utilizando chaves específicas.
     
  3. Geração do identificador:

     O sistema calcula o identificador para o novo produto por meio da expreção:
     
     novo_id = len(produtos) + 1

     A quantidade de elementos existentes na lista obtida por meio da da função len(). em seguida, é acrescentado 1       para gerar o identificador do novo produto.
     
  4. Armamento do ID:

     O identificador calculado é armazenado no dicionário do produto:

     produto["ID"] = novo_id

     Esse valor será utilizado posteriormente para identificar o produto nas operações de busca, edição e remoção.
     
  5. Cadastro do nome:
     
     O sistema solicita ao usuário o nome do produto:

     produto["nome"] = ...

     o nome é armazenado no dicionário  utilizando a chave "nome".
     
  6. Cadastro do preço:

      O preço informado pelo usuário é convertido para o tipo float, permitindo o trabalho com valores monetários          que possuam casas decimais.

     produto["preço"] = float(...)
     
  7. Cadastro do estoque:

     A quantidade inicial disponível no estoque é recebida pelo sistema e convertida para o tipo int.

     produto["estoque"] = int(...)
     
  8. RETORNO DO PRODUTDO

     Depois que todos os dados são preenchidos, a função retorna o dicionário criado:

     return produto

     Esse retorno permite que o programa principal receba o novo produto e adicione-o à lista:

     novo_produto = cadastrar_produto(produto)
     produtos.append(novo_produto)

     Estrutura resultate:

     {"ID": 1 , "nome": "cafe" , "preço": 8.50 , "estoque": 50}

     RESUMO DO FLUXO

     recebe lista de produtos > gerar id > criar dicionário > receber nome > receber preço > receber estoque > retornar produto.
  
  5.2 FUNÇÃO listar_produtos()

  A função listar_produto() é responsável por percorrer a lista de produtos cadastrados e apresentar na tela as        principais informações de cada produto
  A função recebe como parâmetro a lista de produtos que contém dicionários representando os produtos cadastrados.

  ASSINATURA

  def listar_produtos(produtos)

  O parâmetro produtos representa a coleção de produtos armazenado pelo sistema.

  ETAPAS DE EXECUÇÂO

    1.PERCORRER A LISTA DE PRODUTOS
    A função utiliza uma estrutura de repetição for para percorrer cada elemento da lista:
      
  for produto in produtos:

  A cada repetição, a variável produto representa um dos dicionários armazenados na lista, por exemplo:

  { "ID": 1, "nome": "cafe", "preço": 8.50, "estoque": 50 }}=
  
 2. APRESENTAR UM SEPADADOR VISUAL

Antes de exibir os dados, a função utiliza uma sequência de caracteres para separar visualmente os produtos:

print("-" * 30)

A expressão "-" * 30 produz uma sequência contendo 30 caracteres -.

3. EXIBIR O IDENTIFICADOR DO PRODUTO

O ID é obtido diretamente do dicionário:

print(f"ID - {produto['ID']}")

A chave "ID" permite acessar o identificador armazenado no produto.

4. EXIBIR O NOME DO PRODUTO

O nome é acessado pela chave "nome":

print(f"produto.....{produto['nome']}")

5. EXIVIR O PREÇO

O preço é acessado pela chave "preço":

print(f"preço.......{produto['preço']}")

O valor armazenado no dicionário é utilizado diretamente na apresentação.

6. EXIBIR A QUANTIDADE DE ITENS EM ESTOQUE

A quantidade disponível é apresentada por meio da chave "estoque":

print(f"estoque.....{produto['estoque']}")

7. ENCERRAR A APRESENTAÇÃO DO PRODUTO

Ao final de cada iteração, outro separador é apresentado:

print("-" * 30)

Depois disso, o for continua para o próximo produto da lista.

Exemplo de execução

Considerando a seguinte lista:

produto = [{"ID": 1 , "nome": "cafe" , "preço": 8.50 , "estoque": 50} , {"ID": 2 , "nome": "capuccino" , "preço": 10.0 , "estoque": 50}]

A função apresenta:

------------------------------
ID - 1
produto.....cafe
preço.......8.50
estoque.....50
------------------------------
ID - 2
produto.....capuccino
preço.......10.0
estoque.....50
------------------------------
Estrutura utilizada

A função trabalha com duas estruturas principais:

lista
  ↓
produtos
  ↓
dicionários
  ↓
ID, nome, preço e estoque

A lista permite armazenar vários produtos, enquanto cada dicionário organiza as informações de um produto individual.

Retorno

A função não utiliza return. Sua responsabilidade é apresentar os produtos diretamente na interface de execução.

Resumo do fluxo
Receber lista de produtos
          ↓
Percorrer cada produto
          ↓
Acessar os dados do dicionário
          ↓
Exibir ID
          ↓
Exibir nome
          ↓
Exibir preço
          ↓
Exibir estoque
          ↓
Passar para o próximo produto





  
  
