from sqlalchemy import Column, Integer, String, LargeBinary, Float, Date
from sqlalchemy.dialects.mysql import LONGTEXT
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

class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(50))
    contrasena =  Column(String(1000))

class Cuestionarios(Base):
    __tablename__ = 'cuestionarios'

    id = Column(Integer, primary_key=True, index=True)
    preguntas = Column(LONGTEXT)
    descripcion = Column(String(500))

class Preguntas(Base):
    __tablename__ = 'preguntas'

    id = Column(Integer, primary_key=True, index=True)
    id_cuestionario = Column(Integer)
    pregunta = Column(String(500))
    tipo = Column(String(150))

class Respuestas(Base):
    __tablename__ = 'respuestas'

    id = Column(Integer, primary_key=True, index=True)
    id_cuestionario = Column(Integer)
    id_pregunta = Column(Integer)
    nickname = Column(String(50))
    respuesta = Column(String(500))
    
    