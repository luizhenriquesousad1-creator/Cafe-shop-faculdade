
def menu_principal():

    print("MENU")
    print('-' * 30)
    print("1 - Cadastrar produto")
    print("2 - Cadastrar cliente")
    print("3 - Listar produtos")
    print("4 - Buscar produto")
    print("5 - Editar produto")
    print("6 - Remover produto")
    print("7 - Sair")
    print('-' * 30)

def cadastro_produto(produtos):

    print("Cadastro de Produto")

    produto = {}
    novo_id = len(produtos) + 1

    produto["id"] = novo_id
    produto["nome"] = str(input("Insira o nome do produto: "))
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

        print("-"*30)
        print(f"ID - {produto["ID"]}")
        print(f"produto:....{produto["nome"]}")
        print(f"preço:......R${produto["preço"]:.2f}")
        print(f"estoque:....{produto["estoque"]}")
        print("-"*30)


def buscar_produto():
    pass

def editar_produto():
    pass

def remove_produto():
    pass