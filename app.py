from flask import Flask
from routes.auth import auth_bp
from routes.catalog import catalog_bp

app = Flask(__name__)
app.secret_key = 'supersecreto'

app.register_blueprint(auth_bp)
app.register_blueprint(catalog_bp)

if __name__ == '__main__':
    app.run(debug=True)
