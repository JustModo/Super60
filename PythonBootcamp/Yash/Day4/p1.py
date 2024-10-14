# Create a person class with name and age constructor

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> None:
        return (f"Hi I'm {self.name} and I'm {self.age}")

p1 = Person("Yash", 19)
print(p1)

# Car class with maker and model and wheels attribute

class Car:
    wheels = 4

    def __init__(self, maker: str, model: str) -> None:
        self.maker = maker
        self.model = model

    def __str__(self) -> str:
        return f"{self.maker} {self.model}"


c1 = Car("Volvo", "Model123")
print(c1)
