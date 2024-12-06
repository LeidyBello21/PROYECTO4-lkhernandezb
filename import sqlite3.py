import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Verificar las tablas disponibles
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()

if ('usuarios',) in tablas:
    # Seleccionar todos los registros de la tabla usuarios
    cursor.execute("SELECT * FROM usuarios;")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
else:
    print("La tabla 'usuarios' no existe en la base de datos.")

# Cerrar la conexión
conn.close()
