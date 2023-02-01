class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.drink = []

    def remove_cash(self,amount):
        self.wallet -= amount

    def add_drink(self, drink):
        self.drink.append(drink)