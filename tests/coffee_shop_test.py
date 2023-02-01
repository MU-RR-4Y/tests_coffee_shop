import unittest
from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.coffee_shop = CoffeeShop('The Prancing Pony', 100.00)

# testing class attributes

    def test_has_name(self):
        self.assertEqual('The Prancing Pony',self.coffee_shop.name)

    def test_has_till(self):
        self.assertEqual(100.00, self.coffee_shop.till)

# testing class methods

# the 3 As of testing
# Arrange - setup specific to this test
# Act - do the thing you wish to test
# Assert - check that it does wha

    def test_increase_till(self):
        self.coffee_shop.increase_till(10.00)
        self.assertEqual(110.00,self.coffee_shop.till)
