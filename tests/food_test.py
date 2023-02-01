import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food_1 = Food('Cookie', 5, 1)
        self.food_2 = Food('Muffin', 10, 2)
        self.food_3 = Food('Cake', 15, 3)

    def test_food_name(self):
        self.assertEqual('Cookie', self.food_1.name)

    def test_price_name(self):
        self.assertEqual(10, self.food_2.price)

    def test_rejuvenation_level_name(self):
        self.assertEqual(3, self.food_3.rejuvenation_level)

    