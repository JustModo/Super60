# Task: Write a program to create a List of 5 numbers.
# Add 2 more numbers to the List, remove one,
# and print the final List.

num = []
for _ in range(5):
    num.append(int(input()))

num.append(int(input()))
num.append(int(input()))
num.pop()

print(*num, sep=" ")


# Write a program to find the sum,
# maximum, and minimum of numbers in a List.
# Take input from the user to create the List.

num = []
for _ in range(5):
    num.append(int(input()))

print(max(num))
print(min(num))
print(sum(num))

# Write a program that removes aLL duplicates
# and prints the unique items.

num = []
for _ in range(5):
    num.append(int(input()))

print(list(set(num)))

# Create a dictionary where keys are names of
# students and values are their ages.
# Add a new student to the dictionary, remove
# one and print the updated dictonary

students = {}

for _ in range(2):
    name = input()
    age = int(input())
    students[name] = age

name = input()
age = int(input())
students[name] = age

students.pop("Alice", None)

print(students)
