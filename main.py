from models.produto import criar_tabela
from services.produto_service import *

criar_tabela()

while True:
    print("\n📦 SISTEMA DE ESTOQUE")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Deletar produto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))
        cadastrar_produto(nome, quantidade, preco)

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        id = int(input("ID do produto: "))
        nome = input("Novo nome: ")
        quantidade = int(input("Nova quantidade: "))
        preco = float(input("Novo preço: "))
        atualizar_produto(id, nome, quantidade, preco)

    elif opcao == "4":
        id = int(input("ID do produto: "))
        deletar_produto(id)

    elif opcao == "0":
        print("👋 Encerrando sistema...")
        break

    else:
        print("❌ Opção inválida!")