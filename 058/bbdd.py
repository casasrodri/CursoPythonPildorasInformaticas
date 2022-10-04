import sqlite3

conn = sqlite3.connect('058/gestionProductos.sqlite')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion     VARCHAR(50) UNIQUE,
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
    ('vaso', 123, 'bazar')
]

insert_varios = "INSERT INTO productos VALUES (NULL, ?, ?, ?)"
#cursor.executemany(insert_varios, productos)
#conn.commit()


#cursor.execute("INSERT INTO productos VALUES (NULL, 'mouse', 2332, 'computación')")
#conn.commit()


# Select
cursor.execute("SELECT * FROM productos WHERE categoria = 'bazar' ")

print('Productos de la categoría BAZAR:')
for producto in cursor.fetchall():
    print(f"1 {producto[1]} cuesta ${producto[2]}.")


# Update
cursor.execute("UPDATE productos SET precio = 9999 WHERE descripcion = 'vaso' ")
conn.commit()

# Delete
cursor.execute("DELETE FROM productos WHERE id = 5 ")
conn.commit()

cursor.close()
conn.close()
