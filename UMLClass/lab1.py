# Problem Statement 1: Employee Class
# 1. Create an Employee class.

# 2. Attributes: name (str), age (int), and experience (str).

# 3. Add setter and getter methods for each attribute.

# 4. Add a compute_years method to calculate experience in years.
# a. Throw an InvalidExperienceException if the experience is not in the permissible range.
# b. Permissible range: i. Only 1 digit after . (e.g., 5.7). ii. If 2 digits after ., they must be 10 or 11 (e.g., 5.10 or 5.11).
# 5. Add a rule to upgrade/downgrade experience:
# a. If the fractional part is 10 or 11, upgrade the integer part by 1 (e.g., 5.10 → 6).
# b. If the fractional part is a single digit, downgrade to the integer part (e.g., 4.7 → 4).


# Problem Statement 2:
# Address Class

# 1. Create an Address class.

# 2. Attributes: line1, line2, city, state, pin.

# 3. Add setter and getter methods for each attribute.

# 4. Establish a "has-a" relationship: Employee has an Address.

# 5. Create a Console class to print all details of the employee and address.

class InvalidExperienceException(Exception):
    pass


class Address:
    def __init__(self, line1: int, line2: int, city: str, state: str, pin: int) -> None:
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.state = state
        self.pin = pin

    def __str__(self) -> str:
        return f"{self.line1} {self.line2} {self.city} {self.state} {self.pin}"


class Employee:
    def __init__(self,  name="", age=0, experience=""):
        self.name = name
        self.age = age
        self.experience = experience
        self.address = None

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

    def compute_years(self, years: str):
        if "." in years and len(years.split(".")) == 2:
            year, month = years.split(".")

            if len(month) == 2 and int(month) not in range(10, 13):
                raise InvalidExperienceException
            elif len(month) == 2:
                return int(year) + 1
            else:
                return int(year)
        else:
            raise InvalidExperienceException

    def get_address(self):
        if self.address is None:
            return None
        return self.address

    def set_address(self, address: Address):
        self.address = address

    def __str__(self) -> str:
        return f"{self.get_name()} {self.get_age()} {self.get_experience()}"


class Console:

    @staticmethod
    def print(employee: Employee):
        print(employee, employee.address)


a1 = Address(123, 123, "abc", "bcd", 456)
e1 = Employee()
e1.set_address(a1)

c1 = Console.print(e1)

print(e1.compute_years("1.9"))
print(e1.get_address())
