from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(5,1)
        self.assertEqual(res,6)

    def test_substract_numbers(self):
        res = calc.substract(5,1)
        self.assertEqual(res,4)