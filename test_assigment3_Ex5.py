import unittest
import numpy as np
from assigment3_Ex5 import equilibrium

def round_alloc(a):
    return np.round(a, 2)

class TestEquilibrium(unittest.TestCase):

    def test1(self):
        prefs = [[9, 1], [1, 9]]
        budgets = [50, 50]
        res = equilibrium(prefs, budgets)
        a = round_alloc(res["allocation"])
        self.assertAlmostEqual(a[0][0], 1.0, delta=0.01)
        self.assertAlmostEqual(a[1][1], 1.0, delta=0.01)

    def test2(self):
        prefs = [[3, 2], [4, 1]]
        budgets = [30, 70]
        res = equilibrium(prefs, budgets)
        total_p = sum(res["prices"])
        total_b = sum(budgets)
        self.assertAlmostEqual(total_p, total_b, delta=0.01)

    def test3(self):
        prefs = [[1, 1, 1], [1, 1, 1]]
        budgets = [50, 50]
        res = equilibrium(prefs, budgets)
        a = round_alloc(res["allocation"])
        for j in range(3):
            self.assertAlmostEqual(a[0][j], 0.5, delta=0.01)
            self.assertAlmostEqual(a[1][j], 0.5, delta=0.01)

    def test4(self):
        prefs = [[10, 0], [5, 0]]
        budgets = [60, 40]
        res = equilibrium(prefs, budgets)
        a = round_alloc(res["allocation"])
        self.assertAlmostEqual(a[0][1] + a[1][1], 1.0, delta=0.01)
        self.assertAlmostEqual(a[0][1], 0.5, delta=0.1)

    def test5(self):
        prefs = [[100, 100], [1, 1]]
        budgets = [100, 1]
        res = equilibrium(prefs, budgets)
        a = round_alloc(res["allocation"])
        self.assertGreater(a[0][0], 0.98)
        self.assertGreater(a[0][1], 0.98)
        self.assertLess(a[1][0], 0.02)

    def test6(self):
        prefs = [[5], [2], [9]]
        budgets = [10, 10, 10]
        res = equilibrium(prefs, budgets)
        a = round_alloc(res["allocation"])
        self.assertAlmostEqual(np.sum(a), 1.0, delta=0.011)

    def test7(self):
        prefs = [[10, 1], [1, 10]]
        budgets = [50, 50]
        res = equilibrium(prefs, budgets)
        a = round_alloc(res["allocation"])
        self.assertAlmostEqual(a[0][0], 1.0, delta=0.01)
        self.assertAlmostEqual(a[1][1], 1.0, delta=0.01)


if __name__ == "__main__":
    unittest.main()
#https://g.co/gemini/share/cc38a2625f47