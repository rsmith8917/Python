import unittest

class CalcTests(unittest.TestCase):

	def test_calc_add(self):
		calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)