USERS = {
    "admin": {"password": "1234", "role": "Admin"},
    "sales": {"password": "1111", "role": "Sales"},
    "finance": {"password": "2222", "role": "Finance"},
    "ops": {"password": "3333", "role": "Operations"}
}

def authenticate(username, password):
    if username in USERS and USERS[username]["password"] == password:
        return USERS[username]["role"]
    return None