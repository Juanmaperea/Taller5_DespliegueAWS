from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .controllers import student_controller

# Crear tablas (solo para desarrollo)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student CRUD API (MVC)")

# ✅ Middleware CORS
origins = [
    "http://localhost:8080",      # para desarrollo local
    "http://127.0.0.1:8080",      # otra forma local
    "http://18.215.163.57",       # acceso directo por IP pública (HTTP)
    "https://18.215.163.57",      # si luego activas HTTPS con Nginx o certbot
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],         # permitir todos los métodos (GET, POST, PUT, DELETE)
    allow_headers=["*"],         # permitir todos los headers
)

# Rutas
app.include_router(student_controller.router)
