
from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)

app.secret_key = "kjdhgfkjhsdfkhjsadfkjhjkh"

# -------------------- DECORADORES --------------------

# Decorador para comprobar si el usuario está logeado antes de ejecutar la función.
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for("login"))
    return wrap



# --------------------- ENDPOINTS ---------------------

# Generar una ruta.
@app.route("/")
@login_required
def home():
    return render_template("index.html")

# Generar una ruta que devuelva un template.
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

# Generar un login.
@app.route("/login", methods = ["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "admin":
            error = "Invalid Credentials. Please try again."
        else:
            session["logged_in"] = True
            flash("You were logged in.")
            return redirect(url_for("home"))
    return render_template("login.html", error = error)
        
#  Generar un logout.
@app.route("/logout")
@login_required
def logout():
    session.pop("logged_in", None)
    flash("You logged out.")
    return redirect(url_for("welcome"))



if __name__ == "__main__":
    app.run(debug=True)