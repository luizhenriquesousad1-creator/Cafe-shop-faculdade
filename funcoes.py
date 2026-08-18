import unicodedata

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
    print("7 - Sair")
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

def cadastrar_cliente():

    print("Cadastro de Cliente")

    clientes = {}
    clientes["nome"] = str(input("Insira o nome do cliente: "))
    clientes["CPF"] = str(input("Insira o CPF do cliente: "))
    clientes["telefone"] = str(input("Insira o numero de telefone: "))
    clientes["pontos"] = 0

    return clientes

def listar_produtos(produtos):

    for produto in produtos:

        separador()
        print(f"ID - {produto["ID"]}")
        print(f"produto:....{produto["nome"]}")
        print(f"preço:......R${produto["preço"]:.2f}")
        print(f"estoque:....{produto["estoque"]}")
        separador()


def buscar_produto(produtos):
    print("buscar produto")
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
            """separador()
            print(f"ID ... {resultado['ID']}")
            print(f"nome ... {resultado['nome']}")
            print(f"preço ...{resultado['preço']}")
            print(f"estoque....{resultado['estoque']}")
            separador()"""

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
            """"separador()
            print(f"ID ... {resultado['ID']}")
            print(f"nome ... {resultado['nome']}")
            print(f"preço ...{resultado['preço']}")
            print(f"estoque ....{resultado['estoque']}")
            separador()"""


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


def separador():
    print("-"*30)