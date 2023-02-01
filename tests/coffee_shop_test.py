import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.drink_1 = {'name': "Hot Chocolate", 'price': 20}
        self.drink_2 =  {'name': "Espresso", 'price': 15}
        self.drink_3 = {'name': "Latte", 'price': 10}


        drinks = [self.drink_1, self.drink_2, self.drink_3]
        
        self.coffee_shop = CoffeeShop('The Prancing Pony', 100.00, drinks)
        self.customer = Customer("John Smith", 50)


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

    def test_has_drinks(self):
        self.assertEqual(3,len(self.coffee_shop.drink))

    def test_has_customer_name(self):
        self.assertEqual("John Smith", self.customer.name)
        
    def test_has_customer_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_find_drink(self):
        drink = self.coffee_shop.find_drink("Espresso")
        self.assertEqual(self.drink_2, drink)

    def test_remove_drink(self):
        self.coffee_shop.drink.remove_drink(drink_1)
        self.assertEqual(2,len(self.coffee_shop.drink))