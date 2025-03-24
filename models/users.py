import json
import os

# Ruta del archivo JSON
USERS_FILE = 'users.json'

# Función para cargar el archivo JSON
def loadUsers():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            return json.load(file) # Devuelve la lista de diccionarios (DB)
    return []

def getUserByCui(cui):
    users = loadUsers()
    '''
    for u in users:
        if u["cui"] == cui:
            return u
    return None
    '''
    return next((u for u in users if u["cui"] == cui), None)

def saveUsers(users):
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as file:
            json.dump(users, file, indent=4)

def registerUser(cui, name, email, password, bornDate, picture):
    users = loadUsers()
    if getUserByCui(cui): # Si devuelve None, no existe un usuario con CUI específico
        return False

    # Si todo va bien, continúa aquí:
    newUser = {
        "cui": cui,
        "name": name,
        "dateBorn": bornDate,
        "email": email,
        "password": password,
        "picture": picture
    }

    users.append(newUser)
    saveUsers(users)
    return True
