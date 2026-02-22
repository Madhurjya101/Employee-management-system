
import json 

class Employee:
    def __init__(self, id, name, department, salary):          # makes employee object
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    def to_dict(self):          # converts employee object to dictionary 
        return{
            "ID": self.id,
            "Name": self.name,
            "Department": self.department,
            "Salary": self.salary
        }
    
    @classmethod
    def from_dict(cls, item):          # converts dictionary to employee object
        return cls(
            item["ID"],
            item["Name"],
            item["Department"],
            item["Salary"]
        )
    
def get_valid_id():          # get valid input for employee id
    while True:
        try:
            raw = input("Enter ID: ")
            if not raw.strip():
                print("ID can not be empty !!")
                continue
            user = int(raw)
            return user
        except KeyboardInterrupt:
            print("\nPLease re-enter ID")
            continue
        except ValueError:
            print("Please enter a valid number")
            continue
        except Exception as e:
            print("Unexpected error: ", e)
            continue

def get_valid_salary():          # get valid input for employee salary
    while True:
        try:
            raw = input("Enter salary: ")
            if not raw.strip():
                print("Salary can not be empty !!")
                continue
            user = int(raw)
            return user
        except KeyboardInterrupt:
            print("\nPLease re-enter salary")
            continue
        except ValueError:
            print("Please enter a valid number")
            continue
        except Exception as e:
            print("Unexpected error: ", e)
            continue

def get_valid_name(usable_area):          # get valid input for employee name
    while True:
        try:
            user = input(f"Enter {usable_area}: ").strip()
            if not user.strip():
                print(f"{usable_area.capitalize()} can not be empty !!")
                continue
            return user
        except KeyboardInterrupt:
            print(f"\nPLease re-enter {usable_area}")
            continue
        except Exception as e:
            print("Unexpected error: ", e)
            continue

def get_valid_department(usable_area):          # get valid selection for employee department
    departments = ["IT", "HR", "Finance", "Marketing", "Operations"]
    while True:
        print("Available departments-")
        for i, dept in enumerate(departments, start = 1):
            print(f"{i}. {dept}")
        try:
            choice = int(input(f"Enter {usable_area}: "))
            if 1<= choice <= len(departments):
                return departments[choice-1]
            else:
                print("Enter a valid choice")
                continue
        except KeyboardInterrupt:
            print("Please try again.....")
            continue
        except ValueError:
            print("Enter a valid number.....")
        except Exception as e:
            print("Unexpected error: ", e)
        
