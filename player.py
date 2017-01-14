import random


class Player:
    def __init__(self, money):
        self.properties_owned = []
        self.money = money
        self.current_space = 39
        self.spaces_landed_on = [0] * 40
        self.in_jail = False
        self.turns_in_jail = 0

    def get_money(self):
        return self.money

    def get_properties_owned(self):
        return self.properties_owned

    def get_current_space(self):
        return self.current_space

    def roll(self):
        return random.randint(1, 6), random.randint(1, 6)

    def pay(self, amount):
        self.money -= amount

    def buy_property(self, property):
        self.properties_owned.append(property)
        self.money -= property.get_cost()

    def move(self):
        die1, die2 = self.roll()
        if self.in_jail:
            self.turns_in_jail += 1
            if die1 == die2:
                self.current_space = (self.current_space + die1 + die2)
                self.in_jail = False
            elif self.turns_in_jail >= 3:
                self.money -= 50
                self.current_space = (self.current_space + die1 + die2)
                self.in_jail = False
        else:
            self.current_space = (self.current_space + die1 + die2)
            self.track_space()
        return die1, die2

    def track_space(self):
        if self.current_space > 39:
            self.money += 200
            self.current_space = self.current_space % 40

        # print(self.current_space)
        self.spaces_landed_on[self.current_space] += 1

    def process(self, card):
        if card.get_name() == "Go_To_Jail":
            self.go_to_jail()
        elif card.get_name() == "Go":
            self.money += 200
        elif card.get_name() == "Chance":
            self.draw_chance_card()
        elif card.get_name() == "Community_Chest":
            self.draw_community_chest_card()
        elif card.get_name() == "Income_Tax":
            self.money -= 200
        elif card.get_name() == "Jail_Cell":
            pass
        elif card.get_name() == "Free_Parking":
            pass
        elif card.get_name() == "Luxury_Tax":
            pass
        else:
            self.process_property_card(card)

    def go_to_jail(self):
        self.current_space = 9
        self.in_jail = True
        self.track_space()
        self.turns_in_jail = 0

    def advance_to_go(self):
        self.current_space = 39
        self.money += 200

    def process_property_card(self, card):
        if (card.get_owner() != None):
            self.money -= card.get_rents()[card.get_num_houses()]
            card.get_owner().money += card.get_rents()[card.get_num_houses()]

    def draw_chance_card(self):
        '''
        if self._chance[index] == 0:
            self.advance_to_go()
        elif self._chance[index] == 1:
            self.advance_to_illinois()
        elif self._chance[index] == 1:
            self.go_to_jail()
        '''
        pass
        # add in other cases


    def draw_community_chest_card(self):
        '''
        if self._chest[index] == 0:
            self.advance_to_go()
        elif self._chest[index] == 1:
            self..go_to_jail()
        '''
        pass
        # add in other cases




    def bankrupt(self):
        '''
        sum = 0
        for property in self.properties_owned:
            sum += property.get_cost()/2
        '''
        if (self.money < 0):
            return True
        return False