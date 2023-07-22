# создаем класс Car
class Car:
    message1 = "Двигатель заведен"

    def start(self):
        message2 = "Автомобиль заведен"
        return message2


car_a = Car()
print(car_a.message1)