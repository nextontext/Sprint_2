class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(self):
        if self.hours is None:
            self.hours = (7 - self.rest_days) * 8
        return self.hours

    def get_email(self):
        if self.email is None:
            return f"{self.name}@email.com"
        return self.email

    @classmethod
    def set_hourly_payment(cls, value):
        cls.hourly_payment = value

    def salary(self):
        hours = self.get_hours()
        return hours * self.hourly_payment


employee_1 = EmployeeSalary("Tonny", hours=40)
print(f"Заработная плата {employee_1.name}", employee_1.salary())
print(f"Адрес электронной почты {employee_1.name}:", employee_1.get_email())
print()
employee_2 = EmployeeSalary("Peter", rest_days=3)
print(f"Заработная плата {employee_2.name}", employee_2.salary())
print(f"{employee_2.name}, отработал часов: ", employee_2.get_hours())
print(f"Адрес электронной почты {employee_2.name}:", employee_2.get_email())
