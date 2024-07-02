
# API DE USUARIOS AUTENTIFICADA DE CON TOKEN ENCRIPTADO JWT.

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

# Constantes: El algoritmo de encriptació n
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "QWCPOM dfohgoigfoisahdgfoisoiufgasoiugfhas lkjsahgfkjasgfoasyfgoiasufgoashloijawpod`pwof"

router = APIRouter(prefix="/jwt_auth", 
                   tags = ["jwt_auth"],
                   responses = {status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl = "/login")

crypt = CryptContext(schemes =["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str
    
users_db = {
    "jrtvgz": {
        "username": "jrtvgz",
        "full_name": "Javier Rojo Tortajada",
        "email": "jrtvgz@gmail.com",
        "disabled": False,
        "password": "$2a$12$0aEMVdfVvcPdBCydCytoz.cDa8KNuIiK5TcNmUikiUIUrws2Njinu"
    },
    "user2": {
        "username": "user2",
        "full_name": "Usuario 2",
        "email": "user2@gmail.com",
        "disabled": True,
        "password": "$2a$12$NyKKeIpcfY2pp803K2LAJu45YpDVOLg8cCPowQDWd1H4l3EhpRmUO"
    }
}    

def search_user_db(username: str):
   if username in users_db:
       return UserDB(**users_db[username])
   
# El RequestForm es igual que en el básico, la forma de buscar el usuario será también igual.  
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code = 400, detail = "El usuario no existe en la base de datos.")
    
    user = search_user_db(form.username)
    
    # Antes de comparar las contraseñas, tenemos que encriptar la que hemos recibido y compararla con la de la base de datos.
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code = 400, detail = "La contraseña no es correcta.")

    # Creamos una variable que será la hora actual en la que se genere el token y le sumamos el tiempo que queremos que dure el token.
    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_DURATION)
    
    # --- CREAMOS EL ACCESS TOKEN: Nombre de Usuario, Fecha de expiración del token ---
    access_token = {
        "sub": user.username,
        "exp": expire   
    }
    
    # Antes de returnear, encriptamos el token con la libreria "jwt" y utilizamos tambien el algoritmo de encriptación.
    return {"access_token": jwt.encode(access_token, SECRET, algorithm = ALGORITHM), "token_type": "jwt"}  
    
    
    
    
def search_user(username: str):
   if username in users_db:
       return User(**users_db[username])

# Para desencriptar el token, dividimos lo que hicimos en el básico en dos funciones, en vez de una.
# Creamos una nueva funcion que autentifique al user con el token y nos devuelva el user.
async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED, 
            detail = "Credenciales de autenticación inválidas.", 
            headers = {"WWW-Authenticate": "JWT"})
    
    # Hacemos un try a la decoficicación.
    try:
        username = jwt.decode(token, SECRET, algorithms = [ALGORITHM]).get("sub")       
        # En caso de que funcione, nos aseguramos que el nombre del usuario no es None.
        if username is None:
            raise exception  
        
        # Una vez tenemos el username, buscamos el user.
        return search_user(username)   
    except JWTError:
        raise exception  
    
# Función criterio de dependencia:
async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail = "Usuario inactivo.")
    return user

# Peticiones:

@router.get("/users/me") 
async def me(user: User = Depends(current_user)):
    return user

# TESTEO:
# 1. Si tratamos de hacer un GET a "/users/me" sin token, nos dice que no estamos autenticados.
# 2. Para poder hacer un POST "/login", tenemos que pasar tambien Form en el Body con las variables (username y password).
# 3. Pedir el GET "/users/me" pasandole un Auth Bearer con el nombre del token.


