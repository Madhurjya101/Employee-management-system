# Employee management system
 A Python CLI-based Employee Management System using OOP and JSON for persistent storage. Supports full CRUD operations with input validation and structured design.

# Employee Management System (CLI + JSON)

A simple command-line based Employee Management System built using Python and Object-Oriented Programming (OOP).  
This project demonstrates CRUD operations, JSON data persistence, input validation, and clean code structure.

---

## 📌 Features

- Add new employee
- Search employee by ID
- Check salary by ID
- View all employees
- Delete employee
- Update:
  - Name
  - Department
  - Salary
- Automatic ID generation
- JSON file-based data storage
- Input validation with error handling

---

## 🏗 Project Structure

The project is built using OOP principles:

### 1️⃣ Employee Class
Represents a single employee object.

- Stores employee data (ID, Name, Department, Salary)
- Converts object → dictionary (`to_dict`)
- Converts dictionary → object (`from_dict`)

### 2️⃣ Manager Class
Controls all operations.

- Maintains list of Employee objects
- Handles CRUD operations
- Loads data from JSON file
- Saves data to JSON file
- Sorts employees by ID

---

## 💾 Data Storage

All employee data is stored in: emp.json


Data is saved in structured JSON format for persistence.
Example:

```json
[
    {
        "ID": 1,
        "Name": "John",
        "Department": "IT",
        "Salary": 50000
    }
]
