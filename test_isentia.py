import unittest
import os
from isentia import *

class ApiHelperTestCase(unittest.TestCase):

	def test_star_wars_characters_not_null(self):
		url = "https://swapi.co/api/people/"
		obj = ApiHelper()
		star_chars_list_final=obj.star_wars_characters(url)
		self.assertTrue(star_chars_list_final)

    
if __name__ == '__main__':
	unittest.main()