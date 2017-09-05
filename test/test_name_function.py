import unittest
from test import get_formatted_name

class NameTestCase(unittest.TestCase):

	def test_first_last(self):
		formatted_name = get_formatted_name("wang","lingcong")
		self.assertEqual(formatted_name,"Wang Lingcong")

	def test_first_middle_last(self):
		formatted_name = get_formatted_name("wang","cong","ling")
		self.assertEqual(formatted_name,"Wang Ling Cong")
unittest.main()