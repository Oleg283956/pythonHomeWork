class Animal():
    alive = True
    fed = False
    name = ''

    def __init__(self,name):
        self.name = name

    def eat(self, food):
        self.food = food
        self.res = ''
        str_sjel = ' съел '
        if isinstance(self.food,Fruit):
            if self.food.edible == True:
                self.fed = True
            else:
                self.alive = False
                str_sjel = ' не стал есть '
        if isinstance(self.food,Flower):
            if self.food.edible == True:
                self.fed = True
            else:
                self.alive = False
                str_sjel = ' не стал есть '
        self.res = str(self.name) +str_sjel+ str(self.food.name)
        print(self.res)



class Plant:
    edible = False
    name = ''
    def __init__(self,name):
        self.name = name


class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)