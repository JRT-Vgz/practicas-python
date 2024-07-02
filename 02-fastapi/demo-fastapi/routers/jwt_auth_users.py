
# API DE USUARIOS AUTENTIFICADA DE CON TOKEN ENCRIPTADO JWT.

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

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
   
   
# --- OPERACIONES ---

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code = 400, detail = "El usuario no existe en la base de datos.")
    
    user = search_user_db(form.username)
    
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code = 400, detail = "La contraseña no es correcta.")

    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_DURATION)   
    access_token = {
        "sub": user.username,
        "exp": expire   
    }   
    return {"access_token": jwt.encode(access_token, SECRET, algorithm = ALGORITHM), "token_type": "jwt"}  
    
        
def search_user(username: str):
   if username in users_db:
       return User(**users_db[username])


async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED, 
            detail = "Credenciales de autenticación inválidas.", 
            headers = {"WWW-Authenticate": "JWT"})
    
    try:
        username = jwt.decode(token, SECRET, algorithms = [ALGORITHM]).get("sub")       
        if username is None:
            raise exception  
        return search_user(username)   
    except JWTError:
        raise exception  
    

async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail = "Usuario inactivo.")
    return user


@router.get("/users/me") 
async def me(user: User = Depends(current_user)):
    return user



