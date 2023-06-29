from test1 import Employee
from test2 import dev_1, dev_2


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("---->", emp.fullname())


mgr_1 = Manager("willam", "smith", 90000, [dev_1])

mgr_1.print_emps()
print(mgr_1.email())

mgr_1.add_emp(dev_2)

mgr_1.print_emps()
