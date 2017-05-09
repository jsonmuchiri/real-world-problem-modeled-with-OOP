import unittest

from oop import Drink

class TestDrink(unittest.TestCase):
	def test_describe_string(self):
		self.assertEqual(type(describe('coffee')), str)

	def test_cost_integer(self):
		self.assertEqual(type(cost(23)), int)
