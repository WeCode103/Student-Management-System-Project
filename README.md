# 🎓 Student Profile Management System

A final group project for the **Fundamentals of Data Science (UFCFK1-15-0)** module.  
This Python-based app allows admins and students to manage academic data, profiles, and extracurricular activities efficiently.

---

## 👥 Team Members
- Bikranta (Team lead, main.py + GitHub repo manager)
- Aaryal (Student feature dev, data handling)
- Shuban(Admin analytics + GUI design)

---

## 📚 Features

### 🧑‍🎓 Student Role
- Login securely
- View personal profile
- View grades (from `grades.txt`)
- View ECA details (from `eca.txt`)

### 🛠️ Admin Role
- Add new users with roles (admin/student)
- Delete users from all records
- View average subject-wise grades
- (Optional) Performance dashboard & alerts

---

## 🗂 Project Structure
```
├── main.py # Main entry point for the app
├── utils.py # Helper functions like login verification, user info fetch
├── user_models.py # Contains User, Admin, and Student class definitions
├── eca_manager.py #Admin handles CRUD operation of ECA
├── grade_manager.py #Admin handles CRUD operation of ECA
├── login_system.py #It shows login for admin and studet to get into the respective user dashboard
├──user_menu.py#Handles Admin and Student Menus 
├── gui.py # (Optional) GUI features (if implemented)
├── data/ # Folder holding all the data files
│ ├── users.txt # Stores registered users (ID, name, role)
│ ├── passwords.txt # Stores usernames and passwords
│ ├── grades.txt # Stores subject-wise grades for each student
│ └── eca.txt # Stores extracurricular activity info per student
├── report/ # Final submission materials
│ ├── report.docx # Written report document
│ ├── slides.pptx # Presentation slides
│ └── screenshots/ # Folder containing demo screenshots
├── README.md # This file (project overview and instructions)
```
