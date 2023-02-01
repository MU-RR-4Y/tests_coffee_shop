class Customer:
    def __init__(self, name, wallet, age, energy_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy_level = energy_level
        self.drink = []
        self.food = []

    def remove_cash(self,amount):
        self.wallet -= amount

    def add_drink(self, drink):
        self.drink.append(drink)

    def add_food(self, food):
        self.food.append(food)

    def check_energy_level(self,customer):
        if customer.energy_level < 3:
            return True
        else:
            return False

    def increase_energy_level(self, drink):
        self.energy_level += drink.caffine_level

    def decrease_energy(self,food):
        self.energy_level -= food.rejuvenation_level