import sqlite3
from pathlib import Path

# Caminha relativo
ROOT_PATH = Path(__file__).parent

# Criar conexao e banco de dados
conexao = sqlite3.connect(ROOT_PATH / "clientes.db")
cursor = conexao.cursor

# criando uma tabela
cursor.execute(
    "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTO INCREMENT, nome(VARCHAR 100), email (VARCHAR 150))"
)

# Mascarando a inserção
data = ("Walter Junior", "teste@teste.com")

# Inserindo dados
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
conexao.commit()
