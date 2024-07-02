
""" 
----------------------------CREAR UNA BASE DE DATOS LOCAL EN MONGO Y USARLA. ----------------------------
El ejercicio que haremos es utilizar las operaciones de "users.py" GET, POST, PUT y DELETE en una base de datos.
Cogeremos la base de datos fictícea que hicimos allí y la desplegaremos en MongoDB, para poder interactuar con estos datos.
Duplicamos el archivo "users.py" y lo llamamos "usersdb".py, que es con el que trabajaremos este ejemplo, para no perder el otro.
"""

from pymongo import MongoClient

# Base de datos local.
#db_client = MongoClient().local

# Base de datos remota.
db_client = MongoClient("mongodb+srv://jrtvgz:3763201vargath@vargath.7thojgg.mongodb.net/").vargath






