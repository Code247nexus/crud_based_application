# 📌 CRUD-Based Student Management (CLI Application)

This is a **command-line based CRUD application** built using Python and MySQL. It allows users to manage student records directly from the terminal.

---

## ⚙️ Tech Stack

* **Language:** Python
* **Database:** MySQL
* **Connector:** mysql-connector-python
* **Environment Variables:** python-dotenv

---

## 📂 Project Structure

```bash
connection.py   # Handles database connection using environment variables
queries.py      # Contains all SQL CRUD operations
main.py         # CLI menu and application entry point
```

---

## ✨ Features

* Add a new student
* View all students
* View student by roll number
* Update student details
* Delete student record
* MySQL database integration
* Uses environment variables for DB credentials

---

## 🧠 How It Works

* The application runs via a CLI menu loop 
* Database connection is handled using a dedicated class 
* All SQL queries are modularized in a separate class 
* Each operation (Create, Read, Update, Delete) is executed through user input

---

## 🗄️ Database Schema (Required)

Make sure you have a table like this:

```sql
CREATE TABLE stud (
    rollno INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    marks FLOAT,
    grade VARCHAR(10),
    section VARCHAR(10),
    project VARCHAR(100)
);
```

---

## 🔐 Environment Setup

Create a `.env` file in your project root:

```env
DB_USER=your_username
DB_HOST=localhost
DB_PASSWORD=your_password
DB_NAME=your_database
```

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install mysql-connector-python python-dotenv
```

### 2. Run the Application

```bash
python main.py
```

---

## 🖥️ Sample Menu

```text
1. Add Student
2. View All Students
3. View Student by ID
4. Update Student
5. Delete Student
6. Exit
```

---

## ⚠️ Limitations

* CLI-based (no GUI or API yet)
* No authentication system
* Basic input validation
* Error handling is minimal

---

## 📈 Future Improvements

* Convert to FastAPI backend
* Add REST APIs
* Add authentication (JWT)
* Build frontend UI
* Add logging and better validation

---

## 📌 Key Learning Outcomes

* Working with MySQL in Python
* Structuring code into modules
* Implementing CRUD operations
* Handling database connections safely
* Building CLI-based applications

---

## ⭐ Acknowledgment

This project is part of my backend learning journey, focusing on building strong fundamentals before moving to frameworks like FastAPI.

---
