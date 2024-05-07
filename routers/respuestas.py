from fastapi import APIRouter,HTTPException
from typing import List
from starlette.responses import RedirectResponse
from sqlalchemy.orm import session
from fastapi.params import Depends
from BD.Connn import engine, sessionlocal
import BD.schemas as page_schemas
import BD.Connn as page_conexion
import BD.modelos as page_models

page_models.Base.metadata.create_all(bind=engine)
router = APIRouter()


def get_respuestas():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()

@router.get("/")
async def Main():
    return RedirectResponse(url="/docs/")

@router.get("/verRespuestas/", response_model=List[page_schemas.respuestas])
async def show_Respuestas(db:session=Depends(get_respuestas)):
    respuesta = db.query(page_models.Respuestas).all()
    return respuesta

@router.post("/registrarRespuestas/",response_model=page_schemas.respuestas)
def create_respuestas(entrada:page_schemas.respuestas,db:session=Depends(get_respuestas)):
   respuestas = page_models.Respuestas(id_cuestionario = entrada.id_cuestionario, id_pregunta = entrada.id_pregunta, nickname = entrada.nickname, respuesta = entrada.respuesta)
   db.add(respuestas)
   db.commit()
   db.refresh(respuestas)
   return respuestas

@router.put("/CambiarRespuestas/{Respuesta_id}",response_model=page_schemas.respuestas)
def mod_respuestas(respuestasid: int, entrada:page_schemas.respuestas,db:session=Depends(get_respuestas)):
    respuestas = db.query(page_models.Respuestas).filter_by(id=respuestasid).first()
    respuestas.id_cuestionario = entrada.id_cuestionario 
    respuestas.id_pregunta = entrada.id_pregunta
    respuestas.nickname = entrada.nickname
    respuestas.respuesta = entrada.respuesta
    db.commit()
    db.refresh(respuestas)
    return respuestas

@router.put("/CambiarRespuesta/{Id_respuesta}",response_model=page_schemas.cambiarRespuestas)
def mod_RespuestasUsuario(idrespuesta: int, entrada:page_schemas.cambiarRespuestas,db:session=Depends(get_respuestas)):
    respuestas = db.query(page_models.Respuestas).filter_by(id=idrespuesta).first()
    respuestas.respuesta = entrada.respuesta
    db.commit()
    db.refresh(respuestas)
    return respuestas

@router.delete("/EliminarRespuestas/{respuestas_id}",response_model=page_schemas.respuesta)
def del_respuestas(respuestasid: int,db:session=Depends(get_respuestas)):
    respuestas = db.query(page_models.Respuestas).filter_by(id=respuestasid).first()
    db.delete(respuestas)
    db.commit()
    respuesta = page_schemas.respuesta(mensaje="Eliminado exitosamente")
    return respuesta