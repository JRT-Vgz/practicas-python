
"""
----------------------------EJEMPLO DE CREAR UN PEQUEÑO API SENCILLO PARA USUARIOS ----------------------------
- Crear la clase User heredando de la clase BaseModel. Ponerle las variables.
- Crear una listra de usuarios ficticea (una lista de objetos).
- Crear las peticiones GET, POST, PUT y DELETE básicas para esa clase user.
- Testear todas las peticiones.
- Extra: Función avanzada filter para saber si un user.id ya se encuentra en la lista de usuarios.
- Extra: Ejemplos de peticiones GET pasando parámetros en el PATH y en el QUERY.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags = ["users"])

# 1. MODELAMOS UNA CLASE USER, HEREDANDO LA CLASE BASEMODEL.
# El BaseModel da la capacidad de crear una entidad solo poniendo los parámetros, sin tener que hacer la clase entera, su constructor, etc... y ya le da todos los metodos.
# FastAPI crea todas las autenticaciones de tipos de variable y automatiza todas las comprobaciones de si falta pasar alguna variable en la petición para crear el objeto.
# Podemos elegir si las variables sopn OPCIONALES. Por defecto son obligatorias.

class User(BaseModel):
    id : int
    name: str
    surname : str
    url : str
    age: int


# 2. CREAMOS UNA LISTA DE USUARIOS.
# La hacemos aqui a mano, pero los users de la lista son los que tendríamos en la base de datos.
User_1 = User(id = 1, name = "Javi", surname = "Vgz", url = "http://javivgz.com", age = 39)
User_2 = User(id = 2, name = "User2", surname = "sUser2", url = "http://user2.com", age = 39)
User_3 = User(id = 3, name = "User3", surname = "sUser3", url = "http://user3.com", age = 39)

users_list = [User_1, User_2, User_3]
  
# 3. HACEMOS LA PETICION GET SOBRE LA LISTA DE USUARIOS.  
# Peticion GET hecha con los usuarios escritos a mano.
# NO SE HACE ASI. Seria muy tedioso tener que construir el JSON a mano con diccionarios.
@router.get("/users_json")
async def users_json():
    return [
        {"id": 1, "name": "Javi", "surname": "Vgz", "url": "http://javivgz.com", "age": 39},
        {"id": 2,"name": "User2", "surname": "sUser2", "url": "http://user2.com", "age": 39},
        {"id": 3,"name": "User3", "surname": "sUser3", "url": "http://user3.com", "age": 39}  
    ]

# Para ello, la clase BaseModel ya hace esa transformación por nosotros.

# Si hacemos una petición GET a una lista con los objetos User de la base de datos, automáticamente, lo convierte a JSON cuando returnea.
@router.get("/users")
async def users():
    return users_list
# PETICION: http://127.0.0.1:8000/users

# -----------------------------------------------------------------------------------
# 4. PETICION GET CON PARAMETROS EN EL PATH
################ PARAMETROS EN EL PATH ################
# BUSCAR USER 1:
# Buscar Users por ID forma INTERMEDIA.
@router.get("/user_intermedio/{id}")
async def user_intermedio(id: int):
    for usuario in users_list:
        if usuario.id == id:
            return usuario
# PETICION: http://127.0.0.1:8000/user_intermedio/1


# BUSCAR USER 2:
# Buscar User por ID forma SUPER PRO. Teóricamente devolvería todos los users que tengan esa ID. Por eso luego pasamos el indice 0 (primer elemento). 
# En teoria la lista solo tendra un elemento.
@router.get("/user_pro/{id}")
async def user_pro(id: int):
    # El filtro devuelve un objeto filtro, que es como un diccionario de objetos. Por eso se enlista, aunque haya solo un elemento.
    usuarios = filter(lambda user: user.id == id, users_list)
    return list(usuarios)[0]
# PETICION: http://127.0.0.1:8000/user_pro/1
# PETICION QUE FALLA SI SE DA UN USER QUE NO EXISTE: http://127.0.0.1:8000/user_pro/6


# BUSCAR USER 3:
# Esto de arriba esta bien, pero estamos asumiendo que el usuario existe. Si pasamos una ID que no existe, dará un error 500 al estar vacia la lista.
# Tendremos que empezar a hacer comprobaciones.

@router.get("/user_pro_2/{id}")
async def user_pro_2(id: int):
    # El filtro devuelve un objeto filtro, que es como un diccionario de objetos. Por eso se enlista, aunque haya solo un elemento.
    usuarios = filter(lambda user: user.id == id, users_list)
    try:
        return list(usuarios)[0]
    except:
        return {"error": "No se ha encontrado el usuario."}
# PETICION: http://127.0.0.1:8000/user_pro_2/1
# PETICION SIN FALLO DE UN USER QUE NO EXISTE: http://127.0.0.1:8000/user_pro_2/6


# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# 5. PETICION GET CON UN PARAMETRO EN EL QUERY
################ PARAMETROS EN EL QUERY ################
@router.get("/user_query")
async def user_query(id: int):
    usuarios = filter(lambda user: user.id == id, users_list)
    try:
        return list(usuarios)[0]
    except:
        return {"error": "No se ha encontrado el usuario."}
# PETICION: http://127.0.0.1:8000/user_query/?id=1


 # 6. PETICION GET CON DOS PARAMETROS EN EL QUERY   
@router.get("/returnea_id_nombre")
async def returnea_id_nombre(id: int, nombre: str):
    return {"nombre": nombre, "id": id}
# PETICION: http://127.0.0.1:8000/returnea_id_nombre/?id=1&nombre=Javi
# -----------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# ------------------------- OPERACIONES POST, PUT Y DELETE --------------------------
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

# Funcion para buscar si un user existe en la lista.
def search_user(id: int):
    # El filtro devuelve un objeto filtro, que es como un diccionario de objetos. Por eso se enlista, aunque haya solo un elemento.
    usuarios = filter(lambda user: user.id == id, users_list)
    try:
        return list(usuarios)[0]
    except:
        return {"error": "No se ha encontrado el usuario."}
    
    
# ------------------------- POST --------------------------
# 7. PETICION POST PARA POSTEAR UN JSON COMO USER.
@router.post("/user/", status_code = 201, response_model = User) 
async def add_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code = 204)
    else:
        users_list.append(user)
        return user
# PETICION: http://127.0.0.1:8000/user
# Añadir: {"id": 4, "name": "User4", "surname": "sUser4", "url": "http://user4.com", "age": 39} 
# Ponerlo en el body de la petición, como un JSON.


# ------------------------- PUT --------------------------
# 8. PETICION POST PARA ACTUALIZAR UN USER ENTERO. RECIBE UN JSON CON TODOS LOS DATOS.
@router.put("/user/")
async def act_user(user: User):
    if type(search_user(user.id)) == User:
        for indice, usuario in enumerate(users_list):
            if usuario.id == user.id:
                users_list[indice] = user
                return user
    else:
        return {"error": "El usuario no existe."}
# PETICION: http://127.0.0.1:8000/user
# Añadir: {"id": 4, "name": "User666", "surname": "sUser4", "url": "http://user4.com", "age": 39} 
# Ponerlo en el body de la petición, como un JSON.   
    
    
# ------------------------- DELETE --------------------------
# 8. PETICION DELETE PARA BORRAR UN USER DE LA LISTA.
@router.delete("/user/{id}")
async def delete_user(id: int): 
    if type(search_user(id)) == User:
        for usuario in users_list:
            if usuario.id == id:
                users_list.remove(usuario)
                return {"success": "Usuario borrado."}
    else:
        return {"error": "El usuario no existe."}
# PETICION: http://127.0.0.1:8000/user/1
    







