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

    
    def sell_to_customer(self, drink, customer):
        found_drink = self.find_drink(drink.name)
        if found_drink == drink:
            if customer.wallet >= drink.price:
                self.increase_till(drink.price)
                self.remove_drink(drink)
                customer.remove_cash(drink.price)
                customer.add_drink(drink)
                    
                
