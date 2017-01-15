import random

class BaseCard:
    def __init__(self, name='', cost=0, house_rents=[], num_houses=0,mortagage=False):
        self._cost = cost
        self._name = name
        self._house_costs = house_rents
        self._num_houses = num_houses
        self._player_owner = None
        self._mortgage = mortagage


    def get_mortgage(self):
        return self._mortgage
		

    def mortgage(self):
        self._mortgage = True


    def unmortgage(self):
        self._mortgage = False

    
    def get_mortgage(self):
        return self._mortgage
    
    
    def mortgage(self):
        self._mortgage = True
    
    
    def unmortgage(self):
        self._mortgage = False

    
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


    def set_name(self, new_name):
        self._name = new_name


    def get_owner(self):
        return self._player_owner


class PropertyCard(BaseCard):
    def __init__(self, group='', name='', cost=0, house_rents=[], num_houses=0, hotel=0, mortgage_value=0,
                 house_cost=0):
        super().__init__(name, cost, house_rents, num_houses)
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



class special_card(BaseCard):
    def __init__(self, name):
        self._name = name


    def get_name(self):
        return self._name


boardwalk = PropertyCard()
boardwalk.get_group()