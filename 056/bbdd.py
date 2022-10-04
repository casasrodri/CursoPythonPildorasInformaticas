# Pasos
# 1. Abrir conexion
# 2. Crear puntero
# 3. Ejecutar query
# 4. Manejo de resultados (CRUD)
# 5. Cerrar puntero
# 6. Cerrar conexion

import sqlite3

conn = sqlite3.connect('056/primera_base.sqlite')
cursor = conn.cursor()

productos = [
    ('botella', 12, 'bazar'),
    ('vaso', 123, 'bazar'),
    ('plato', 9, 'bazar'),
    ('guante', 44, 'vestimenta'),
    ('bicicleta', 12, 'deporte'),
]

insert_varios = "INSERT INTO productos VALUES (?, ?, ?)"
#cursor.executemany(insert_varios, productos)
#conn.commit()

# Select
cursor.execute("SELECT * FROM productos")

todos_productos = cursor.fetchall()

print(todos_productos)

for producto in todos_productos:
    print(f"1 {producto[0]} cuesta ${producto[1]}.")

cursor.close()
conn.close()
