class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def _financial_report(self):
        return "Confidential Financial Report"

    def show_details(self):
        print("Company:", self.name)


class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

    def _policy_update(self):
        return "Confidential Policy Update"

    def show_details(self):
        print(self.emp_name, "-", self.designation)


class NewEmployee(Employee):
    def __init__(self, emp_id, emp_name, designation, joining_date):
        super().__init__(emp_id, emp_name, designation)
        self.joining_date = joining_date


class Manager(NewEmployee, Company):
    def access_finance(self):
        print(self._financial_report())


class HR(NewEmployee):
    def access_policy(self):
        print(self._policy_update())


class Developer(NewEmployee):
    pass


class Intern(NewEmployee):
    pass


class ManagerHR(Manager, HR):
    pass


class DeveloperIntern(Developer, Intern):
    pass


mgr = Manager("1", "Alice", "Manager", "2024")
mgr.access_finance()

hr = HR("2", "Bob", "HR", "2024")
hr.access_policy()