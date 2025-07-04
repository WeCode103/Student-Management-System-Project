'''The utils import the directory for passwords.txt and users.txt
Inside function login While runs through the loop until the code inside try gets executed ..
The code inside try is executed only when the password and user id is matched from password.txt and when the user id is 
in file one is matched with user id in users.txt file the else inside try get executed if the user id of passwords.txt and users.txt does 
not match'''
from utils import get_path
def login(expected_role):
    while True:
        user_id = input("Enter your ID: ").strip()
        password = input("Enter your password: ").strip()
        try:
            with open(get_path("passwords.txt"), "r") as f:
                for line in f:
                    uid, pwd = line.strip().split(",")
                    if uid == user_id and pwd == password:
                        with open(get_path("users.txt"), "r") as f2:
                            for uline in f2:
                                parts = uline.strip().split(",")
                                if parts[0] == user_id:
                                    name, role = parts[1], parts[2]
                                    if role == expected_role:
                                        print(f"Login successful as {role}!")
                                        return role, user_id, name
                                    else:
                                        print(f"This user is not a {expected_role}.")
                        break
            print("Invalid credentials. Try again.")
        except Exception as e:
            print("Error during login:", e)
