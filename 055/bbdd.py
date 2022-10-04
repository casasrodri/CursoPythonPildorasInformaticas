# Pasos
# 1. Abrir conexion
# 2. Crear puntero
# 3. Ejecutar query
# 4. Manejo de resultados (CRUD)
# 5. Cerrar puntero
# 6. Cerrar conexion

import sqlite3

conn = sqlite3.connect('055/primera_base.sqlite')
cursor = conn.cursor()

query = 'CREATE TABLE IF NOT EXISTS productos ( \
            descripcion VARCHAR(50), \
            precio INTEGER, \
            categoria VARCHAR(20) \
        )'
cursor.execute(query)

insert = "INSERT INTO productos VALUES ('pelota', 22, 'deporte')"
cursor.execute(insert)
conn.commit()

cursor.close()
conn.close()
