class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def first_name(self):
        return self.first_name

    def last_name(self):
        return self.last_name

    def salary(self):
        return self.salary

    @staticmethod
    def from_string(string):
        arg = string.split("-")
        emp = Employee(arg[0], arg[1], int(arg[2]))
        return emp
