from organization import Organization
from trainee import Trainee

from typing import List


class Trainer:
    def __init__(self, name: str, organization: Organization) -> None:
        self.__organization = organization.get_name()
        self.__count = 0
        self.__trainees: List[Trainee] = []
        self.__name = name

    def get_organization(self) -> str:
        return self.__organization

    # Extra

    def add_trainee(self, *args: Trainee) -> None:
        for trainee in args:
            self.__trainees.append(trainee)
            self.__count += 1

    def get_trainees(self) -> List[Trainee]:
        return [trainee.get_name() for trainee in self.__trainees]

    def get_number_of_trainees(self) -> int:
        return self.__count

    def get_name(self) -> str:
        return self.__name
