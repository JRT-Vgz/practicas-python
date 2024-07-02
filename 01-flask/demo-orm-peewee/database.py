
from os import environ
from peewee import MySQLDatabase, Model, TextField, DateTimeField, IntegerField, ForeignKeyField, CharField
import datetime

# --- BASE DE DATOS ---
db = MySQLDatabase(
    environ.get("DB_NAME"),
    user=environ.get("DB_USER"),
    password=environ.get("DB_PASSWORD"),
    port=int(environ.get("DB_PORT")),
    host=environ.get("DB_HOST"),
)

# ---TABLA USERS ---
class User(Model):  
    username = CharField()
    password = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        db_table = "users"
    
    @classmethod
    def create_user(cls, _username, _password):
        _password = "cody_" + _password
        return User.create(username=_username, password=_password)
    

# --- TABLA PRODUCTS ---
class Product(Model):  
    name = TextField()
    price = IntegerField()
    user = ForeignKeyField(User, backref="products")
    created_at = DateTimeField(default=datetime.datetime.now)
    
    @property
    def price_format(self):
        return f"$ {self.price} dollars"
    
    class Meta:
        database = db
        db_table = "products"


# CREAR LAS TABLAS.
db.create_tables([User, Product])