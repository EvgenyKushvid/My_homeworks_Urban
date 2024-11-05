import unittest
import tests_12_2
import tests_12_1

testRunner = unittest.TestSuite()
testRunner.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
testRunner.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testRunner)

