

class Address:
    def __init__(self, street: str, city: str, zipcode: int) -> None:
        self.street = street
        self.city = city
        self.zipcode = zipcode


class Employee:
    __count = 1

    def __init__(self) -> None:
        self.name: str
        self.emp_id = Employee.__count
        self.address: Address
        self.role: str
        self.role_id: int
        self.basic_salary: int
        self.hra: int
        self.percentage: int
        Employee.__count += 1

    def show_data(self) -> None:
        allowance = SalaryCalculator.get_allowance(
            self.basic_salary, self.percentage)
        salary = SalaryCalculator.get_salary(
            self.basic_salary, self.hra, allowance)
        role = RoleBuilder.get_role_description(self.role_id)
        print(f"{self.emp_id}\t{self.name}\t{role}\t", end="")
        print(f"\t{self.basic_salary}\t\t{allowance}\t\t{salary}")


def store_data(employee: Employee) -> Employee:
    role_list = ["hr", "developer",
                 "sales", "manager", "ceo"]
    employee.name = input("Enter your Employee Name: ")
    employee.address = Address(input("Enter Street: "), input(
        "Enter City: "), int(input("Enter Zipcode: ")))
    employee.basic_salary = int(input("Enter Basic Salary: "))
    employee.hra = int(input("Enter HRA: "))
    employee.percentage = int(input("Enter Bonus %: "))
    role: str
    while True:
        role = input("Enter Role: ")
        if role.lower() not in role_list:
            print("Not valid Role")
            continue
        print()
        break
    employee.role = role
    employee.role_id = role_list.index(role)
    return employee


class RoleBuilder:
    __role_desc = ["I am HR", "I am Developer",
                   "I am Sales", "I am Manager", "I am CEO"]

    @staticmethod
    def get_role_description(role_id: int) -> str:
        return RoleBuilder.__role_desc[role_id]


class EmployeeReport:
    def __init__(self, report_date: str) -> None:
        self.report_date = report_date

    def display_employees(self, employee_list: list[Employee]) -> None:
        print("\n----------Employee Report----------")
        print(F"\nDate: {self.report_date}\n")
        print("EMP_ID\tNAME\tROLE\t\tBASIC\t\tALLOW\t\tSALARY")
        for employee in employee_list:
            employee.show_data()
        print("\n----------------End----------------")


class SalaryCalculator:
    @staticmethod
    def get_allowance(basic, percentage) -> float:
        return basic * (percentage/100)

    @staticmethod
    def get_salary(basic, hra, allowance) -> float:
        return basic + hra + allowance


if __name__ == "__main__":
    employee_list: list[Employee] = []
    for _ in range(0, 2):
        employee_list.append(store_data(Employee()))

    report1 = EmployeeReport("Jan 1 2024")
    report1.display_employees(employee_list)