class Manager:
    def __init__(self):          # stores all Employee objects in memory
        self.employee = []

    def find_emp(self, emp_id):          # helper method for find a employee by given id
        for emp in self.employee:
            if emp.id == emp_id:
                return emp
        return None

    def load_from_file(self):          # loads json file's data at self.employee as employee object
        self.employee = []
        try:
            with open("emp.json", "r") as f:
                data = json.load(f)
            for i in data:
                emp = Employee.from_dict(i)
                self.employee.append(emp)
        except(FileNotFoundError, json.JSONDecodeError):
            self.employee = []

    def save_to_file(self):          # saves self.employee's data at json file in form of dictionary 
        data = []
        for i in self.employee:
            data.append(i.to_dict())
        with open("emp.json", "w") as f:
            json.dump(data, f, indent=4)

    def sort_by_id(self):          # keeps employee list ordered after add/delete
        self.employee = sorted(self.employee, key = lambda emp : emp.id)

    def add_emp(self):          # adds employee in self.employee from user input
        if not self.employee:
            emp_id = 1
        else:
            max_id = max(emp.id for emp in self.employee)
            emp_id = max_id+1
        name = get_valid_name("name").title()
        department = get_valid_department("department")
        salary = get_valid_salary()
        self.employee.append(Employee(emp_id, name, department, salary))
        self.sort_by_id()
        self.save_to_file()
        print("\nAddition completed\n")

    def search_emp(self):          # searches employee data by theie unique id
        input_id = get_valid_id()
        emp = self.find_emp(input_id)
        if not emp:
            print(f"\nNo employee found with ID {input_id} !!\n")
            return
        else:
            print(f"\nHere's the employee's information-\nName: {emp.name}\nDepartment: {emp.department}\n")
                
    def emp_salary(self):          # checks employee salary by thier unique id
        input_id = get_valid_id()
        emp = self.find_emp(input_id)
        if not emp:
            print(f"\nNo employee found with ID {input_id} !!\n")
            return
        else:
            print(f"The salary of ID {input_id} is {emp.salary}/-\n")

    def view_all_emp(self):          # shows all employee 
        if not self.employee:
            print("\nNo employee is hired till now !!")
            return
        print("\n")
        for emp in self.employee:
            print(f"ID - {emp.id} | Name - {emp.name} | Department - {emp.department} | Salary - {emp.salary}/-")
        print("\n")

    def delete_emp(self):          # deletes employee from self.employee with their unique id from user input
        input_id = get_valid_id()
        emp = self.find_emp(input_id)
        if not emp:
            print(f"No employee found with ID {input_id}\n")
            return
        self.employee.remove(emp)
        self.sort_by_id()
        self.save_to_file()
        print("Deletion completed\n")
        

    def update_department(self):          # updates department of selected employee 
        input_id = get_valid_id()
        emp_for_update = self.find_emp(input_id)
        if not emp_for_update:
            print(f"\nNo employee found with ID {input_id}\n")
            return
        print(f"\nThe current department of ID {input_id} is {emp_for_update.department}")
        emp_for_update.department = get_valid_department("new department")
        print("Department updated\n")
        self.save_to_file()
    
    def update_name(self):          # updates name of selected employee
        input_id = get_valid_id()
        emp_for_update = self.find_emp(input_id)
        if not emp_for_update:
            print(f"\nNo employee found with ID {input_id}\n")
            return
        print(f"\nThe current name of ID {input_id} is {emp_for_update.name}")
        emp_for_update.name = get_valid_name("new name").title()
        print("Name updated\n")
        self.save_to_file()

    def update_salary(self):          # updated salary of selected employee
        input_id = get_valid_id()
        emp_for_update = self.find_emp(input_id)
        if not emp_for_update:
            print(f"\nNo employee found with ID {input_id}\n")
            return
        print(f"\nThe current salary of ID {input_id} is {emp_for_update.salary}/-")
        emp_for_update.salary = get_valid_salary()
        print("Salary updated\n")
        self.save_to_file()

start = Manager()
start.load_from_file()

def menu():          # Menu system to manage the whole program
    while True:
        print('''\n\n\nHere's the choices -\n1. Add employee\n2. Search employee (by ID)\n3. Check salary of employee (by ID)\n4. View all employee\n5. Delete employee\n6. Update department of employee (by ID)\n7. Update name of employee (by ID)\n8. Update salary of employee (by ID)\n9. Exit''')

        while True:
            try:
                user = int(input("\nEnter your choice here: "))
                if user<1 or user>9:
                    print("\nPlease enter a valid choice (1-9)")
                    continue
                break
            except KeyboardInterrupt:
                print("\n\nPlease re-enter your choice")
                continue
            except Exception:
                print("\nPlease enter a valid choice")
    
        if user == 1:
            start.add_emp()
            input("Press enter to return to menu.......")
        elif user == 2:
            start.search_emp()
            input("Press enter to return to menu.......")
        elif user == 3:
            start.emp_salary()
            input("Press enter to return to menu.......")
        elif user == 4:
            start.view_all_emp()
            input("Press enter to return to menu.......")
        elif user == 5:
            start.delete_emp()
            input("Press enter to return to menu.......")
        elif user == 6:
            start.update_department()
            input("Press enter to return to menu.......")
        elif user == 7:
            start.update_name()
            input("Press enter to return to menu.......")
        elif user == 8:
            start.update_salary()
            input("Press enter to return to menu.......")
        elif user == 9:
            print("Closing program............")
            break

menu()
