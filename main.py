from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import login
from routers import registerUser

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(login.router)
app.include_router(registerUser.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}