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

    def test_walk (self):
        run = Runner('run')
        for i in range(10):
            run.walk()
        self.assertEqual(run.distance,50)

    def test_run  (self):
        run = Runner('run')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)
    def test_challenge (self):
        r1 = Runner('r1')
        r2 = Runner('r2')
        for i in range(10):
            r2.walk()
            r1.run()
        self.assertNotEqual(r1.distance, r2.distance)

if __name__ == '__main__':
    unittest.main()
