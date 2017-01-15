import random

class Player:
    def __init__(self, money):
        self.properties_owned = []
        self.money = money
        self.current_space = 39
        self.spaces_landed_on = [0] * 40
        self.in_jail = False
        self.turns_in_jail = 0
        self._chance = []
        self._chest = []
        self.generate_deck()


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

        self.spaces_landed_on[self.current_space] += 1


    def process(self, board):
        positionbefore = self.current_space
        if board[self.current_space].get_name() == "Go_To_Jail":
            self.go_to_jail()
        elif board[self.current_space].get_name() == "Go":
            self.money += 200
        elif board[self.current_space].get_name() == "Chance":
            self.draw_chance_card()
        elif board[self.current_space].get_name() == "Community_Chest":
            self.draw_community_chest_card()
        elif board[self.current_space].get_name() == "Income_Tax":
            self.money -= 200
        elif board[self.current_space].get_name() == "Jail_Cell":
            pass
        elif board[self.current_space].get_name() == "Free_Parking":
            pass
        elif board[self.current_space].get_name() == "Luxury_Tax":
            self.pay (75)
        else:
            self.process_property_card(board[self.current_space])
        if (positionbefore != self.current_space):
            self.process (board)


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
        if self._chance [0][0] == "Go_To_Jail":
            self.go_to_jail()
        elif self._chance[0][0] == "Go_Back":
            self.current_space -= 3
            self.track_space()
        elif self._chance[0][0] == "Pay" and self._chance[0][1] != "x":
            self.pay(int(self._chance[0][1]))
        # Unused
        elif self._chance[0][0] == "Pay" and self._chance[0][1] == "x":
            #XXXXXXXXX
            pass
        elif self._chance[0][0] == "Advance_To":
            before = self.current_space
            self.current_space = int(self._chance[0][1])
            if before > self.current_space:
                self.money += 200
            self.track_space()
        elif (self._chance[0][0] == "House_Thing"):
            houses = 0
            hotels = 0
            for property in self.properties_owned:
                if (property.get_group() != "" and property.get_hotel() > 0):
                    hotels = 1
                elif (property.get_group() != "" and property.get_num_houses() > 0):
                    houses = property.get_num_houses()
            self.pay(100 * hotels + 25 * houses)
        elif self._chance[0][0] == "Advance_To_Nearest":
            if self._chance[0][1] == "Railroad":
                if self.current_space == 6:
                    self.current_space = 14
                elif self.current_space == 21:
                    self.current_space = 24
                elif self.current_space == 35:
                    self.current_space = 4
                    self.money += 200
            else:
                if self.current_space == 6:
                    self.current_space = 11
                elif self.current_space == 21:
                    self.current_space = 27
                elif self.current_space == 35:
                    self.current_space = 11
                    self.money += 200

            self.track_space()

            #TODO Calculate the new price of rent based on the card

        drawn_card = self._chance.pop(0)
        self._chance.append(drawn_card)


    def draw_community_chest_card(self):
        if (self._chest[0][0] == "Pay"):
            self.pay (int(self._chest[0][1]))
        elif (self._chest[0][0] == "Go_To_Jail"):
            self.go_to_jail()
        elif (self._chest[0][0] == "Advance_To"):
            before = self.current_space
            self.current_space = int(self._chest[0][1])
            if before > self.current_space:
                self.money += 200
            self.track_space()
        elif (self._chest[0][0] == "House_Thing"):
            houses = 0
            hotels = 0
            for property in self.properties_owned:
                if (property.get_group() != "" and property.get_hotel() > 0):
                    hotels = 1
                elif (property.get_group() != "" and property.get_num_houses() > 0):
                    houses = property.get_num_houses()
            self.pay (115*hotels+40*houses)

        drawn_card = self._chest.pop(0)
        self._chest.append(drawn_card)


    def mortgage_property(self,property):
        self.money +=property.get_cost()
        property.mortgage()


    def bankrupt(self):
        '''
        sum = 0
        for property in self.properties_owned:
            sum += property.get_cost()/2
        '''
        if (self.money < 0):
            return True
        return False


    def generate_deck(self):
        f = open("ChanceCards.txt", "r")

        for line in f:
            self._chance.append(line.rstrip().split())

        random.shuffle(self._chance)

        f = open("CommunityChest.txt", "r")
		
        for line in f:
            self._chest.append(line.rstrip().split())

        random.shuffle(self._chest)
