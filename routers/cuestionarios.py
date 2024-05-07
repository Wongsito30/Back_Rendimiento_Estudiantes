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


def get_cuestionario():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()

@router.get("/")
async def Main():
    return RedirectResponse(url="/docs/")

@router.get("/verCuestionarios/", response_model=List[page_schemas.cuestionario])
async def show_Cuestionario(db:session=Depends(get_cuestionario)):
    cuestionario = db.query(page_models.Cuestionarios).all()
    return cuestionario

@router.post("/registrarCuestionario/",response_model=page_schemas.cuestionario)
def create_cuestionario(entrada:page_schemas.cuestionario,db:session=Depends(get_cuestionario)):
   cuestionario = page_models.Cuestionarios(preguntas = entrada.preguntas, descripcion = entrada.descripcion)
   db.add(cuestionario)
   db.commit()
   db.refresh(cuestionario)
   return cuestionario

@router.put("/CambiarCuestionario/{cuestionario_id}",response_model=page_schemas.cuestionario)
def mod_cuestionario(cuestionarioid: int, entrada:page_schemas.cuestionario,db:session=Depends(get_cuestionario)):
    cuestionario = db.query(page_models.Cuestionarios).filter_by(id=cuestionarioid).first()
    cuestionario.preguntas = entrada.preguntas
    cuestionario.descripcion = entrada.descripcion
    db.commit()
    db.refresh(cuestionario)
    return cuestionario

@router.put("/Cambiarpreguntas/{cuestionario_id}",response_model=page_schemas.cuestionarioPreguntas)
def mod_cuestionarioPreguntas(cuestionarioid: int, entrada:page_schemas.cuestionarioPreguntas,db:session=Depends(get_cuestionario)):
    preguntas = db.query(page_models.Cuestionarios).filter_by(id=cuestionarioid).first()
    preguntas.preguntas = entrada.preguntas
    db.commit()
    db.refresh(preguntas)
    return preguntas

@router.delete("/EliminarCuestionario/{cuestionario_id}",response_model=page_schemas.respuesta)
def del_cuestionario(cuestionarioid: int,db:session=Depends(get_cuestionario)):
    cuestionario = db.query(page_models.Cuestionarios).filter_by(id=cuestionarioid).first()
    db.delete(cuestionario)
    db.commit()
    respuesta = page_schemas.respuesta(mensaje="Eliminado exitosamente")
    return respuesta