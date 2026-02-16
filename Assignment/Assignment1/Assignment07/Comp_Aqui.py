class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def show_details(self):
        print("Company:", self.name)
        print("Location:", self.location)


class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

    def show_details(self):
        print(f"{self.emp_name} ({self.designation})")


class CompanyAcquisition(Company):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def show_details(self):
        super().show_details()
        print("Employees after acquisition:")
        for emp in self.employees:
            emp.show_details()


class NewEmployee(Employee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company):
        super().__init__(emp_id, emp_name, designation)
        self.joining_date = joining_date
        self.previous_company = previous_company


class Manager(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, team_size):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.team_size = team_size


class HR(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, policies_handled):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.policies_handled = policies_handled


class Developer(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, languages):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.languages = languages


class Intern(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, duration):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.duration = duration


# Hybrid Example
class ManagerHR(Manager, HR):
    pass


class DeveloperIntern(Developer, Intern):
    pass


company = CompanyAcquisition("TechCorp", "New York")

emp1 = Manager(1, "Alice", "Manager", "2024-01-01", "ABC Corp", 10)
emp2 = Developer(2, "Bob", "Developer", "2024-02-01", "XYZ Ltd", ["Python", "Java"])

company.add_employee(emp1)
company.add_employee(emp2)

company.show_details()