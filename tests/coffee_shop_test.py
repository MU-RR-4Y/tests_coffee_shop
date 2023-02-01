import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drinks import Drinks

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drinks("Hot Chocolate", 20.00, 1)
        self.drink_2 = Drinks("Espresso", 15.00, 3)
        self.drink_3 = Drinks("Latte", 10.00, 2)


        drinks = [self.drink_1, self.drink_2, self.drink_3]
        
        self.coffee_shop = CoffeeShop('The Prancing Pony', 100.00, drinks)
        self.customer = Customer("John Smith", 50.00, 20, 2)


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

    # def test_has_customer_name(self):
    #     self.assertEqual("John Smith", self.customer.name)
        
    # def test_has_customer_wallet(self):
    #     self.assertEqual(50, self.customer.wallet)

    def test_find_drink(self):
        drink = self.coffee_shop.find_drink("Espresso")
        self.assertEqual(self.drink_2, drink)

    def test_remove_drink(self):
        self.coffee_shop.remove_drink(self.drink_1)
        self.assertEqual(2,len(self.coffee_shop.drink))

    # def test_remove_cash_from_customer(self):
    #     self.customer.remove_cash(self.drink_1.price)
    #     self.assertEqual(30, self.customer.wallet)

    # def test_add_drink_to_customer(self):
    #     self.customer.add_drink(self.drink_2)
    #     self.assertEqual(1, len(self.customer.drink))


    def test_sell_drink_to_customer(self):
        self.coffee_shop.sell_to_customer(self.drink_3, self.customer)
        self.assertEqual(2,len(self.coffee_shop.drink))
        self.assertEqual(110.00,self.coffee_shop.till)
        self.assertEqual(40.00, self.customer.wallet)
        self.assertEqual(1, len(self.customer.drink))

    def test_customer_is_over_16__True__(self):
        self.assertEqual(True, self.customer.age>16)

    def test_customer_is_over_16__False__(self):
        self.customer = Customer('David', 50, 12, 1)
        self.assertEqual(False, self.coffee_shop.check_age(self.customer))
    
    def test_customer_energy_level_ok__True(self):
        self.assertEqual(True, self.customer.check_energy_level(self.customer))

    def test_customer_energy_level_ok__False(self):
        self.customer = Customer('David', 50, 12, 3)
        self.assertEqual(False, self.customer.check_energy_level(self.customer))


    # [
    #   "Hot Chocolate" : {
    #         "price" :
    #         "stock" : int
    #         "caffine-levels" : int

    #     }
    # ]