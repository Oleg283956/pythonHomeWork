import os
try:
    import unittest
except:
    os.system('pip install unittest')
    import unittest



import logging
logging.basicConfig(level=logging.INFO,filename='runner_tests.log',filemode='w',encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            self.runner1 = Runner('Вася',-5)
        except ValueError as err:
            logging.warning('Неверная скорость для Runner',exc_info=True)
        for i in range(1,11):
            self.runner1.walk()
        self.assertEqual(self.runner1.distance,50)

    def test_run(self):
        #logging.info("The values of.")
        try:
            self.runner2 = Runner(2)
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner',exc_info=True)

        for i in range(1,11):
            self.runner2.run()
        self.assertEqual(self.runner2.distance,100)

    def test_challenge(self):
        self.runner3 = Runner('Petja',7)
        self.runner4 = Runner('Vasja',8)
        self.runner3.distance = 10
        self.runner4.distance = 20
        for j in range(1,11):
            self.runner3.walk()
            self.runner4.walk()
            self.runner3.run()
            self.runner4.run()
        self.assertNotEqual(self.runner3.distance,self.runner4.distance)

if __name__ == "__main__":
    unittest.main()

