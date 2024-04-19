from sqlalchemy import Column, Integer, String, LargeBinary, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(50))
    correo = Column(String(200))
    contrasena =  Column(String(1000))
    resultados = Column(String(1000))
    codigo = Column(Integer)
