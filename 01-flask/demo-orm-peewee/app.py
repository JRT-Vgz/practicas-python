
from os import environ
from flask import Flask, render_template, request, session, redirect, url_for
from database import User, Product
from functools import wraps

app = Flask(__name__)
app.secret_key = environ.get("SECRET_KEY")


# Decorador para comprobar si el usuario está registrado antes de ejecutar la función.
def register_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for("register"))
    return wrapper


# PAGINA PRINCIPAL.
@app.route("/")
def index():
    return render_template("index.html")


# REGISTRO:
@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username and password:
            user = User.create_user(username, password)
            session["user_id"] = user.id
            return redirect(url_for("products"))
    return render_template("register.html")


# LISTA DE PRODUCTOS POR USUARIO.
@app.route("/products")
@register_required
def products():
    user = User.get(session["user_id"])

    #Obtener los productos de la base de datos. Dos formas:
    #_products = Product.select().where(Product.user == user)
    _products = user.products
    return render_template("products/index.html", products=_products)


# AÑADIR PRODUCTO:
@app.route("/products/create", methods = ["POST", "GET"])
@register_required
def product_create():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        
        if name and price:
            user = session["user_id"]
            Product.create(name=name, price=price, user_id=user)
            return redirect(url_for("products"))
    return render_template("products/create.html")


# EDITAR PRODUCTO:
@app.route("/products/update/<id>", methods = ["GET", "POST"])
@register_required
def product_update(id: int):
    _product = Product.select().where(Product.id == id).first()
    
    if request.method == "POST":
        _product.name = request.form["name"]
        _product.price = request.form["price"]
        _product.save()
        return redirect(url_for("products"))
    return render_template("products/update.html", product = _product)


# BORRAR PRODUCTO:
@app.route("/products/delete/<id>", methods= ["GET", "DELETE"])
@register_required
def product_delete(id):
    if request.method == "GET":
        print(id)
        Product.delete().where(Product.id == id).execute()
        return redirect(url_for("products"))
    return "t"


    
