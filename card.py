from player import player
import random

class BaseCard:
    def __init__(self,name='',cost=0,house_rents=[],num_houses=0):
        #self._group = group
        self._cost = cost
        self._name = name
        self._house_costs = house_rents
        self._num_houses = num_houses
        self._player_owner = None

    def get_group(self):
        return self._group
    def get_cost(self):
        return self._cost
    def get_name(self):
        return self._name
    def get_total_rent(self):
        return self._house_costs[self._num_houses]
    def get_num_houses(self):
        return self._num_houses
    def get_house_rents(self):
        return self._house_costs
    def set_owner(self, player):
        self._player_owner = player
    def get_owner(self):
        return self._player_owner



class PropertyCard(BaseCard):
    def __init__(self,group='',name='',cost=0,house_rents=[],num_houses=0,hotel=0,mortgage_value=0,house_cost=0):
        super().__init__(name,cost,house_rents,num_houses)
        self._group = group
        self._hotel = hotel
        self._mortgage_value = mortgage_value
        self._house_cost = house_cost
    def get_hotel(self):
        return self._hotel
    def get_mortgage_value(self):
        return self._mortgage_value
    def get_house_cost(self):
        return self._house_cost

class SpecialDeck:
	def __init__(self):
		self._chance = []
		self._chest = []
		
		self._chance.append(SpecialCard(0, 'Advance to Go'))
		self._chance.append(SpecialCard(1, 'Go to jail'))
		self._chance.append(SpecialCard(2, 'Advance to Illinois'))
		self._chance.append(SpecialCard(3, 'Advance to St.Charles Place'))
		self._chance.append(SpecialCard(4, 'Advance to Nearest Utility'))
		self._chance.append(SpecialCard(5, 'Advance to Nearest Railroad'))
		self._chance.append(SpecialCard(5, 'Advance to Nearest Railroad '))
		self._chance.append(SpecialCard(6, 'Advance to Reading Railroad '))
		self._chance.append(SpecialCard(7, 'Advance to Boardwalk '))
		self._chance.append(SpecialCard(8, 'Go back 3 spaces'))
		self._chance.append(SpecialCard(9, 'Bank pays you dividend of $50'))
		self._chance.append(SpecialCard(9, 'Pay poor tax of $15'))
		self._chance.append(SpecialCard(9, 'Pay each player $50'))
		self._chance.append(SpecialCard(9, 'Make repairs: $25 per HS $100 per HL '))
		self._chance.append(SpecialCard(9, 'Collect $150'))
		self._chance.append(SpecialCard(9, 'Get out of jail free'))
		
		
		self._chest.append(SpecialCard(0, 'Advance to Go'))
		self._chest.append(SpecialCard(1, 'Go to jail'))
		self._chest.append(SpecialCard(2, 'Bank error in your favour'))
		self._chest.append(SpecialCard(2, 'Doctors fee pay $50'))
		self._chest.append(SpecialCard(2, 'Stock sale collect $50'))
		self._chest.append(SpecialCard(2, 'Get out of jail'))
		self._chest.append(SpecialCard(2, 'Collect $50 from each player'))
		self._chest.append(SpecialCard(2, 'Xmas fund colect $100'))
		self._chest.append(SpecialCard(2, 'Income tax refund collect $20'))
		self._chest.append(SpecialCard(2, 'Collect $10 from each player for your birthday'))
		self._chest.append(SpecialCard(2, 'Life inusrance matures-- collect $100'))
		self._chest.append(SpecialCard(2, 'Pay hospital fees of $100'))
		self._chest.append(SpecialCard(2, 'Pay school fees of $150'))
		self._chest.append(SpecialCard(2, 'Receive $25 consultancy fee'))
		self._chest.append(SpecialCard(2, 'Street repairs: $40 per HS $115 per HL'))
		self._chest.append(SpecialCard(2, 'You inherit $100'))
	
	
	
	def get_chance(self, index):
		if self._chance[index] == 0:
			self._player_owner.advance_to_go()
		elif self._chance[index] == 1:
			self._player_owner.go_to_jail()
		#add in other cases
			
	def get_chest(self, index):
		if self._chest[index] == 0:
			self._player_owner.advance_to_go()
		elif self._chest[index] == 1:
			self._player_owner.go_to_jail()
		# add in other cases
	
		
class SpecialCard:
	def __init__(self, type, label):
		self._type = type
		self._label = label
	
	
	def get_special_card(self):
		return (self._type, self._label)
	

class special_card(BaseCard):
    def __init__ (self, name):
        self._name=name
    def get_name(self):
        return self._name

boardwalk = PropertyCard()
boardwalk.get_group()