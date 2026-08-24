import sqlite3
from pathlib import Path

root_dir = Path(__file__).parent

DB_name = 'db.sqlite3'

db_file = root_dir / 'db' / DB_name

table_users = 'customers'

connection = sqlite3.connect(db_file)
cursor = connection.cursor()
cursor.execute(
    f' CREATE TABLE IF NOT EXISTS {table_users}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'idade INTEGER,'
    'cpf INTEGER UNIQUE,'
    'dia INTEGER'
    ')'
)
table_users_2 = 'logins'
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {table_users_2}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT, '
    'usuário TEXT, '
    'senha TEXT '
    ')'
)

cursor.execute(
    'INSERT INTO logins (usuário, senha) VALUES (?, ?)',
    ('admin', 'admin')
)
connection.commit()
cursor.close()
connection.close()