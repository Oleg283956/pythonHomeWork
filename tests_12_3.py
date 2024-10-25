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
    is_frozen = False
    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        self.runner1 = Runner('RRR')
        for i in range(1,11):
            self.runner1.walk()
        self.assertEqual(self.runner1.distance,50)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        self.runner2 = Runner('ZZZ')
        for i in range(1,11):
            self.runner2.run()
        self.assertEqual(self.runner2.distance,100)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
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


class RunnerT:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name



class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True
    res = []
    resAll = []

    def setUp(self):
        self.run1 = RunnerT('Усэйн', 10)
        self.run2 = RunnerT('Андрей', 9)
        self.run3 = RunnerT('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_start(self):
        self.t_nam1 = Tournament(90, self.run1, self.run3)
        self.t_nam2 = Tournament(90, self.run2, self.run3)
        self.t_nam3 = Tournament(90, self.run1, self.run2, self.run3)

        self.test_distance_begin_rase()
        self.all_results = self.t_nam1.start()
        self.test_last_runner()
        pl1 = self.all_results[1]
        pl2 = self.all_results[2]
        self.res = []
        self.res.append(pl1.name)
        self.res.append(pl2.name)
        self.resAll.append(self.res)

        self.test_distance_begin_rase()
        self.all_results = self.t_nam2.start()
        self.test_last_runner()
        pl1 = self.all_results[1]
        pl2 = self.all_results[2]
        self.res = []
        self.res.append(pl1.name)
        self.res.append(pl2.name)
        self.resAll.append(self.res)

        self.test_distance_begin_rase()
        self.all_results = self.t_nam3.start()
        self.test_last_runner()
        pl1 = self.all_results[1]
        pl2 = self.all_results[2]
        pl3 = self.all_results[3]
        self.res = []
        self.res.append(pl1.name)
        self.res.append(pl2.name)
        self.res.append(pl3.name)
        self.resAll.append(self.res)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_distance_begin_rase(self):
        self.run1.distance = 0
        self.run2.distance = 0
        self.run3.distance = 0
        self.assertEqual(self.run1.distance, 0)
        self.assertEqual(self.run2.distance, 0)
        self.assertEqual(self.run3.distance, 0)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_last_runner(self):
        self.l_all_results = list(self.all_results)
        if len((self.l_all_results)) > 0:
            val = self.all_results.get((len(self.l_all_results)))
            self.assertTrue(val, 'Ник')

    @classmethod
    def tearDownClass(self):
        self.listDict = []
        self.dictTMP = {}
        for i in self.resAll:
            self.resTMP = i
            nomer = 0
            self.dictTMP = {}
            for i in self.resTMP:
                nomer += 1
                self.dictTMP[nomer] = i
            self.listDict.append(self.dictTMP)



