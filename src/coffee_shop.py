class CoffeeShop:
    def __init__(self, name, till, drink):
        self.name = name
        self.till = till
        self.drink = drink


    def increase_till(self, amount):
        self.till += amount

    def find_drink(self, drink_name):
        for drink in self.drink:
            if drink.name == drink_name:
                return drink

    def remove_drink(self, drink):
        # drink_found = self.find_drink(drink)
        self.drink.remove(drink)

    def check_age(self,customer):
        if customer.age >= 16:
            return True
        else:
            return False

    def customer_eligible(self,drink,customer):
        found_drink = self.find_drink(drink.name)
        if found_drink == drink:
            if customer.wallet >= drink.price:
                if (self.check_age(customer)) and (customer.check_energy_level(customer)):
                    return True
                else:
                    return False

    
    def sell_to_customer(self, drink, customer):
        # found_drink = self.find_drink(drink.name)
        # if found_drink == drink:
        #     if customer.wallet >= drink.price:
        #         if self.check_age(customer) == True:
        if self.customer_eligible(drink, customer) == True:
                self.increase_till(drink.price)
                self.remove_drink(drink)
                customer.remove_cash(drink.price)
                customer.add_drink(drink)
