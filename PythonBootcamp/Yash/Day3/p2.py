grade_book = dict()
students_list = set()


def add_student():
    name = input("Enter name: ")
    if name in students_list:
        print("Not Unique")
        return
    students_list.add(name)
    grade_book[name] = {int(input("Marks 1: ")), int(
        input("Marks 2: ")), int(input("Marks 3: "))}


add_student()
add_student()
