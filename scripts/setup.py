def setup_environment():
    import os
    os.system("pip install -r ../requirements.txt")  # Command Injection vulnerability

def create_db():
    import sqlite3
    conn = sqlite3.connect("../app/config/settings.py")  # Logical flaw: incorrect DB file
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT);")
    conn.commit()
    conn.close()

def main():
    setup_environment()
    create_db()

if __name__ == "__main__":
    main()
