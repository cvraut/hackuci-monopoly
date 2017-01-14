class base_card:
    def __init__(self,group='',name='',cost=0,rent=0,house_rents=[],num_houses=0):
        self._group = group
        self._cost = cost
        self._name = name
        self._rent = rent
        self._house_costs = house_rents
        self._num_houses = num_houses

    def get_group(self):
        return self._group
    def get_cost(self):
        return self._cost
    def get_name(self):
        return self._name
    def get_rent(self):
        return self._rent
    def get_total_rent(self):
        return self._house_rents[self._num_houses]
    def get_num_houses(self):
        return self._num_houses
    def get_house_rents(self):
        return self._house_rents

    def set_num_houses(self,num):
        self._num_houses = num


class property_card(base_card):
    def __init__(self,group='',name='',cost=0,rent=0,house_rents=[],num_houses=0,hotel=0,mortgage_value=0,house_cost=0,hotel_cost=0):
        super.__init__(self,group,name,cost,rent,house_rents,num_houses)
        self._hotel = hotel
        self._mortgage_value = mortgage_value
        self._house_cost = house_cost
        self._hotel_cost = hotel_cost
    def get_hotel(self):
        return self._hotel
    def get_mortgage_value(self):
        return self._mortgage_value
    def get_house_cost(self):
        return self._house_cost
    def get_hotel_cost(self):
        return self._hotel_cost

    def set_hotel(self,hotel):
        self._hotel = hotel




boardwalk = property_card()
boardwalk.get_group()