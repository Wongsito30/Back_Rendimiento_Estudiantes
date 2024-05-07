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


def get_pregunta():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()

@router.get("/")
async def Main():
    return RedirectResponse(url="/docs/")

@router.get("/verPregunta/", response_model=List[page_schemas.preguntas])
async def show_preguntas(db:session=Depends(get_pregunta)):
    pregunta = db.query(page_models.Preguntas).all()
    return pregunta

@router.post("/registrarPreguntas/",response_model=page_schemas.preguntas)
def create_preguntas(entrada:page_schemas.preguntas,db:session=Depends(get_pregunta)):
   pregunta = page_models.Preguntas(id_cuestionario = entrada.id_cuestionario, pregunta = entrada.pregunta, tipo = entrada.tipo)
   db.add(pregunta)
   db.commit()
   db.refresh(pregunta)
   return pregunta

@router.put("/Cambiarpreguntatodo/{pregunta_id}",response_model=page_schemas.preguntas)
def mod_pregunta(preguntaid: int, entrada:page_schemas.preguntas,db:session=Depends(get_pregunta)):
    pregunta = db.query(page_models.Preguntas).filter_by(id=preguntaid).first()
    pregunta.id_cuestionario = entrada.id_cuestionario
    pregunta.pregunta = entrada.pregunta
    pregunta.tipo = entrada.tipo
    db.commit()
    db.refresh(pregunta)
    return pregunta

@router.put("/Cambiarpregunta/{pregunta_id}",response_model=page_schemas.Cambiarpreguntas)
def mod_Pregunta(preguntaid: int, entrada:page_schemas.Cambiarpreguntas,db:session=Depends(get_pregunta)):
    pregunta = db.query(page_models.Preguntas).filter_by(id=preguntaid).first()
    pregunta.pregunta = entrada.pregunta
    db.commit()
    db.refresh(pregunta)
    return pregunta

@router.delete("/EliminarPregunta/{pregunta_id}",response_model=page_schemas.respuesta)
def del_pregunta(preguntaid: int,db:session=Depends(get_pregunta)):
    pregunta = db.query(page_models.Preguntas).filter_by(id=preguntaid).first()
    db.delete(pregunta)
    db.commit()
    respuesta = page_schemas.respuesta(mensaje="Eliminado exitosamente")
    return respuesta