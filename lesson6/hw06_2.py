#Реализовать класс Road (дорога).
#определить атрибуты: length (длина), width (ширина);
#значения атрибутов должны передаваться при создании экземпляра класса;
#атрибуты сделать защищёнными;
#пределить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#спользовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной
#в 1 см*число см толщины полотна;
#проверить работу метода.
#Например: 20 м*5000 м*25 кг*5 см = 12500 т

class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Create road_to_village object')

    def intake(self):
        self.weigth = 25
        self.tickness = 0.05
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Need {intake} ton for the building')

road_to_village = Road(20000, 6)
road_to_village.intake()

