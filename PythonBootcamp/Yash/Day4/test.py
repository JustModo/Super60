class Person:
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname

    def greet(self):
        print(f"{self.fname} {self.lname}")

    def exist(self):
        print("I Exist")


class Student(Person):
    def __init__(self, fname: str, lname: str, marks: int) -> None:
        super().__init__(fname, lname)
        self.marks = marks

    def greet(self):
        print(f"{self.fname} {self.lname} {self.marks}")


person1 = Person("Yash", "L")

person1.greet()

s1 = Student("Yash", "L", 100)

s1.greet
