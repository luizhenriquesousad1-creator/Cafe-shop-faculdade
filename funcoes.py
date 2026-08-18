import unicodedata
from datetime import datetime

def normalizar_texto(texto):

    texto_normalizado = []

    nfkd = unicodedata.normalize('NFKD', texto)


    for letra in nfkd:
        if not unicodedata.combining(letra):
            texto_normalizado.append(letra)

    texto_normalizado = "".join(texto_normalizado)

    return texto_normalizado.lower()

def menu_principal():
    separador()
    print("MENU")
    separador()
    print("1 - Cadastrar produto")
    print("2 - Cadastrar cliente")
    print("3 - Listar produtos")
    print("4 - Buscar produto")
    print("5 - Editar produto")
    print("6 - Remover produto")
    print("7 - Venda")
    print("8 - Sair")

    separador()

def cadastro_produto(produtos):

    print("Cadastro de Produto")

    produto = {}
    novo_id = len(produtos) + 1

    produto["ID"] = novo_id
    produto["nome"] = normalizar_texto(str(input("Insira o nome do produto: ")))
    produto["preço"] = float(input("Insira o preço do produto: "))
    produto["estoque"] = int(input("Insira a quantidade do produto em estoque: "))

    return produto

def cadastrar_cliente(clientes):

    print("Cadastro de Cliente")

    cliente = {}

    if not clientes:
        proximo_id = 1

    else:
        proximo_id = max(cliente["ID"] for cliente in clientes) + 1

    cliente["ID"] = proximo_id
    cliente["nome"] = str(input("Insira o nome do cliente: "))
    cliente["CPF"] = str(input("Insira o CPF do cliente: "))
    cliente["telefone"] = str(input("Insira o numero de telefone: "))
    cliente["pontos"] = 0

    return cliente

def listar_produtos(produtos):

    for produto in produtos:

        separador()
        print(f"ID - {produto["ID"]}")
        print(f"produto:....{produto["nome"]}")
        print(f"preço:......R${produto["preço"]:.2f}")
        print(f"estoque:....{produto["estoque"]}")
        separador()

def buscar_cliente(clientes):

    buscador = int(input("Insira o ID do cliente: "))

    resultado = next((cliente for cliente in clientes if cliente["ID"] == buscador), False)

    if resultado == False:
        print("Cliente não cadastrado!")
        return False

    else:
        return resultado

def buscar_produto(produtos):

    print("Buscar produto por ID.....[1]")
    print("Buscar produto por nome...[2]")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:

        buscador = int(input("Insira o ID do produto: "))
        resultado = next((produto for produto in produtos if produto["ID"] == buscador), False)

        if resultado == False:
            print("produto não encontrado")
            return False

        else:
            return resultado

    elif opcao == 2:

        buscador = []

        nfkd = str(input("Digite o nome do produto: ")).lower()
        decodificacao = unicodedata.normalize('NFKD', nfkd)

        for letra in decodificacao:
            if not unicodedata.combining(letra):

                buscador.append(letra)

        buscador = "".join(buscador)

        resultado = next((produto for produto in produtos if produto["nome"] == buscador), False)

        if resultado == False:
            print("produto não encontrado")
            return False

        else:
            return resultado
    else:
        print("Opção inválida!")
        return False

def editar_produto(produtos):

    produto = buscar_produto(produtos)

    if produto == False:
        return

    """print("Produto encontrado: ")
    print(produto)"""

    separador()

    print("nome.....[1]")
    print("preço....[2]")
    print("estoque....[3]")

    opcao = int(input("Que opção deseja alterar?"))

    if opcao == 1:

        novo_nome = str(input("Insira o nome do produto: "))
        produto["nome"] = normalizar_texto(novo_nome)
        print("Nome do produto alterado com sucesso!")

        print(f"nome do prodouto {produto["nome"]}")
        print(f"preço do produto {produto["preço"]}")
        print(f"estoque do produto {produto["estoque"]}")

    elif opcao == 2:

        novo_preco = float(input("Insira o novo preço do produto: "))
        produto["preço"] = novo_preco
        print("Preço do produto alterado com sucesso!")

        print(f"nome do prodouto {produto["nome"]}")
        print(f"preço do produto {produto["preço"]}")
        print(f"estoque do produto {produto["estoque"]}")

    elif opcao == 3:

        novo_estoque = int(input("Insira o novo estoque do produto: "))
        produto["estoque"] = novo_estoque
        print("Estoque do produto alterado com sucesso!")

        print(f"nome do prodouto {produto["nome"]}")
        print(f"preço do produto {produto["preço"]}")
        print(f"estoque do produto {produto["estoque"]}")

def remover_produto(produtos):

    produto = buscar_produto(produtos)

    if produto == False:
        return

    print("deseja remover o produto ?")
    print("Sim.....[1]")
    print("Não.....[2]")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("Tem certeza que deseja excluir o produto?")
        print("Sim.....[1]")
        print("Não.....[2]")

        verificacao = int(input("Digite a opção desejada: "))

        if verificacao == 1:

            produtos.remove(produto)
            print("Produto removido com sucesso!")


        elif verificacao == 2:
            return

        """else:
            print("Opção invalida!")
            print("Digite uma opção valida:")
            verificacao = int(input("Tem certeza que deseja excluir o produto?"))

            print("Sim.....[1]")
            print("Não.....[2]")"""

def vendas(produtos, clientes, registro_vendas):

    cliente = buscar_cliente(clientes)

    if cliente == False:
        return

    produto = buscar_produto(produtos)

    if produto == False:
        return

    quantidade = int(input("Quantas produtos o cliente deseja:  "))
    venda = {}

    if quantidade > produto["estoque"]:

        print("Estoque insuficiente para venda")

    else:

        produto["estoque"] = produto["estoque"] - quantidade

        valor = produto["preço"] * quantidade

        pontos = int(valor)
        cliente["pontos"] += pontos

        print(f"pontos ganhos {pontos}")
        print(f"pontos acumulados {cliente["pontos"]}")

        # Adiciona venda a lista
        if not registro_vendas:
            proximo_id = 1

        else:
            proximo_id = max(venda["ID"] for venda in registro_vendas) + 1

        venda["Data"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        venda["ID"] = proximo_id
        venda["Cliente"] = cliente["ID"]
        venda["Produto"] = produto["ID"]
        venda["preço"] = produto["preço"]
        venda["quantidade"] = quantidade
        venda["total"] = valor

        registro_vendas.append(venda)


def separador():
    print("-"*30)