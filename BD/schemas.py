from pydantic import BaseModel
from typing import Optional
from datetime import date

class User(BaseModel):
     id: Optional[int] = None
     nickname: str
     correo: str
     contrasena: str
     resultados: Optional[str] = None
     codigo: int

     class Config:
       from_attributes = True

class Admin(BaseModel):
     id: Optional[int] = None
     nickname: str
     contrasena: str

     class Config:
       from_attributes = True

class ModificarUsernameAdmin(BaseModel):
     nickname: str

     class Config:
       from_attributes = True

class ModificarPassWordAdmin(BaseModel):
     contrasena: str

     class Config:
       from_attributes = True

class RegisterUser(BaseModel):
     id: Optional[int] = None
     nickname: str
     correo: str
     contrasena: str
     codigo: int

     class Config:
       from_attributes = True

class ModificarUser(BaseModel):
     id: Optional[int] = None
     nickname: str
     correo: str

     class Config:
       from_attributes = True

class Modificarcontrasena(BaseModel):
     contrasena: str

     class Config:
       from_attributes = True

class cuestionario(BaseModel):
     id: Optional[int] = None
     preguntas: str
     descripcion: str

     class Config:
       from_attributes = True

class cuestionarioPreguntas(BaseModel):
     preguntas: str

     class Config:
       from_attributes = True       

class respuestas(BaseModel):
     id: Optional[int] = None
     id_cuestionario: int
     id_pregunta: int
     nickname: str
     respuesta: str

     class Config:
         from_attributes = True

class cambiarRespuestas(BaseModel):
     respuesta: str

     class Config:
         from_attributes = True

class preguntas(BaseModel):
     id: Optional[int] = None
     id_cuestionario: int
     pregunta: str
     tipo: str

     class Config:
       from_attributes = True

class Cambiarpreguntas(BaseModel):
     pregunta: str


     class Config:
       from_attributes = True
       
class respuesta(BaseModel):
     mensaje: str