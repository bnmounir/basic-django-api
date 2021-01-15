from django.test import TestCase
from app.calc import add, subtract


class CalcTest(TestCase):

    def test_add_numbers(self):
        ''' test adding two numbers '''
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        ''' test to subtract nums '''
        self.assertEqual(subtract(5, 2), 3)
