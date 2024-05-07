from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import login
from routers import registerUser
from routers import cuestionarios
from routers import preguntas
from routers import respuestas

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(login.router, tags=["Login"])
app.include_router(registerUser.router, tags=["RegisterUser"])
app.include_router(cuestionarios.router, tags=["Cuestionario"])
app.include_router(preguntas.router, tags=["Preguntas"])
app.include_router(respuestas.router, tags=["Respuestas"])


@app.get("/")
async def root():
    return {"message": "Hello World"}