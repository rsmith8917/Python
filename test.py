import unittest

class CalcTests(unittest.TestCase):

	def test_calc_add(self):
		result=2+3
		self.assertEqual(4, result)