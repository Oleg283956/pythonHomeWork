import math

class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filled = False

    def __new__(cls, *args, **kwargs):
        args_list = list(args)
        cls.__color = []
        cls.__sides = []
        cls.__color = args_list[0]
        if len(args_list) != cls.sides_count + 1:
            if len(args_list) == 2:
                for i in range(0,cls.sides_count):
                    cls.__sides.append(1)
        if len(args_list) == cls.sides_count + 1:
           for k in range(1,cls.sides_count + 1):
                cls.__sides.append(args_list[k])
        return super().__new__(cls)

    def __init__(self,*args,**kwargs):
        if type(self) == Cube and len(list(args)) == 2:
            Cube.side = list(args)[1]

    def set_sides(self, *new_sides):
        if len(list(new_sides)) == self.sides_count:
            self.__sides = list(new_sides)

    def get_sides(self):
        if type(self) == Cube:
            self.__sides = self.sides
        return self.__sides

    def get_color(self):
        return self.__color

    def __is_valid_color(self,r,g,b):
        res = 0
        res_r =0
        res_g = 0
        res_b = 0
        if isinstance(r,int) and r >= 0 and r <= 255:
            res_r = 1
        if isinstance(g,int) and g >= 0 and g <= 255:
            res_g = 1
        if isinstance(b,int) and b >= 0 and b <= 255:
            res_b = 1
        res = res_r * res_g * res_b
        return res

    def set_color(self,r,g,b):
        is_valid = self.__is_valid_color(r,g,b)
        if is_valid == 1:
            self.__color = []
            self.__color.append(r)
            self.__color.append(g)
            self.__color.append(b)

    def __len__(self):
        p = 0
        for i in self.__sides:
            p += i
        return p


class Circle(Figure):
    sides_count = 1
    __radius = 0
    def get_radius(self):
        rad = 0
        rad = self.__len__()
        rad = rad/(2*math.pi)
        return rad
    def get_square(self):
        if self.__radius == 0:
            square = 0
            rad = 0
            rad = self.get_radius()
            square = rad ** 2 * math.pi
        else:
            square = self.__radius ** 2 * math.pi
        return square


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        square = 0
        p = 0
        p = self.__len__()/2
        tmp_sides = self.get_sides()
        p_not_a = p - tmp_sides[0]
        p_not_b = p - tmp_sides[1]
        p_not_c = p - tmp_sides[2]
        square = math.sqrt(p*p_not_a*p_not_b*p_not_c)
        return square


class Cube(Figure):
    sides_count = 12
    sides = []
    side = 0
    def __init__(self,*args,**kwargs):
        Figure.__init__(self,*args,**kwargs)
        if self.side != 0:
            self.update_sides(self.side)

    def update_sides(self,len_side):
        self.sides = []
        for i in range(0, self.sides_count):
            self.sides.append(self.side)

    def get_volume(self):
        v=0
        for i in self.sides:
            v = i**3
        return v

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())

