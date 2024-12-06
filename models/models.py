from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_usuario = Column(String(50), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)
    es_admin = Column(Boolean, default=False)  # Booleano para indicar si es administrador
    es_empleado = Column(Boolean, default=False)  # Booleano para indicar si es empleado

class Ingrediente(Base):
    __tablename__ = 'ingredientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    tipo = Column(String(50), nullable=False)
    inventario = Column(Float, default=0.0)

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    precio_publico = Column(Float, nullable=False)
    calorias = Column(Float, nullable=False)
    ingrediente1_id = Column(Integer, ForeignKey('ingredientes.id'))
    ingrediente1 = relationship('Ingrediente')

engine = create_engine('sqlite:///usuarios.db')
Base.metadata.create_all(engine)
