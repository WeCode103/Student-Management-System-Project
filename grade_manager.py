import os
from utils import get_path

class GradeManager:
    """
    GradeManager class handles adding, updating, deleting,
    viewing, and averaging student grades stored in a text file.
    """

    def add_grade(self):
        """
        Add grades for a student.
        Prevents adding grades if the student ID already exists in the file.
        """
        student_id = input("Enter Student ID: ")
        file_path = get_path("grades.txt")

        # Check if grades already exist for this student
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                for line in f:
                    if line.startswith(student_id + ","):
                        print("❌ Grades already exist. Try update instead.")
                        return

        subjects = [
            "Academic English",
            "Fundamentals of Data Science",
            "Internet Technologies",
            "Fundamentals of Multimedia",
            "Math"
        ]
        grades = []

        # Collect grades for each subject
        for subject in subjects:
            while True:
                grade = input(f"Enter grade for {subject}: ")
                if grade.isdigit():
                    grades.append(grade)
                    break
                else:
                    print("Invalid input. Please enter a number.")

        # Append new grades to file
        with open(file_path, "a") as f:
            f.write(f"{student_id},{','.join(grades)}\n")

        print("✅ Grades added successfully.")

    def update_grade(self):
        """
        Update grades for a student by student ID.
        Reads all grades and rewrites file with updated grades.
        """
        student_id = input("Enter Student ID to update grades: ")
        file_path = get_path("grades.txt")

        if not os.path.exists(file_path):
            print("grades.txt not found.")
            return

        updated = False
        lines = []

        with open(file_path, "r") as f:
            for line in f:
                if line.startswith(student_id + ","):
                    print("🎯 Enter new grades:")
                    new_grades = []
                    subjects = [
                        "Academic English",
                        "Fundamentals of Data Science",
                        "Internet Technologies",
                        "Fundamentals of Multimedia",
                        "Math"
                    ]

                    for subject in subjects:
                        while True:
                            grade = input(f"New grade for {subject}: ")
                            if grade.isdigit():
                                new_grades.append(grade)
                                break
                            else:
                                print("❌ Invalid input. Please enter a number.")

                    lines.append(f"{student_id},{','.join(new_grades)}\n")
                    updated = True
                else:
                    lines.append(line)

        with open(file_path, "w") as f:
            f.writelines(lines)

        print("✅ Grades updated." if updated else "❌ Student ID not found.")

    def delete_grade(self):
        """
        Delete all grades for a specific student ID.
        """
        student_id = input("Enter Student ID to delete grades: ")
        file_path = get_path("grades.txt")

        if not os.path.exists(file_path):
            print("grades.txt not found.")
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

        print("✅ Grades deleted." if deleted else "❌ Student ID not found.")

    def view_grades_for(self, student_id):
        """
        Display grades for a specific student ID.
        """
        file_path = get_path("grades.txt")

        try:
            with open(file_path, "r") as f:
                for line in f:
                    if line.startswith(student_id + ","):
                        grades = line.strip().split(",")[1:]
                        print("Grades:", ", ".join(grades))
                        return
            print("Grades not found.")
        except FileNotFoundError:
            print("grades.txt not found.")

    def show_average_grades(self):
        """
        Calculate and display average grades across all students.
        """
        file_path = get_path("grades.txt")

        try:
            with open(file_path, "r") as f:
                total = []
                count = 0
                for line in f:
                    parts = line.strip().split(",")[1:]
                    grades = list(map(int, parts))

                    if not total:
                        total = grades
                    else:
                        total = [x + y for x, y in zip(total, grades)]

                    count += 1

            if count > 0:
                avg = [round(x / count, 2) for x in total]
                print("📊 Average grades:", avg)
            else:
                print("No records to average.")
        except Exception as e:
            print(f"Error reading grades.txt: {e}")
