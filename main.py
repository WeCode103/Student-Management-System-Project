'''1.The utils import get path to store .txt documents in data folder 
it is used for cross machine dir compability while running programs to prevent file not found error and 
any others..
2.user_models file imports the Student, Admin classes and their logics.
grade_manager file imports the code to handle CRUD operation of grades in GradeManager Class.
3.eca_manager file imports the code to handle CRUD operation of Extra Curriculumn Activities in ECAManager
class.
login_system file imports the login() of respective roles like admin or student..
4.Users_menu file imports the menu of admin and student wiht the information management features.

 '''
import os
from utils import get_path
from user_models import Student, Admin
from grade_manager import GradeManager
from eca_manager import ECAManager
from login_system import login
from Users_menu import admin_menu, student_menu


def main():
    while True:
        print("\nWelcome to the Student Management System")
        print("1. Admin\n2. Student\n3. Exit")
        choice = input("Choose (1/2/3): ").strip()
        if choice == "1": expected_role = "admin"
        elif choice == "2": expected_role = "student"
        elif choice == "3": print("Thanks for using the system. Bye!"); break
        else: print("Invalid choice."); continue

        login_result = login(expected_role)
        if login_result is None:
            continue
        role, user_id, name = login_result
        if role == "admin": admin_menu(Admin(user_id, name))
        elif role == "student": student_menu(Student(user_id, name))  
if __name__=="__main__":
   main()
