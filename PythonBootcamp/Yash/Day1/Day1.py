# Write the code to accept a student's name and scores in three subject.
# Display the average and total.
# Display whether the student has secured 1st, 2nd, pass class or has failed.
# 1st class is for a score of 60 and above, 2nd is for a score of 50 and above,
# while pass class is for a score of 35 and above. If the score is less than 35,then the student fails.

def print_report(name: str, average: float, total: int) -> None:
    print("Report Card")
    print(f"Name: {name}")
    print(f"Avg: {average}")
    print(f"Total: {total}")
    print(f"Rank: {get_rank(average)}")


def get_rank(marks):
    if (marks >= 60):
        return "1st"
    elif (marks >= 50):
        return "2nd"
    elif (marks >= 35):
        return "Pass"
    else:
        return "Fail"


def main():
    name = input()
    m1 = int(input())
    m2 = int(input())
    m3 = int(input())
    total = m1+m2+m3
    avg = total/3
    print_report(name, avg, total)


main()
