
"""
----------------------------EJEMPLO DE CREAR UN PEQUEÑO API SENCILLO PARA USUARIOS ----------------------------
- Primer ejercicio hecho en el archivo "users.py"
- Retocamos este archivo para dejar solo las peticiones básicas GET, POST, PUT y DELETE.
- Retocamos el router para ponerle un prefijo y simplificar los endpoints.
- Retoca este archivo para poder utilizarse con la base de datos real.
"""

from fastapi import APIRouter, HTTPException, status
# Importamos la clase user que hemos creado en la zona de la base de datos.
from db.models.user import User
# Importamos el cliente de base de datos.
from db.client import db_client
# Importamos el schema.
from db.schemas.user import user_schema, users_schema
# Importamos la clase que representa el Object ID en las bases de dato Mongo, para poder buscar por ID
from bson import ObjectId

router = APIRouter(prefix="/userdb", 
                   tags = ["userdb"],
                   responses = {status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


# -------------------------------------------------------
# ----------------- FUNCION DE BUSQUEDA -----------------
# -------------------------------------------------------
def search_user_by_field(field: str, key: str):
    try:
        user = user_schema(db_client.users.find_one({field: key}))
        return User(**user)
    except:
        return {"error": "No se ha encontrado el usuario."}
   
# -------------------------------------------------------
# --------------------- OPERACIONES ---------------------
# -------------------------------------------------------

@router.get("/", response_model = list[User])
async def users():
    users_dict = users_schema(db_client.users.find())
    users_list = [User(**user) for user in users_dict]
    return users_list
# PETICION: http://127.0.0.1:8000/userdb


@router.get("/{id}")
async def user_by_id(id: str):
    return search_user_by_field("_id", ObjectId(id))
# PETICION: http://127.0.0.1:8000/userdb/id


@router.post("/", status_code = status.HTTP_201_CREATED, response_model = User) 
async def add_user(user: User):
    if type(search_user_by_field("username", user.username)) == User:
        raise HTTPException(status_code = status.HTTP_204_NO_CONTENT, detail = "El usuario ya existe")
    
    # Transformamos al user en un diccionario, que es lo que tiene que recibir nuestra base de datos.
    # Borramos el campo ID del user que nos llega, para que solo inserte el username y el email. No queremos que inserte en la base de datos un valor Null en el ID.
    # El ID lo autogenera MongoDB.
    user_dict = dict(user)
    del user_dict["id"]
    
    id = db_client.users.insert_one(user_dict).inserted_id

    # Con lo de arriba ya insertaría al usuario. Ahora vamos a validar que el ID existe para returnear al user con su nuevo ID que Mongo le ha asignado y que quede todo bien bonito.
    # El nombre de la clave única que crea Mongo para el ID es "_id".
    new_user = db_client.users.find_one({"_id": id})
    
    # Lo que nos vuelve de la base de datos es un JSON Tenemos que volver a transformarlo en una instancia de la clase User que utilizamos en fastapi, para devolverla.
    # Para eso usaremos un schema que transforme el JSON a una representación de nuestro Usuario.

    new_user = user_schema(new_user)
    
    # Ya podemos returnear una instancia de la clase User compatible con nuestro sistema. Y ya hemos introducido unos datos en la base de datos
    # compatibles con la base de datos.
    return User(**new_user)

# PETICION: http://127.0.0.1:8000/userdb
# Añadir: {"username": "jrtvgz", "email": "jrtvgz@gmail.com"} 


@router.put("/", response_model=User)
async def act_user(user: User):
    try:
        user_dict = dict(user)
        del user_dict["id"]
        db_client.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
        return search_user_by_field("_id", ObjectId(user.id))
    except:
        return {"error": "No se ha actualizado el usuario."}
# PETICION: http://127.0.0.1:8000/userdb
# Añadir: Un User entero conseguido desde el GET, cambiandole lo que sea menos la ID.
    

@router.delete("/{id}")
async def delete_user_by_id(id: str): 
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        return {"error": "El usuario no existe."}
    return {"success": "User deleted"}
# PETICION: http://127.0.0.1:8000/userdb/id
    