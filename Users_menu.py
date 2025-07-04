def admin_menu(admin):
    """
    Displays the admin menu and handles admin actions
    like managing users, grades, ECAs, and average grades.
    """
    while True:
        print("\n1. User Management\n2. Grade Management\n3. ECA Management\n4. View Average Grades\n5. Logout")
        section = input("Choose: ")
        if section == "1":
            print("\n-- User Management --")
            print("1. Add User\n2. Delete User")
            choice = input("Choose: ")
            if choice == "1": admin.add_user()
            elif choice == "2": admin.delete_user()
        elif section == "2":
            print("\n-- Grade Management --")
            print("1. Add Grade\n2. Update Grade\n3. Delete Grade")
            choice = input("Choose: ")
            if choice == "1": admin.add_grade()
            elif choice == "2": admin.update_grade()
            elif choice == "3": admin.delete_grade()
        elif section == "3":
            print("\n-- ECA Management --")
            print("1. Add ECA\n2. Update ECA\n3. Delete ECA")
            choice = input("Choose: ")
            if choice == "1": admin.add_eca()
            elif choice == "2": admin.update_eca()
            elif choice == "3": admin.delete_eca()
        elif section == "4":
            admin.show_average_grades()
        elif section == "5":
            break
        else:
            print("Invalid option.")

def student_menu(student):
    while True:
        print("\n1. View Profile\n2. View Grades\n3. View ECA\n4. Logout")
        choice = input("Choose: ")
        if choice == "1": student.view_profile()
        elif choice == "2": student.view_grades()
        elif choice == "3": student.view_eca()
        elif choice == "4": break
        else: print("Invalid choice.")

