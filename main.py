import os
import tkinter as tk
from gui import Application  # Import GUI
from utils import get_path
from user_models import Student, Admin
from grade_manager import GradeManager
from eca_manager import ECAManager
from login_system import login
from Users_menu import admin_menu, student_menu

def cli_main():
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

def main():
    print("Choose Interface:")
    print("1. Run CLI Menu")
    print("2. Run GUI App")
    choice = input("Select (1/2): ")

    if choice == "1":
        cli_main()
    elif choice == "2":
        root = tk.Tk()
        app = Application(root)
        root.mainloop()
    else:
        print("Invalid input. Exiting...")

if __name__ == "__main__":
    main()
