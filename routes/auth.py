# Importaciones necesarias
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.users import getUserByCui, registerUser
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        cui = request.form['cui']
        password = request.form['password']
        user = getUserByCui(cui)

        if user and user["password"] == password:
            session["cui"] = user["cui"]
            return redirect(url_for("catalog.products"))
        else:
            flash("Credenciales incorrectas, inténtalo de nuevo", "danger")

    return render_template('login.html')

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada correctamente", "success")
    return redirect(url_for("auth.login"))

@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        cui = request.form["cui"]
        name = request.form["name"]
        dateBorn = request.form["dateBorn"]
        email = request.form["email"]
        password = request.form["password"]
        picture = request.files["picture"]
        # print(picture.name)

        filename = None
        if picture:
            filename = secure_filename(picture.filename)
            picture.save(os.path.join(UPLOAD_FOLDER, filename))

        if registerUser(cui, name, email, password, dateBorn, filename):
            flash("Registro exitoso, puedes iniciar sesión", "success")
            return redirect(url_for("auth.login"))
        else:
            flash("El usuario ya existe", "danger")

    return render_template("registro.html")

@auth_bp.route("/home")
def home():
    cui = session.get("cui")
    if not cui:
        flash("Debes iniciar sesion", "danger")
        return redirect(url_for("auth.login"))
    
    # Obtenemos el usuario que se va a loggear
    user = getUserByCui(cui)

    if not user:
        flash("Usuario no encontrado", "danger")
        session.pop("cui", None)
        return redirect(url_for('auth.login'))

    return render_template("home.html", user=user, session=session)


