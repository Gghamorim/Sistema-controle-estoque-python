from database.connection import conectar

def cadastrar_produto(nome, quantidade, preco):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
        (nome, quantidade, preco)
    )

    conn.commit()
    conn.close()
    print("✅ Produto cadastrado com sucesso!")


def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    print("\n📦 LISTA DE PRODUTOS")
    print("-" * 40)

    for produto in produtos:
        print(f"ID: {produto[0]}")
        print(f"Nome: {produto[1]}")
        print(f"Quantidade: {produto[2]}")
        print(f"Preço: R${produto[3]:.2f}")
        print("-" * 40)

    conn.close()


def atualizar_produto(id, nome, quantidade, preco):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE produtos
        SET nome = ?, quantidade = ?, preco = ?
        WHERE id = ?
    """, (nome, quantidade, preco, id))

    conn.commit()
    conn.close()
    print("✏️ Produto atualizado com sucesso!")


def deletar_produto(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))

    conn.commit()
    conn.close()
    print("🗑️ Produto deletado com sucesso!")