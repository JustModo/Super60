class Parent:
    temp = [i for i in range(5)]

    def __init__(self) -> None:
        self.temp = [i for i in range(5)]

    def pop(self):
        self.temp.pop()

    def get_list(self):
        print(*self.temp, sep=" ")


class Child(Parent):
    def __init__(self) -> None:
        super().__init__()


parent = Parent()
child = Child()

parent.get_list()
parent.pop()

parent.get_list()
child.get_list()
