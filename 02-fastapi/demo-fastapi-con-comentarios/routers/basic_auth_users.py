
# API DE USUARIOS AUTENTIFICADA DE MANERA BÁSICA.

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/basic_auth", 
                   tags = ["basic_auth"],
                   responses = {status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

# Creamos una instancia de nuestro sistema de autenticación.
# Tenemos que pasarle como parámetro el endpoint en el que se va a realizar la autenticación.
oauth2 = OAuth2PasswordBearer(tokenUrl = "/login")

# Creamos al User.
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

# Creamos otra clase que herede el User y tiene la contraseña.
class UserDB(User):
    password: str
    
# Base de datos ficticea no relacional, que al final es como un JSON. 
users_db = {
    "jrtvgz": {
        "username": "jrtvgz",
        "full_name": "Javier Rojo Tortajada",
        "email": "jrtvgz@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    "user2": {
        "username": "user2",
        "full_name": "Usuario 2",
        "email": "user2@gmail.com",
        "disabled": True,
        "password": "654321"
    }
}

# Creamos una función que busque al usuario en la base de datos y returnee una instancia de la clase UserDB. Devuelve a ese usuario entero.
def search_user_db(username: str):
   if username in users_db:
       return UserDB(**users_db[username])
  
# Implementamos la operación de autenticación. Es un método POST a la url de nuestro sistema de autenticación.
# Parta rescatar las variables, hay muchas formas de recibir datos. Usamos OAuth2PasswordRequestForm.
# Lo capturamos en una variable y como valor por defecto le metemos la clase Depends(), que importamos de fastapi.
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    # Comprobamos si el username recibido en el formulario existe en nuestra base de datos.
    if not user_db:
        raise HTTPException(status_code = 400, detail = "El usuario no existe en la base de datos.")
    
    # Buscamos el usuario y comprobamos si la contraseña que nos ha llegado coincide con la del usuario de la base de datos.
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code = 400, detail = "La contraseña no es correcta.")
    
    # En el protocolo Auth2, en el momento en el que el usuario se autentifica, lo que debe devolver el sistema es un ACCESS TOKEN.
    # Devolvemos un JSON que por un lado da un access token y por otro dice de qué tipo es el token. En este caso, tipo bearer.ç
    # El token que devolvemos aqui es simplemente el nombre de usuario, para que sean más faciles los ejemplos siguientes. 
    # Pero en realidad nuestro token está encriptado para que el backend entienda lo que es, pero nadie más.
    return {"access_token": user.username, "token_type": "bearer"}
  
# El token permite que no tengamos que autenticarnos a cada cosa que hacemos, sino que da permisos temporales.
  
# Creamos funciones para utilizarlas una vez el usuario se ha autenticado. Por ejemplo un GET que me devuelva mi propia información. 
# Estas funciones tienen siempre criterios de dependencia, utilizando la clase Depends. Si no se cumple el criterio, la función falla.
# De esta forma, las funciones solo se ejecutan bien si la autenticación está hecha.

# Creamos una función que returnee una instancia del usuario pero de la clase User, no UserDB. Para que no esté la contraseña.
def search_user(username: str):
   if username in users_db:
       return User(**users_db[username])
   
# Función criterio de dependencia:
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED, 
            detail = "Credenciales de autenticación inválidas.", 
            headers = {"WWW-Authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail = "Usuario inactivo.")
    return user

# Peticiones:
# El criterio de dependencia es que lo que haya dentro del Depends sea True.
@router.get("/users/me") 
async def me(user: User = Depends(current_user)):
    return user
  
# La función no retornará un User si la dependencia "current_user" no le devuelve un usuario, y la dependencia lo devuelve o no basándose en los criterios de autenticación del token.
 
# TESTEO:
# 1. Si tratamos de hacer un GET a "/users/me" sin token, nos dice que no estamos autenticados.
# 2. Para poder hacer un POST "/login", tenemos que pasar tambien Form en el Body con las variables (username y password).
# 3. Pedir el GET "/users/me" pasandole un Auth Bearer con el nombre del token.
  
  
    