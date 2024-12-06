from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash
from models.models import Usuario, Base  # Asegúrate de tener los modelos correctos importados

# Crear conexión a la base de datos
engine = create_engine('sqlite:///usuarios.db')  # Conexión a la base de datos SQLite
Session = sessionmaker(bind=engine)  # Crear la sesión
session_db = Session()  # Crear una instancia de la sesión

# Crear usuarios de prueba
def crear_usuarios():
    # Verificar si ya existen usuarios en la base de datos
    if session_db.query(Usuario).count() > 0:
        print("Los usuarios ya existen en la base de datos.")
        return

    # Usuario administrador
    admin = Usuario(
        nombre_usuario='admin',  # Nombre de usuario
        contrasena=generate_password_hash('admin123'),  # Contraseña hasheada
        es_admin=True,  # Rol administrador
        es_empleado=False  # El administrador no es empleado
    )

    # Usuario empleado
    empleado = Usuario(
        nombre_usuario='empleado',  # Nombre de usuario
        contrasena=generate_password_hash('empleado123'),  # Contraseña hasheada
        es_admin=False,  # El empleado no es administrador
        es_empleado=True  # Rol empleado
    )

    # Usuario cliente
    cliente = Usuario(
        nombre_usuario='cliente',  # Nombre de usuario
        contrasena=generate_password_hash('cliente123'),  # Contraseña hasheada
        es_admin=False,  # El cliente no es administrador
        es_empleado=False,  # El cliente no es empleado
    )

    # Agregar usuarios a la base de datos
    session_db.add_all([admin, empleado, cliente])
    session_db.commit()  # Guardar los cambios en la base de datos
    print("Usuarios creados con éxito.")

# Crear la tabla si no existe y agregar los usuarios
Base.metadata.create_all(engine)  # Crear tablas en la base de datos
crear_usuarios()  # Crear usuarios de prueba si no existen

# Cerrar la sesión
session_db.close()
