import os

SECRET_KEY = 'supersecreto'

PRODUCTS_FILE = os.path.join("data", "products.json")
SESSION_TYPE = "filesystem"  # Debe ser un string válido

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)