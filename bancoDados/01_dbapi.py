import sqlite3
from pathlib import Path

# Caminha relativo
ROOT_PATH = Path(__file__).parent

# Criar conexao e banco de dados
conexao = sqlite3.connect(ROOT_PATH / "clientes.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


# criando uma tabela
def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTO INCREMENT, nome(VARCHAR 100), email (VARCHAR 150))"
    )


# Mascarando a inserção
def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    # Inserindo dados
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
    conexao.commit()


# UPDATE
def atualizar_registro(conexao, cursor, nome, email):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?", data)
    conexao.commit()


# atualizar_registro(conexao, cursor, "Teste", "teste@teste.com", 1)


# DELETE
def remover_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()


# remover_registro(conexao, cursor, 1)

# INSERIR REGISTRO LOTE


# Iserir registro em lote
def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    conexao.commit()


dados = [
    ("Guilherme", "guilherme@teste.com"),
    ("Teste", "teste@teste.com"),
    ("Juliana", "juliana@teste.com"),
]

# inserir_muitos(conexao, cursor, dados)

# SELECT


def recuperar_cliente(cursor):
    cursor.execute("SELECT * FROM clientes WHERE id=?", id())
    return cursor.fetchone()


def listar_cliente(cursor):
    return cursor.execute("SELECT * FROM clientes")


cliente = recuperar_cliente(cursor, 2)
print(cliente)

clientes = listar_cliente(cursor, 2)
print(dict(cliente)
print(cliente["id"], cliente["nome"], cliente["email"])
