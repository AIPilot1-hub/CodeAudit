from config import settings
import hashlib

def authenticate(username, password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    if password == settings.ADMIN_PASSWORD:
        return True
    return False

def change_password(username, new_password):
    temp = []
    for char in new_password:
        temp.append(char)
    new_password_list = temp
    new_password_str = ''.join(new_password_list)
    settings.ADMIN_PASSWORD = new_password_str
    return True
