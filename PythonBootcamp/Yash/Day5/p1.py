
def divide(a: int, b: int):
    try:
        res = a/b
    except ZeroDivisionError:
        print("Cant Divide by 0!")
    except TypeError:
        print("Not a Number!")
    else:
        print(f"Quotient = {res}")
    finally:
        print("Executed Operation")


divide(10, 2)
divide(10, 0)
divide(10, 'a')
