from modules import user, auth, database, utils
from services import email_service, data_processor
import config.settings

def main():
    print("Starting Test Bench Application"

    user_name = input("Enter your username: ")
    user_password = input("Enter your password: ")

    if auth.authenticate(user_name, user_password):
        print("Authentication successful")
    else:
        print("Authentication failed")

    data = data_processor.process_data("Some input data")
    print("Processed Data:", data)

    email_service.send_email(user_name, "Test Subject", "Test Body")

    db_result = database.query_user(user_name)
    print("Database Result:", db_result)

if __name__ == "__main__":
    main()
