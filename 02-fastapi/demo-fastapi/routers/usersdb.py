

from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_schema
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

    user_dict = dict(user)
    del user_dict["id"]
    
    id = db_client.users.insert_one(user_dict).inserted_id
    
    new_user = db_client.users.find_one({"_id": id})
    new_user = user_schema(new_user)
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
    