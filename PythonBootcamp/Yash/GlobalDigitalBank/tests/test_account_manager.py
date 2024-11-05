class CustomError(Exception):
    def __init__(self, message="My Error"):
        super().__init__(message)


def test():
    try:
        raise CustomError("My cutom cutom message")
    except CustomError as e:
        print(e)


test()
