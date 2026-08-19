import csv

def salvar_produtos(produtos):

    with open("produtos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["ID", "nome", "preço", "estoque"])

        escritor.writeheader()
        escritor.writerows(produtos)

def carregar_produtos():

    produtos = []

    with open("produtos.csv", "r", newline="", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo)

        for produto in leitor:

            produto["ID"] = int(produto["ID"])
            produto["nome"] = str(produto["nome"])
            produto["preço"] = float(produto["preço"])
            produto["estoque"] = int(produto["estoque"])

            produtos.append(produto)

    return produtos

def salvar_vendas(registro_vendas):

    with open("vendas.csv", "w", newline="", encoding="utf-8") as arquivo:

        escritor = csv.DictWriter(arquivo, fieldnames=["ID", "Data", "Cliente", "Produto", "preço",
                                                       "quantidade", "total"])

        escritor.writeheader()
        escritor.writerows(registro_vendas)

def carregar_vendas():

    registro_vendas = []

    with open("vendas.csv", "r", newline="", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo)

        for venda in leitor:

            venda["ID"] = int(venda["ID"])
            venda["Cliente"] = int(venda["Cliente"])
            venda["Produto"] = int(venda["Produto"])
            venda["preço"] = float(venda["preço"])
            venda["quantidade"] = int(venda["quantidade"])
            venda["total"] = float(venda["total"])

            registro_vendas.append(venda)

    return registro_vendas

def salvar_clientes(clientes):

    with open("clientes.csv", "w", newline="", encoding="utf-8") as arquivo:

        escritor = csv.DictWriter(arquivo, fieldnames=["ID", "nome", "CPF", "telefone", "pontos"])

        escritor.writeheader()
        escritor.writerows(clientes)

def carregar_clientes():

    clientes = []

    with open("clientes.csv", "r", newline="", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo)

        for cliente in leitor:

            cliente["ID"] = int(cliente["ID"])
            cliente["nome"] = str(cliente["nome"])
            cliente["CPF"] = str(cliente["CPF"])
            cliente["telefone"] = str(cliente["telefone"])
            cliente["pontos"] = int(cliente["pontos"])

            clientes.append(cliente)

    return clientes

