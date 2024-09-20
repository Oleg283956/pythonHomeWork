class Vehicle:
    owner = ''
    __model = ''
    __engine_power = 0
    __color = ''
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self,owner,model,color,engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        print(f"Модель: {self.__model}")

    def get_horsepower(self):
        print(f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):
        print(f"Цвет: {self.__color}")

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f"Владелец: {self.owner}")

    def set_color(self,new_color):
        is_color = 0
        for i in self.__COLOR_VARIANTS:
            if str(i).lower() == new_color.lower():
                self.__color = new_color
                is_color = 1
                break
        if is_color == 0:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue',500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
