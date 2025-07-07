# 👤 User Models
from utils import get_path
from grade_manager import GradeManager
from eca_manager import ECAManager
class User:
    def __init__(self, user_id, name, role):
        self.id = user_id
        self.name = name
        self.role = role

    def view_profile(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Role:", self.role)

class Student(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, "student")

    def view_grades(self):
        GradeManager().view_grades_for(self.id)

    def view_eca(self):
        ECAManager().view_eca_for(self.id)
        
class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, "admin")

    def add_user(self):
        new_id = input("Enter new user ID: ")
        name = input("Enter user name: ")
        role = input("Enter role (admin/student): ")
        password = input("Enter password: ")
        with open(get_path("users.txt"), "a") as f:
            f.write(f"{new_id},{name},{role}\n")
        with open(get_path("passwords.txt"), "a") as f:
            f.write(f"{new_id},{password}\n")
        print("✅ User added successfully.")

    def delete_user(self):
        user_id = input("Enter ID to delete: ")
        for filename in ["users.txt", "passwords.txt", "grades.txt", "eca.txt"]:
            try:
                path = get_path(filename)
                with open(path, "r") as f:
                    lines = f.readlines()
                with open(path, "w") as f:
                    for line in lines:
                        if not line.startswith(user_id + ","):
                            f.write(line)
            except:
                print(f"⚠️ {filename} not found.")
        print("🗑️ User deleted from all records.")

    def add_grade(self):
     GradeManager().add_grade()
    def update_grade(self): 
     GradeManager().update_grade()
    def delete_grade(self): 
     GradeManager().delete_grade()
    def add_eca(self):
     ECAManager().add_eca()
    def update_eca(self):
     ECAManager().update_eca()
    def delete_eca(self): 
     ECAManager().delete_eca()
    def show_average_grades(self): 
     GradeManager().show_average_grades()
