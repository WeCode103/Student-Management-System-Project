from utils import get_path
import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt 

class User:
    def __init__(self, user_id, name, role):
        self.id = user_id
        self.name = name
        self.role = role

    def view_profile(self):
        return f"ID: {self.id}\nName: {self.name}\nRole: {self.role}"

class Student(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, "student")

    def view_grades(self):
        try:
            with open(get_path("grades.txt"), "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    if data[0] == self.id:
                        return data[1:]
            return []
        except:
            return []

    def view_eca(self):
        try:
            with open(get_path("eca.txt"), "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    if data[0] == self.id:
                        return data[1:]
            return []
        except:
            return []

    def update_password(self):
        try:
            new_pwd = simpledialog.askstring("Password Update", "Enter new password:")
            self.update_file_with_blank_handling(get_path("passwords.txt"), f"{self.id},{new_pwd}", self.id)
        except:
            messagebox.showerror("Error", "passwords.txt not found")

    def update_file_with_blank_handling(self, filename, new_data, match_id):
        with open(filename, "r") as f:
            lines = f.readlines()
        updated = False
        with open(filename, "w") as f:
            for line in lines:
                if line.strip().startswith(match_id + ","):
                    f.write(new_data + "\n")
                    updated = True
                elif line.strip() == "" and not updated:
                    f.write(new_data + "\n")
                    updated = True
                else:
                    f.write(line)
            if not updated:
                if lines and lines[-1].strip() != "":
                    f.write("\n")
                f.write(new_data + "\n")

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, "admin")

    def show_average_grades(self):
        try:
            with open(get_path("grades.txt"), "r") as f:
                subject_totals = [0] * 5
                count = 0
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) >= 6:
                        grades = list(map(int, parts[1:]))
                        for i in range(5):
                            subject_totals[i] += grades[i]
                        count += 1
                return [total / count for total in subject_totals] if count else []
        except:
            return []

    def identify_low_performers(self, threshold=40):
        try:
            with open(get_path("grades.txt"), "r") as f:
                alerts = []
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) >= 6:
                        grades = list(map(int, parts[1:]))
                        avg = sum(grades) / len(grades)
                        if avg < threshold:
                            alerts.append((parts[0], avg))
                return alerts
        except:
            return []

    def eca_participation(self):
        try:
            counts = {}
            with open(get_path("eca.txt"), "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0]:
                        counts[parts[0]] = len(parts) - 1
            return counts
        except:
            return {}

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Student/Admin System")
        self.login_screen()

    def login_screen(self):
        self.clear()
        tk.Label(self.root, text="Login", font=("Arial", 20)).pack()
        tk.Label(self.root, text="User ID").pack()
        self.user_id = tk.Entry(self.root)
        self.user_id.pack()
        tk.Label(self.root, text="Password").pack()
        self.password = tk.Entry(self.root, show="*")
        self.password.pack()
        tk.Label(self.root, text="Role").pack()
        self.role = tk.StringVar(value="student")
        tk.Radiobutton(self.root, text="Student", variable=self.role, value="student").pack()
        tk.Radiobutton(self.root, text="Admin", variable=self.role, value="admin").pack()
        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        uid = self.user_id.get()
        pwd = self.password.get()
        role = self.role.get()
        try:
            with open(get_path("passwords.txt"), "r") as f:
                for line in f:
                    stored_uid, stored_pwd = line.strip().split(",")
                    if stored_uid == uid and stored_pwd == pwd:
                        with open(get_path("users.txt"),"r") as uf:
                            for uline in uf:
                                parts = uline.strip().split(",")
                                if parts[0] == uid:
                                    name, actual_role = parts[1], parts[2]
                                    if actual_role == role:
                                        if role == "admin":
                                            self.admin = Admin(uid, name)
                                            self.admin_screen()
                                        else:
                                            self.student = Student(uid, name)
                                            self.student_screen()
                                        return
                                    else:
                                        messagebox.showerror("Role Error", "Incorrect role selected.")
                                        return
            messagebox.showerror("Login Failed", "Invalid credentials.")
        except:
            messagebox.showerror("Error", "Files not found.")

    def student_screen(self):
        self.clear()
        tk.Label(self.root, text=f"Welcome {self.student.name} (Student)", font=("Arial", 16)).pack()
        tk.Button(self.root, text="View Profile", command=self.view_profile).pack(pady=2)
        tk.Button(self.root, text="View Grades", command=self.view_grades).pack(pady=2)
        tk.Button(self.root, text="View ECA", command=self.view_eca).pack(pady=2)
        tk.Button(self.root, text="Update Password", command=self.student.update_password).pack(pady=2)
        tk.Button(self.root, text="Logout", command=self.login_screen).pack(pady=5)

    def admin_screen(self):
        self.clear()
        tk.Label(self.root, text=f"Welcome {self.admin.name} (Admin)", font=("Arial", 16)).pack()
        tk.Button(self.root, text="Performance Dashboard", command=self.performance_dashboard).pack(pady=2)
        tk.Button(self.root, text="Logout", command=self.login_screen).pack(pady=5)

    def view_profile(self):
        messagebox.showinfo("Profile", self.student.view_profile())

    def view_grades(self):
        grades = self.student.view_grades()
        messagebox.showinfo("Grades", ", ".join(grades) if grades else "No grades found.")

    def view_eca(self):
        eca = self.student.view_eca()
        messagebox.showinfo("ECA", ", ".join(eca) if eca else "No ECA activities found.")

    def performance_dashboard(self):
        avg = self.admin.show_average_grades()
        eca_data = self.admin.eca_participation()
        alerts = self.admin.identify_low_performers()

        if avg:
            plt.figure(figsize=(10, 4))
            plt.subplot(131)
            plt.bar([f"Sub{i+1}" for i in range(5)], avg, color='skyblue')
            plt.title("Average Grades")

        if eca_data:
            plt.subplot(132)
            students = list(eca_data.keys())
            activities = list(eca_data.values())
            plt.bar(students, activities, color='lightgreen')
            plt.title("ECA Participation")
            plt.xticks(rotation=45)

        if alerts:
            plt.subplot(133)
            ids = [s[0] for s in alerts]
            scores = [s[1] for s in alerts]
            plt.bar(ids, scores, color='salmon')
            plt.axhline(40, color='red', linestyle='--')
            plt.title("Low Performers")
            plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
