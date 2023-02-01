import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drinks import Drinks
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John Smith", 50.00, 20, 2)

        self.drink_1 = Drinks("Hot Chocolate", 20.00, 1)
        self.drink_2 = Drinks("Espresso", 15.00, 3)
        self.drink_3 = Drinks("Latte", 10.00, 2)


        drinks = [self.drink_1, self.drink_2, self.drink_3]

        self.food_1 = Food('Cookie', 5, 1)
        self.food_2 = Food('Muffin', 10, 2)
        self.food_3 = Food('Cake', 15, 3)


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

    def test_customer_age(self):
        self.assertEqual(20,self.customer.age)

    def test_customer_energy_levels(self):
        self.assertEqual(2, self.customer.energy_level)

    def test_customer_energy_level_increase(self):
        self.customer.add_drink(self.drink_1)
        self.customer.increase_energy_level(self.drink_1)
        self.assertEqual(3, self.customer.energy_level)

    def test_customer_add_food(self):
        self.customer.add_food(self.food_1)
        self.assertEqual(1, len(self.customer.food))

    def test_customer_decrease_enegy(self):
        self.customer.add_food(self.food_1)
        self.customer.decrease_energy(self.food_1)
        self.assertEqual(1,self.customer.energy_level)

        
    
    
    


        
