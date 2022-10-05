import sqlite3

#DB_PATH = '059/Rodri/clientes.sqlite'
DB_PATH = './clientes.sqlite'

def create_table(conn):
    conn.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre          VARCHAR(50),
            apellido        VARCHAR(50),
            password        VARCHAR(50),
            direccion       VARCHAR(50),
            observaciones   VARCHAR(300)
        )
    ''')

def connect():
    conn = sqlite3.connect(DB_PATH)
    create_table(conn)

    return conn


def create(conn, dict):
    sentencia = "INSERT INTO clientes VALUES (NULL, ?, ?, ?, ?, ?)"
    datos = list(dict.values())
    del datos[0]

    cursor = conn.execute(sentencia, datos)
    conn.commit()

    return cursor.lastrowid

def read(conn, id):
    sentencia = f"SELECT * FROM clientes WHERE id = {id}"
    cursor = conn.execute(sentencia)

    return cursor

def update():
    pass

def delete():
    pass
