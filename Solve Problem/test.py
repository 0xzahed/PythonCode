user_credentials = {
    "healthMin": "123health",
    "reliefkin": "456 relief",
    "FoodMin": "789food",
    "admin": "imadmin:123"
}

def validate_login(username, password):
    if username in user_credentials and user_credentials[username] == password:
        return True
    return False

def add_user(username, password):
    if username == "admin":
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")
        user_credentials[new_username] = new_password
        print("New user added successfully!")
    else:
        print("Access denied. Only admin can add new users.")

username = input("Enter username: ")
password = input("Enter password: ")

if validate_login(username, password):
    print("Login successful!")
    if username == "admin":
        add_user(username, password)
else:
    print("Invalid username or password.")
