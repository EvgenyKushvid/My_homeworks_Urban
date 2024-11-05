import  unittest
from pprint import pprint
import inspect

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

class TournamentTest (unittest.TestCase):

    @classmethod
    def setUpClass (self):
        self.all_results = {}


    def setUp (self):
        self.r1 = Runner("Усэйн",10)
        self.r2 = Runner("Андрей",9)
        self.r3 = Runner('Ник', 3)


    @classmethod
    def tearDownClass (self):
        temp = {}
        for key, value in self.all_results.items():
            for k, val in value.items():
                temp[k] = (val.name)
            print(temp)

    def test_race1 (self):
        race = Tournament(90,self.r1,self.r3)
        self.all_results[1] = race.start()
        self.assertTrue(self.all_results[1][2] == self.r3)

    def test_race2 (self):
            race = Tournament(90,self.r2,self.r3)
            self.all_results[2] = race.start()
            self.assertTrue(self.all_results[2][2]== self.r3)


    def test_race3 (self):
            race = Tournament(90,self.r1,self.r2,self.r3)
            self.all_results[3] = race.start()
            self.assertTrue(self.all_results[3][3] == self.r3)






if __name__ == '__main__':
    unittest.main()