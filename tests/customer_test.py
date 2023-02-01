import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drinks import Drinks

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John Smith", 50.00)

        self.drink_1 = Drinks("Hot Chocolate", 20.00)
        self.drink_2 = Drinks("Espresso", 15.00)
        self.drink_3 = Drinks("Latte", 10.00)


        drinks = [self.drink_1, self.drink_2, self.drink_3]


    def test_has_customer_name(self):
        self.assertEqual("John Smith", self.customer.name)

    def test_has_customer_wallet(self):
        self.assertEqual(50, self.customer.wallet)


    def test_remove_cash_from_customer(self):
        self.customer.remove_cash(self.drink_1.price)
        self.assertEqual(30, self.customer.wallet)

    def test_add_drink_to_customer(self):
        self.customer.add_drink(self.drink_2)
        self.assertEqual(1, len(self.customer.drink))
