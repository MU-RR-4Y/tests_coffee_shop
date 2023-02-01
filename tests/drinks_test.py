import unittest

from src.drinks import Drinks

class TestDrinks(unittest.TestCase):
    def setUp(self):
        
        self.drink_1 = Drinks("Hot Chocolate", 20.00, 1)
        self.drink_2 = Drinks("Espresso", 15.00, 3)
        self.drink_3 = Drinks("Latte", 10.00, 2)

         

    def test_check_drink_name(self):
        self.assertEqual("Hot Chocolate", self.drink_1.name)

    def test_check_drink_price(self):
        self.assertEqual(15.00, self.drink_2.price)

    def test_check_drink_caffine_level(self):
        self.assertEqual(2, self.drink_3.caffine_level)