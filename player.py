import random

class player():
    def __init__(self, money):
        self.properties_owned = []
        self.money=money
        self.current_space = 39
        self.spaces_landed_on = [0]*40

    def get_money(self):
        return self.money

    def get_properties_owned(self):
        return self.properties_owned

    def get_current_space(self):
        return self.current_space

    def roll(self):
        return random.randint(1,6)+random.randint(1,6)

    def pay(self, amount):
        self.money -= amount

    def buy_property(self, property):
        self.properties_owned.append(property)
        self.money -= property.get_cost()

    def move(self):
        spaces = self.roll()
        self.current_space = (self.current_space + spaces) % 40
        #print(self.current_space)
        self.spaces_landed_on[self.current_space] += 1