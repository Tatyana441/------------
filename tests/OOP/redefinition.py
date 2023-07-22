# создание класса Vehicle
class Vehicle:
    def print_details(self):
        print("Это родительский метод из класса Vehicle")

# создание класса, который наследует Vehicle
class Car(Vehicle):
    def print_details(self):
        print("Это дочерний метод из класса Car")

# создание класса Cycle, который наследует Vehicle
class Cycle(Vehicle):
    def print_details(self):
        print("Это дочерний метод из класса Cycle")

car_a = Vehicle()
car_a.print_details()

car_b = Car()
car_b.print_details()

car_c = Cycle()
car_c.print_details()