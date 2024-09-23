class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):
        if isinstance(new_floor,int):
            if new_floor <= self.number_of_floors:
                 for i in range(1,new_floor+1):
                     print(i)
            else :
                 print('"Такого этажа не существует"')

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


    def __str__(self):
            return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
            return self.number_of_floors

    def __add__(self, other):
        if isinstance(other,House):
            self.number_of_floors = self.number_of_floors + other.number_of_floors
            return  House(self.name,self.number_of_floors)
        else:
            self.number_of_floors = self.number_of_floors + other
            return House(self.name,self.number_of_floors)

    __iadd__ = __add__

    __radd__ = __add__

    def __gt__(self, other):
        if isinstance(other,House):
            return self.number_of_floors > other.number_of_floors
        else:
            return self.number_of_floors > other


    def __ge__(self, other):
        if isinstance(other,House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return self.number_of_floors >= other

    def __lt__(self, other):
        if isinstance(other,House):
            return self.number_of_floors < other.number_of_floors
        else:
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other,House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return self.number_of_floors <= other

    def __ne__(self, other):
        if isinstance(other,House):
            return self.number_of_floors != other.number_of_floors
        else:
            return self.number_of_floors != other

    def __eq__(self, other):
        if isinstance(other,House):
            return self.number_of_floors == other.number_of_floors
        else:
            return self.number_of_floors == other

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)



