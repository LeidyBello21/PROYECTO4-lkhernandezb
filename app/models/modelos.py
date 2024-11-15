from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Ingrediente(Base):
    __tablename__ = 'ingredientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    tipo = Column(String)
    inventario = Column(Float)

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    precio_publico = Column(Float)
    calorias = Column(Float)
    ingrediente1_id = Column(Integer, ForeignKey('ingredientes.id'))
    ingrediente2_id = Column(Integer, ForeignKey('ingredientes.id'))
    ingrediente3_id = Column(Integer, ForeignKey('ingredientes.id'))
    ingrediente1 = relationship("Ingrediente", foreign_keys=[ingrediente1_id])
    ingrediente2 = relationship("Ingrediente", foreign_keys=[ingrediente2_id])
    ingrediente3 = relationship("Ingrediente", foreign_keys=[ingrediente3_id])

# Configura la base de datos
engine = create_engine('sqlite:///heladeria.db')  # Puedes cambiar a otra base de datos si lo deseas
Base.metadata.create_all(engine)
