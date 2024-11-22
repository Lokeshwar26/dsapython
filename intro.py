class Employee:
    empcount = 0  # Class variable to count the number of employees

    def __init__(self, name, salary):
        self.name = name  # Instance variable for name
        self.salary = salary  # Instance variable for salary
        Employee.empcount += 1  # Increment the employee count

    def display_count(self):
        print("Total number of employees are %d" % Employee.empcount)

    def display_employee(self):
        print("Name:", self.name, "Salary:", self.salary)


# Example of using the class
emp1 = Employee("John", 50000)
emp2 = Employee("Jane", 60000)
emp3 = Employee("Drake", 70000)

emp1.display_employee()
emp2.display_employee()
emp3.display_employee()
emp1.display_count()

# Adding a new attribute `age` to `emp1`
setattr(emp1, "age", 8)  # Corrected `age` to a string

