from topic import Topic
from typing import List


class Unit:
    def __init__(self, name: str, duration: int, *topics) -> None:
        self.__name: str = name
        self.__duration = duration
        self.__topic_list: List[Topic] = []
        for topic in topics:
            self.__topic_list.append(topic)

    def get_duration(self) -> int:
        return self.__duration

    # Extra

    def get_topics(self) -> List[Topic]:
        return self.__topic_list

    def get_name(self) -> str:
        return self.__name
