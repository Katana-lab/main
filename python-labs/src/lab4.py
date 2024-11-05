class Insect:
    def __init__(self, name="Unknown", speed=0.0, weight=0.0, id_number=0, category="Insect"):
        self.__name = name
        self.__speed = speed
        self.__weight = weight
        self.id_number = id_number
        self.category = category

    def get_name(self):
        return self.__name

    def get_speed(self):
        return self.__speed

    def get_weight(self):
        return self.__weight

    def set_name(self, name):
        self.__name = name

    def set_speed(self, speed):
        self.__speed = speed

    def set_weight(self, weight):
        self.__weight = weight

    def __str__(self):
        return f"Insect(Name: {self.__name}, Speed: {self.__speed} m/s, Weight: {self.__weight} grams, ID: {self.id_number}, Category: {self.category})"

    def __repr__(self):
        return f"Insect({self.__name!r}, {self.__speed!r}, {self.__weight!r}, {self.id_number!r}, {self.category!r})"

    def __del__(self):
        print(f"Deleting Insect instance: {self.__name}")

def main():
    insect1 = Insect("Bee", 3.2, 0.1, id_number=1, category="Pollinator")
    insect2 = Insect("Ant", 0.03, 0.002, id_number=2, category="Worker")
    insect3 = Insect("Butterfly", 2.1, 0.05, id_number=3, category="Pollinator")

    print(insect1)
    print(insect2)
    print(insect3)

    print("Insect 1 Name:", insect1.get_name())
    print("Insect 2 Speed:", insect2.get_speed())
    print("Insect 3 Weight:", insect3.get_weight())

if __name__ == "__main__":
    main()
