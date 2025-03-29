from flask import Blueprint, render_template, redirect, url_for, session
from models.products import loadProducts

catalog_bp = Blueprint("catalog", __name__)

@catalog_bp.route("/catalog")
def products():
    if "cui" not in session:
        return redirect(url_for("auth.login"))
    
    products = loadProducts()
    return render_template("catalog.html", products=products)