#importações
import unicodedata
from funcoes import (menu_principal, cadastro_produto, cadastrar_cliente, listar_produtos, buscar_produto,
                     editar_produto, normalizar_texto, remover_produto, buscar_cliente, vendas,
                     listar_vendas, relatorio_vendas)
from arquivos import (salvar_produtos, carregar_produtos, salvar_vendas, carregar_vendas, salvar_clientes,
                      carregar_clientes)


#Variáveis
produtos = carregar_produtos()
clientes = carregar_clientes()
registro_vendas = carregar_vendas()

#carregar_dados

#menu
while True:

    menu_principal()

    opcao = int(input("escolha a opção desejada: "))


    if opcao == 1:

        novo_produto = cadastro_produto(produtos)
        produtos.append(novo_produto)
        salvar_produtos(produtos)

    elif opcao == 2:

        novo_cliente = cadastrar_cliente(clientes)
        clientes.append(novo_cliente)
        salvar_clientes(clientes)


    elif opcao == 3:

        listar_produtos(produtos)

    elif opcao == 4:

        print(buscar_produto(produtos))

    elif opcao == 5:

        editar_produto(produtos)

    elif opcao == 6:

        remover_produto(produtos)

    elif opcao == 7:

        vendas(produtos, clientes, registro_vendas)
        salvar_vendas(registro_vendas)

    elif opcao == 8:

        listar_vendas(registro_vendas)

    elif opcao == 9:

        relatorio_vendas(registro_vendas)

    elif opcao == 0:
        #salvar_produtos
        salvar_produtos(produtos)

        #salva_clientes
        salvar_clientes(clientes)

        #salvar_vendas
        salvar_vendas(registro_vendas)

        print("Salvando alterações")
        print("Finalizando...")
        break

