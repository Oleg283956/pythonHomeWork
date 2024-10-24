import os
from wsgiref.validate import assert_

try:
    import unittest
except:
    os.system('pip install unittest')
    import unittest

class Runner:
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
    res = []
    resAll = []
    def setUp(self):
        self.run1 = Runner('Усэйн',10)
        self.run2 = Runner('Андрей',9)
        self.run3 = Runner('Ник',3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def test_start(self):
        self.t_nam1 = Tournament(90,self.run1,self.run3)
        self.t_nam2 = Tournament(90,self.run2,self.run3)
        self.t_nam3 = Tournament(90,self.run1,self.run2,self.run3)

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

    def test_distance_begin_rase(self):
        
        self.run1.distance = 0
        self.run2.distance = 0
        self.run3.distance = 0

        self.assertEqual(self.run1.distance,0)
        self.assertEqual(self.run2.distance,0)
        self.assertEqual(self.run3.distance,0)



    def test_last_runner(self):
        self.l_all_results = list(self.all_results)
        if len((self.l_all_results)) > 0:
            val = self.all_results.get((len(self.l_all_results)))
            self.assertTrue(val,'Ник')


    @classmethod
    def tearDownClass(self):
        self.listDict = []
        self.dictTMP =  {}
        for i in self.resAll:
            self.resTMP = i
            nomer = 0
            self.dictTMP = {}
            for i in self.resTMP:
                nomer += 1
                self.dictTMP[nomer] = i
            self.listDict.append(self.dictTMP)
        for race in self.listDict:
            print(race)



if __name__ == "__main__":
    unittest.main()


