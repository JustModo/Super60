from typing import List, Union

mixed: List[Union[str, int]] = [1, "two", 3, "five"]

mixed.append(3.0)
mixed.pop()

person = {
    'name': "Yash",
    'age': 10
}

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
print(*numbers, sep=", ")

# print(person.keys)
print(numbers[-5:])

