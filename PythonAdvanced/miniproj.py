from abc import ABC, abstractmethod
import random


class Animal(ABC):
    def __init__(self, name, health, hunger, habitat_type):
        self._name = name
        self._health = health
        self._hunger = hunger
        self._habitat_type = habitat_type

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food_amount):
        pass

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if (value == 0):
            print("It's Dead Now..")
        self._health = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def hunger(self):
        return self._hunger

    @hunger.setter
    def hunger(self, value):
        if (value == 100):
            print("It's ALready Full!")
        self._hunger = value

    @property
    def habitat_type(self):
        return self._habitat_type

    @habitat_type.setter
    def habitat_type(self, value):
        self._habitat_type = value

    def decrease_health(self, amount):
        self.health = max(self.health-amount, 0)

    def increase_hunger(self, amount):
        self._health = min(self.hunger+amount, 100)


class Lion(Animal):

    def __init__(self, name, health, hunger, habitat_type):
        super().__init__(name, health, hunger, habitat_type)

    def make_sound(self):
        print("Roar!")

    def feed(self, amount):
        self.hunger = max(self.hunger - amount * 2, 0)
        self.health += max(amount, self.hunger) * 0.5


class Elephant(Animal):

    def __init__(self, name, health, hunger, habitat_type):
        super().__init__(name, health, hunger, habitat_type)

    def make_sound(self):
        print("Trumpet!")

    def feed(self, amount):
        self.hunger = max(self.hunger - amount * 1.5, 0)
        self.health += amount * 0.3


class Parrot(Animal):

    def __init__(self, name, health, hunger, habitat_type):
        super().__init__(name, health, hunger, habitat_type)

    def make_sound(self):
        print("Squawk!")

    def feed(self, amount):
        self.hunger = max(self.hunger - amount * 0.5, 0)
        self.health += amount * 0.2


class Habitat(ABC):
    def __init__(self, type: str, condition: float, animals: list[Animal]):
        self._type = type
        self._condition = condition
        self._animals = animals

    @abstractmethod
    def affect_animal(self, animal: Animal):
        pass

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value: float):
        self._condition = value

    def add_animal(self, animal: Animal):
        if (animal.habitat_type == self._type):
            self._animals.append(animal)

    def degrade(self, amount: float):
        self.condition = min(self.condition - amount, 0)


class Savanna(Habitat):
    def __init__(self, condition: float, animals: list[Animal] = []):
        super().__init__("Savanna", condition, animals)

    def affect_animal(self, animal: Animal):
        if self.condition > 50:
            animal.health += 5
        else:
            animal.health -= 5


class Jungle(Habitat):
    def __init__(self, condition: float, animals: list[Animal] = []):
        super().__init__("Jungle", condition, animals)

    def affect_animal(self, animal: Animal):
        if self.condition > 60:
            animal.health += 3
        else:
            animal.health -= 3


class Aviary(Habitat):
    def __init__(self, condition: float, animals: list[Animal] = []):
        super().__init__("Aviary", condition, animals)

    def affect_animal(self, animal: Animal):
        if self.condition > 70:
            animal.health += 2
        else:
            animal.health -= 2


class Staff(ABC):
    def __init__(self, name, energy):
        self._name = name
        self._energy = energy

    @abstractmethod
    def perform_task(self, target):
        pass

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        if value < 0 or value > 100:
            raise ValueError("Not within range")
        self._energy = value


class Caretaker(Staff):
    def __init__(self, name, energy):
        super().__init__(name, energy)

    def perform_task(self, target):
        if isinstance(target, Habitat):
            target.condition += 20
            self.energy -= 10
            print(f"Caretaker maintaining {target.__class__.__name__}")
        else:
            print("Caretaker can only maintain habitats.")


class Veterinarian(Staff):
    def __init__(self, name, energy):
        super().__init__(name, energy)

    def perform_task(self, target):
        if isinstance(target, Animal):
            target.health += 15
            self.energy -= 15
            print(f"Veterinarian treating {target.name}")
        else:
            print("Veterinarian can only treat animals.")


class Sanctuary:

    __pairs = [(Parrot, Aviary), (Lion, Savanna), (Elephant, Jungle)]

    def __init__(self, animals: list[Animal] = [], habitats: list[Habitat] = [], staff: list[Staff] = []):
        self.animals = animals
        self.habitats = habitats
        self.staff = staff

    def add_animal(self, animal: Animal, habitat: Habitat):
        if habitat not in self.habitats:
            raise ValueError("Habitat not managed by Santuary.")

        if ((animal.__class__, habitat.__class__) not in self.__pairs):
            raise ValueError("Not Compatible")
        
        habitat.add_animal(animal)

    def add_habitat(self, habitat):
        if (habitat in self.habitats):
            raise ValueError("Habitat Exists")
        self.habitats.append(habitat)

    def simulate_day(self):
        print("--- Day 1 ---")

        print("")

        for animal in self.animals:
            animal.make_sound()

        print("")

        for staff in self.staff:
            if isinstance(staff, Caretaker):
                habitat = random.choice(self.habitats)
                staff.perform_task(habitat)

        for staff in self.staff:
            if isinstance(staff, Veterinarian):
                animal = random.choice(self.animals)
                staff.perform_task(animal)

        for animal in self.animals:
            animal.feed(20)

        print("\nAnimal Status:")
        for animal in self.animals:
            print(f"{animal.name}: Health {animal.health}, Hunger {animal.hunger}")

        print("\nHabitat Status:")
        for habitat in self.habitats:
            print(f"{habitat.__class__.__name__}: Condition {habitat.condition}")


def main():
    lion = Lion("Lion", 65, 60, "Savanna")
    elephant = Elephant("Elephant", 83, 60, "Jungle")
    parrot = Parrot("Parrot", 72, 60, "Aviary")

    savanna = Savanna(75, [lion])
    jungle = Jungle(65, [elephant])
    aviary = Aviary(85, [parrot])

    caretaker = Caretaker("Caretaker", 100)
    veterinarian = Veterinarian("Veterinarian", 100)

    sanctuary = Sanctuary([lion, elephant, parrot], [
                          savanna, jungle, aviary], [caretaker, veterinarian])

    sanctuary.simulate_day()


if __name__ == "__main__":
    main()
