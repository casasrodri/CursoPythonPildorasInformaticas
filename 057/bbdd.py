import sqlite3

conn = sqlite3.connect('057/gestionProductos.sqlite')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion     VARCHAR(50),
        precio          INTEGER,
        categoria       VARCHAR(20)
    )
''')

productos = [
    ('botella', 12, 'bazar'),
    ('vaso', 123, 'bazar'),
    ('plato', 9, 'bazar'),
    ('guante', 44, 'vestimenta'),
    ('bicicleta', 12, 'deporte'),
]

insert_varios = "INSERT INTO productos VALUES (NULL, ?, ?, ?)"
cursor.executemany(insert_varios, productos)
conn.commit()


cursor.execute("INSERT INTO productos VALUES (NULL, 'mouse', 2332, 'computación')")
conn.commit()


cursor.close()
conn.close()
