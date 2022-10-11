import unittest
from main import Solver, ERROR


class TestSolverMethods(unittest.TestCase):
    def test_has_suffix(self):
        with self.assertRaises(ERROR):
            Solver.has_suffix('', 'a', 0)
        with self.assertRaises(ERROR):
            Solver.has_suffix('aaaa', 'b', 30)
        with self.assertRaises(ERROR):
            Solver.has_suffix('a+b', 'c', 2)
        with self.assertRaises(ERROR):
            Solver.has_suffix('.', '1', 3)

        self.assertFalse(Solver.has_suffix('ab+c.aba.*.bac.+.+*', 'a', 2))
        self.assertFalse(Solver.has_suffix('1*', 'a', 2))
        self.assertFalse(Solver.has_suffix('1*', 'c', 500))
        self.assertFalse(Solver.has_suffix('a*b+', 'b', 2))
        self.assertFalse(Solver.has_suffix('ab+c+', 'b', 13))
        self.assertFalse(Solver.has_suffix('ab.c.', 'c', 2))
        self.assertFalse(Solver.has_suffix('ab+c.', 'b', 1))
        self.assertFalse(Solver.has_suffix('ab+c.bc+a.+ca+b.+*', 'b', 3))

        self.assertTrue(Solver.has_suffix('acb..bab.c.*.ab.ba.+.+*a.', 'c', 0))
        self.assertTrue(Solver.has_suffix('1*', 'a', 0))
        self.assertTrue(Solver.has_suffix('a*b+', 'b', 1))
        self.assertTrue(Solver.has_suffix('ab+*1.', 'b', 3))
        self.assertTrue(Solver.has_suffix('ab+c+', 'b', 1))
        self.assertTrue(Solver.has_suffix('ab+c+*', 'b', 100))
        self.assertTrue(Solver.has_suffix('ab+c.', 'b', 0))
        self.assertTrue(Solver.has_suffix('ab+c.bc+a.+ca+b.+*', 'a', 1))

if __name__ == '__main__':
    unittest.main()
