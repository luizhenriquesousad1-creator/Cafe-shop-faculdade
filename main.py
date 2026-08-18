#importações
import unicodedata
from funcoes import (menu_principal, cadastro_produto, cadastrar_cliente, listar_produtos, buscar_produto,
                     editar_produto, normalizar_texto, remover_produto)

#Variáveis
produtos = [{"ID": 1 ,"nome": "cafe", "preço":8.5, "estoque": 50}, {"ID":2, "nome": "capuccino", "preço": 10.0, "estoque": 50}]
clientes = []

#menu
while True:
    menu_principal()

    opcao = int(input("escolha a opção desejada: "))


    if opcao == 1:
        novo_produto = cadastro_produto(produtos)
        produtos.append(novo_produto)
        print(produtos)

    elif opcao == 2:
        novo_cliente = cadastrar_cliente()
        clientes.append(novo_cliente)
        print(clientes)

    elif opcao == 3:
        listar_produtos(produtos)

    elif opcao == 4:
        print("Procurando...")
        buscar_produto(produtos)

    elif opcao == 5:

        editar_produto(produtos)

    elif opcao == 6:

        remover_produto(produtos)

    elif opcao == 7:
        print("Salvando alterações")
        print("Finalizando...")
        break

    elif opcao == 8:
        print("Procurando...")
        buscar_produto(produtos)

    elif opcao == 9:
        texto_teste = str(input("Digite alguma coisa ai: "))
        normalizar_texto(texto_teste)
        print(normalizar_texto(texto_teste))