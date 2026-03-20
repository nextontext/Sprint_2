class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_dayes, email=None):
        hours = (7 - rest_dayes) * 8
        return cls(name, hours, rest_dayes, email)

    @classmethod
    def get_email(cls, name, hours=None, rest_days=None):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, value):
        cls.hourly_payment = value

    def salary(self):
        return self.hours * EmployeeSalary.hourly_payment


employee_1 = EmployeeSalary.get_hours("Tonny", 3)
print(employee_1.name)
print(employee_1.hours)
print(employee_1.salary())

employee_2 = EmployeeSalary.get_email("Peter", hours=40)
print(employee_2.name)
print(employee_2.hours)
print(employee_2.salary())
