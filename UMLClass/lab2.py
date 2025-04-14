class InvalidExperienceException(Exception):
    pass


class Employee:
    def __init__(self, name: str, age: int, experience: str):
        self.name = name
        self.age = age
        self.experience = experience

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_experience(self):
        return self.experience

    def set_experience(self, experience):
        self.experience = experience

    def compute_years(self):
        if "." in self.experience and len(self.experience.split(".")) == 2:
            year, month = map(int, self.experience.split("."))
            if 0 <= month <= 11:
                if month >= 10:
                    return year + 1
                return year
            else:
                raise InvalidExperienceException(
                    "Month must be between 0 and 11.")
        else:
            raise InvalidExperienceException(
                "Invalid format. Must be in X.Y format.")


class Address:
    def __init__(self, line1: str, line2: str, city: str, state: str, pin: int):
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.state = state
        self.pin = pin

    def __str__(self):
        return f"{self.line1}, {self.line2}, {self.city}, {self.state} - {self.pin}"


class Salary:
    def __init__(self, basic: float, hra: float, allowance: float):
        self.basic = basic
        self.hra = hra
        self.allowance = allowance

    def compute_total_salary(self):
        return self.basic + self.hra + self.allowance


class Employment:
    def __init__(self, date_of_joining: str, notice_period: int = 90):
        self.date_of_joining = date_of_joining
        self.notice_period = notice_period


class Hiring:
    def __init__(self):
        self.technical_round = 20
        self.manager_round = 5
        self.hr_round = 5
        self.offer_rollout = 10

    def total_hiring_duration(self):
        return self.technical_round + self.manager_round + self.hr_round + self.offer_rollout


class Console:
    @staticmethod
    def print_employee_details(employee: Employee, address: Address, salary: Salary, employment: Employment, hiring: Hiring):
        print(
            f"Employee Details:\nName: {employee.get_name()}\nAge: {employee.get_age()}\nExperience: {employee.get_experience()} years ({employee.compute_years()} actual years)")
        print(f"\nAddress: {address}")
        print(
            f"\nSalary Details:\nBasic: {salary.basic}\nHRA: {salary.hra}\nAllowance: {salary.allowance}\nTotal: {salary.compute_total_salary()}")
        print(
            f"\nEmployment Details:\nDate of Joining: {employment.date_of_joining}\nNotice Period: {employment.notice_period} days")
        print(
            f"\nHiring Process Duration: {hiring.total_hiring_duration()} days")


# Example Usage
emp = Employee("John Doe", 30, "5.10")
addr = Address("123 Street", "Apt 4B", "New York", "NY", 10001)
sal = Salary(50000, 10000, 5000)
emp_info = Employment("2022-05-15")
hiring = Hiring()

Console.print_employee_details(emp, addr, sal, emp_info, hiring)
