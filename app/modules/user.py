def create_user(username, password):
    if not username or not password:
        return False
    return True

def delete_user(username):
    print(f"User {username} deleted.")
    return True
