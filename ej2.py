import sqlite3

conn = sqlite3.connect('EESTN5.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL
    )
''')

alumnos_datos = [
    (1, "Juan Pérez", 16),
    (2, "María López", 18),
    (3, "Carlos García", 17),
    (4, "Ana Martínez", 19),
    (5, "Lucas Rodríguez", 18),
    (6, "Sofía Castro", 16),
    (7, "Diego Sánchez", 19),
    (8, "Valentina Ruiz", 17)
]

cursor.executemany('INSERT OR REPLACE INTO alumnos VALUES (?,?,?)', alumnos_datos)
conn.commit()

print("Alumnos mayores de 17 años:")
print("-" * 30)
cursor.execute('SELECT * FROM alumnos WHERE edad > 17')
for alumno in cursor.fetchall():
    print(f"ID: {alumno[0]}, Nombre: {alumno[1]}, Edad: {alumno[2]}")

conn.close()