import random

class player():
    def __init__(self, money):
        self.properties_owned = []
        self.money=money
        self.current_space = 39
        self.spaces_landed_on = [0]*40
        self.in_jail = False
        self.turns_in_jail = 0

    def get_money(self):
        return self.money

    def get_properties_owned(self):
        return self.properties_owned

    def get_current_space(self):
        return self.current_space

    def roll(self):
        return random.randint(1,6), random.randint(1,6)

    def pay(self, amount):
        self.money -= amount

    def buy_property(self, property):
        self.properties_owned.append(property)
        self.money -= property.get_cost()

    def walk(self,dist):
        if not self.in_jail:
            self.current_space += dist
            if self.current_space > 39:
                self.money += 200
                self.current_space = self.current_space % 40
            self.process_property()

    def move(self):
        if self.in_jail:
            self.turns_in_jail += 1
            die1, die2 = self.roll()
            if die1 == die2:
                self.in_jail = False
                self.walk(die1+die2)
            elif self.turns_in_jail == 3:
                self.money -= 50
                self.in_jail = False
                self.walk(die1 + die2)
        else:
            die1,die2 = self.roll()
            i = 0 # counter for number of double rolls
            while (die1 == die2 and i < 3):
                self.current_space = (self.current_space + die1+die2)
                i+=1
                die1,die2 = self.roll()
            if (i == 3):
                self.go_to_jail()
            else:
                self.current_space = (self.current_space + die1+die2)

        if self.current_space > 39:
            self.money += 200
            self.current_space = self.current_space% 40

        #print(self.current_space)
        self.spaces_landed_on[self.current_space] += 1


    def process(self, card):
        if card.get_name() =="Go":
            self.money += 200
        elif card.get_name() == "Go_To_Jail":
            self.go_to_jail()
        elif card.get_name() == "Chance":
            self.draw_chance_card()
        elif card.get_name() == "Community_Chest":
            self.draw_community_chest_card()
        else:
            self.process_property_card()


    def go_to_jail (self):
        self.current_space = 9
        self.in_jail = True

    def process_property_card(self):
        print ("dummy")

    def draw_chance_card(self):
        print ("dummy")
    def draw_community_chest_card(self):
        print("dummy")
