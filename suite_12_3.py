import os
try:
    import unittest
except:
    os.system('pip install unittest')
    import unittest
import tests_12_3

runTestSuite = unittest.TestSuite()
runTestSuite.addTest(unittest.makeSuite(tests_12_3.RunnerTest))
runTestSuite.addTest(unittest.makeSuite(tests_12_3.TournamentTest))

runner1 = unittest.TextTestRunner(verbosity=2)
runner1.run(runTestSuite)