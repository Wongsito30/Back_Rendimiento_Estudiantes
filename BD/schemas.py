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

class respuesta(BaseModel):
     mensaje: str