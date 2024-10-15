class Organization:
    def __init__(self, organization_name: str) -> None:
        self.__organization_name = organization_name

    def get_name(self) -> str:
        return self.__organization_name
