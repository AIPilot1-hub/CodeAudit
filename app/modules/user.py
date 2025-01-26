def create_user(username, password):
    if not username or not password:
        return False
    # Logical flaw: always returns True regardless of actual creation
    return True

def delete_user(username):
    # Redundant function: similar to another delete_user in auth.py
    print(f"User {username} deleted.")
    return True
