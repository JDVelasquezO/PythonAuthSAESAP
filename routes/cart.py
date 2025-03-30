from flask import Blueprint, render_template, redirect, url_for, session, jsonify
from models.products import loadProducts

cart_bp = Blueprint("cart", __name__)

def getCart():
    # Obtiene el carrito o crea uno nuevo
    return session.get("cart", {})

def saveCart(cart):
    # Guarda el carrito en la sesion
    session["cart"] = cart
    session.modified = True

# Añadir un producto al carrito
@cart_bp.route("/add/<int:productId>", methods=["POST"])
def addToCart(productId):
    cart = getCart()
    products = loadProducts()

    product = next((p for p in products if p["id"] == productId), None)
    if not product:
        return jsonify({ "error": "Producto no encontrado" }), 404

    if str(productId) in (cart):
        # Añadimos producto repetido
        cart[str(productId)]["quantity"] += 1
    else:
        # Añadimos producto por primera vez
        cart[str(productId)] = {
            "name": product["name"],
            "price": product["price"],
            "quantity": 1,
            "picture": product["picture"]
        }

    saveCart(cart)
    return redirect(url_for("catalog.products"))

def getCartCount():
    cart = getCart()
    # item["quantity"] for item in cart.values()
    # 1. Recorremos los valores del cart
    # 2. Se recorren con la variable item
    # 3. Necesitamos el atributo quantity de item para obtener los valores
    """
        acum = 0
        for item in cart.values():
            acum += item[quantity]
        return acum
    """
    return sum(item["quantity"] for item in cart.values())

# Ver nuestro carrito de compras
@cart_bp.route("/cart")
def viewCart():
    cart = getCart()
    total = sum(item["price"] * item["quantity"] for item in cart.values())
    cartCount = getCartCount()
    return render_template("cart.html", cart=cart, total=total, cartCount=cartCount)