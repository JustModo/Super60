# Class Fruit with Mango and Apple as Sub Class with Overridden methods

class Fruit:
    def __init__(self) -> None:
        pass

    def greet(self):
        print("I am a Fruit!")


class Mango(Fruit):
    def __init__(self) -> None:
        super().__init__()

    def greet(self):
        print("I am a Mango!")


class Apple(Fruit):
    def __init__(self) -> None:
        super().__init__()

    def greet(self):
        print("I am a Apple!")


f1 = Fruit()

f1.greet()

m1 = Mango()

m1.greet()
