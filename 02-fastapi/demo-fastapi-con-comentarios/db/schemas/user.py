
# Tenemos que crear un schema que reciba un JSON de la base de datos y devuelva un JSON que coincida con nuestro objeto de modelo User.
# Al final, lo único que hace la operación es cambiarle el nombre a la clave ID, quitando el nombre de Mongo y poniendo el de nuestro Backend.
# user["_id"] sevolverá un objeto, que convertimos en string. 
def user_schema(user: dict):
    return {"id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"],
            }


# Schema para transformar una lista de los datos de toda la base en una lista de datos válida para nuestra clase User:
def users_schema(users: list):
    return [user_schema(user) for user in users]