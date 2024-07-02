
from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, usersdb
from fastapi.staticfiles import StaticFiles

# --- CONFIGURACION DE LA API Y LOS ROUTERS ---
# Instancia principal.
app = FastAPI()
# Routers:
app.include_router(products.router)
#app.include_router(users.router)
app.include_router(usersdb.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

#Archivos estáticos:
app.mount("/static", StaticFiles(directory = "static"), name = "static")

# --- OPERACIONES ---
# Operación con endpoint en la raiz:
@app.get("/")
async def root():
    return "Hola FastAPI"
# Explicación: Si hacemos una petición GET a la IP sin más, lanza la función raíz, que se representa en el código con una "/". 
# La función la hemos llamado root y returnea "Hola FastAPI"


# Operación con endpoint en la url:
@app.get("/url")
async def url_curso_backend():
    return {"url_curso": "htpps://mouredev.com/python"}
# Explicación: Si hacemos una petición a la IP + /url, se dispara esta función.


# Inicia el server: uvicorn main:app --reload


# Documentacion: http://127.0.0.1:8000/docs
# Documentacion: http://127.0.0.1:8000.redoc



