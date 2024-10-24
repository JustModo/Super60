class Address:

    def __init__(self, street: str, city: str, zipcode: int):
        self.street = street
        self.city = city
        self.zipcode = zipcode


class Employee:
    __count = 1

    # def __init__(self,  name: str, address: Address):
    #     self.name = name
    #     self.emp_id = Employee.__count
    #     self.address = address
    #     Employee.__count += 1

    def __init__(self):
        self.name: str
        self.emp_id = Employee.__count
        self.address: Address
        self.role: str
        self.basic_salary: int
        self.hra: int
        Employee.__count += 1

    def show_data(self) -> None:
        print("Employee Details:")
        print(f"Name: {self.name}")
        print(f"ID: {self.emp_id}")
        print("Employee Address:")
        print(f"City: {self.address.city}")
        print(f"Street: {self.address.street}")
        print(f"Zipcode: {self.address.zipcode}")


def store_data_return() -> Employee:
    return Employee(input("Enter your Employee Name: "), Address(input("Enter Street: "), input("Enter City: "), int(input("Enter Zipcode: "))))


def store_data(employee: Employee) -> Employee:
    employee.name = input("Enter your Employee Name: ")
    employee.address = Address(input("Enter Street: "), input(
        "Enter City: "), int(input("Enter Zipcode: ")))
    employee.role = input("Role")
    employee.basic_salary = int(input("Basic Salary"))
    employee.hra = input("Hra")


if __name__ == "__main__":
    # Return Object Class
    # employee1 = store_data_return()
    # employee1.show_data()

    # Store Data as Pass by Reference
    employee2 = Employee()
    store_data(employee2)
    employee2.show_data()
