from utils import get_path
from grade_manager import GradeManager
# 🎭 ECA Manager
class ECAManager:
    def add_eca(self):
        student_id = input("Enter Student ID: ")
        activities = input("Enter ECA activities (comma-separated): ")
        with open(get_path("eca.txt"), "a") as f:
            f.write(f"{student_id},{activities}\n")
        print("✅ ECA added.")

    def update_eca(self):
        student_id = input("Enter Student ID to update ECA: ")
        new_activities = input("Enter new ECA activities (comma-separated): ")
        file_path = get_path("eca.txt")
        if not os.path.exists(file_path):
            print("eca.txt not found.")
            return
        updated = False
        lines = []
        with open(file_path, "r") as f:
            for line in f:
                if line.startswith(student_id + ","):
                    lines.append(f"{student_id},{new_activities}\n")
                    updated = True
                else:
                    lines.append(line)
        with open(file_path, "w") as f:
            f.writelines(lines)
        print("✅ ECA updated." if updated else "❌ Student ID not found.")

    def delete_eca(self):
        student_id = input("Enter Student ID to delete ECA: ")
        file_path = get_path("eca.txt")
        if not os.path.exists(file_path):
            print("eca.txt not found.")
            return
        lines = []
        deleted = False
        with open(file_path, "r") as f:
            for line in f:
                if not line.startswith(student_id + ","):
                    lines.append(line)
                else:
                    deleted = True
        with open(file_path, "w") as f:
            f.writelines(lines)
        print("✅ ECA deleted." if deleted else "❌ Student ID not found.")

    def view_eca_for(self, student_id):
        try:
            with open(get_path("eca.txt"), "r") as f:
                for line in f:
                    if line.startswith(student_id + ","):
                        activities = line.strip().split(",")[1:]
                        print("ECA:", ", ".join(activities))
                        return
            print("ECA not found.")
        except:
            print("eca.txt not found.")

# 👤 User Models
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
