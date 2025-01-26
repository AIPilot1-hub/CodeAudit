import sqlite3

def query_user(username):
    conn = sqlite3.connect("app/config/settings.py")  # Logical flaw: incorrect DB file
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "';"  # SQL Injection vulnerability
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def insert_user(username, password):
    conn = sqlite3.connect("app/config/settings.py")  # Logical flaw: incorrect DB file
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}');")  # SQL Injection
    conn.commit()
    conn.close()
    return True
