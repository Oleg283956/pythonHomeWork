import os
try:
    import unittest
except:
    os.system('pip install unittest')
    import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        self.runner1 = Runner('RRR')
        for i in range(1,11):
            self.runner1.walk()
        self.assertEqual(self.runner1.distance,50)

    def test_run(self):
        self.runner2 = Runner('ZZZ')
        for i in range(1,11):
            self.runner2.run()
        self.assertEqual(self.runner2.distance,100)

    def test_challenge(self):
        self.runner3 = Runner('Petja')
        self.runner4 = Runner('Vasja')
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


