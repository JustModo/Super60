from trainer import Trainer
from course import Course

from typing import List, Set


class Training:
    def __init__(self, organization_name) -> None:
        self.__trainers: List[Trainer] = []
        self.__organization_name = organization_name
        self.__course_list: List[Course] = []

    def get_number_of_trainees(self) -> int:
        return len(set(trainee for trainer in self.__trainers for trainee in trainer.get_trainees()))

    def get_training_organization_name(self) -> str:
        return self.__organization_name

    def get_training_duration_in_hrs(self) -> int:
        duration_list = []
        for course in self.__course_list:
            for module in course.get_modules():
                for unit in module.get_units():
                    duration_list.append(unit.get_duration())
        return sum(duration_list)

    # Extra

    # Trainers

    def add_trainers(self, *trainers: Trainer) -> None:
        for trainer in trainers:
            self.__trainers.append(trainer)

    def get_trainers(self) -> List[str]:
        return [trainer.get_name() for trainer in self.__trainers]

    def get_trainees(self) -> Set[str]:
        return set(trainee for trainer in self.__trainers for trainee in trainer.get_trainees())

    # Courses

    def add_courses(self, *courses: Course) -> None:
        for course in courses:
            self.__course_list.append(course)

    def get_courses(self, *courses: Course) -> None:
        for course in courses:
            self.__course_list.append(course.get_name())
