#Реализуйте базовый класс Car.
#у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы:
#go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
#40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return "The car went"
    def stop(self):
        return "The car has stopped"
    def turn(self, direction):
        return "The car turned to " + direction

class TownCar(Cars):
    family = None
    def __init__(self, name, speed, color, family = True):
        super().__init__(name, speed, color)
        self.family = family

class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)

lincoln = TownCar('Lincoln', 60, 'black')
print(lincoln.name, lincoln.color, lincoln.speed, lincoln.is_police)
print(lincoln.go(), lincoln.turn('City'), lincoln.stop())
sport = SportCar('BMW', 180, 'red')
work1 = WorkCar('Toyota', 90, 'white', True)
work2 = WorkCar('Nissan', 90, 'white', False)
police = PoliceCar('LADA', 180, 'red')