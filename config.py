class Config:
    SECRET_KEY = 'tu_clave_secreta'  # Esto es necesario para la gestión de sesiones
    SQLALCHEMY_DATABASE_URI = 'sqlite:///usuarios.db'  # O la URI correspondiente para tu base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
