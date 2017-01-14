

class ga_worker:
    def __init__(self):
        self._genes = [0]*40
        self._phenotype = []
        self.player()

    def buy_property1(self,gene):
        '''returns a # dictating what & how much to buy:
        0->don't buy
        1->buy prop if it is one space away from corner
        2->buy prop if it is two space away from corner
        3->buy prop if it is three space away from corner
        4->buy prop if it is four space away from corner
        5->buy prop if it is one or two space away from corner
        6->buy prop if it is three or four space away from corner
        '''
        return gene
    def buy_property2(self,gene):
        '''
        0->don't buy
        1->buy property and try to buy 2 houses
        2->buy property and try to buy house
        3->buy if its the last property in the set
        4->buy if its there are two properties unclaimed in the set
        5->buy if there are 3 prop's unclaimed in the set
        6->buy property regardless
        '''
        return gene
    def buy_property3(self,gene):
        '''
        0->don't buy period
        1->don't buy if property type is owned
        2->don't buy if two away from completing set
        3->don't buy if it completes the set
        4->buy if it completes the set
        5->buy if type is already owned
        6->buy regardless
        '''
        return gene

    def prioritize_property(self,gene):
        '''
        0->doesn't buy
        1->buys using 1st method
        2->buys using 2nd method
        3->buys using 3rd method
        4->buys using combo of 1&2
        5->buys using combo of 2&3
        6->buys using combo of 1&3
        '''
        if gene == 0:
            return 0,0
        elif gene == 1:
            return self.buy_property1(gene),0
        elif gene == 2:
            return self.buy_property2(gene),0
        elif gene == 3:
            return self.buy_property3(gene),0
        elif gene == 4:
            return self.buy_property1(gene),self.buy_property2(gene)
        elif gene == 5:
            return self.buy_property2(gene),self.buy_property3(gene)
        elif gene == 6:
            return self.buy_property1(gene),self.buy_property3(gene)

    def buy_house1(self,gene):
        '''
        0->don't buy
        1->don't buy if the cost of the house is more than 15% of bank
        2->don't buy if the cost of the house is more than 30% of bank
        3->don't buy if the cost of the house is more than 45% of bank
        4->don't buy if the cost of the house is more than 60% of bank
        5->don't buy if the cost of the house is more than 75% of bank
        6->don't buy if the cost of the house is more than 90% of bank
        '''
        return gene
    def buy_house2(self,gene):
        '''
        0->don't buy
        1->buy if players are within 2 squares
        2->buy if players are within 4 squares
        3->buy if players are within 6 squares
        4->buy if players are within 8 squares
        5->buy if players are within 10 squares
        6->buy if players are within 12 squares
        '''
        return gene
    def buy_house3(self,gene):
        '''
        0->don't buy
        1->buy if there are zero houses on property
        2->buy if only 1 house on property
        3->buy if at most 2 houses on property
        4->buy if at most 3 houses on property
        5->buy if at most 4 houses on property
        6->buy regardless
        '''
        return gene

    def prioritize_house(self,gene):
        '''
            0->doesn't buy
            1->buys using 1st method
            2->buys using 2nd method
            3->buys using 3rd method
            4->buys using combo of 1&2
            5->buys using combo of 2&3
            6->buys using combo of 1&3
            '''
        if gene == 0:
            return 0, 0
        elif gene == 1:
            return self.buy_house1(gene), 0
        elif gene == 2:
            return self.buy_house2(gene), 0
        elif gene == 3:
            return self.buy_house3(gene), 0
        elif gene == 4:
            return self.buy_house1(gene), self.buy_house2(gene)
        elif gene == 5:
            return self.buy_house2(gene), self.buy_house3(gene)
        elif gene == 6:
            return self.buy_house1(gene), self.buy_house3(gene)

    def sell1(self,gene):
        '''
         0->sell houses required equal to minimum needed
         1->sell houses equal to 2*minimum needed
         2->sell houses equal to 3*minimum needed
         3->sell houses equal to 4*minimum needed
         4->sell houses equal to 5*minimum needed
         5->sell houses equal to 6*minimum needed
         6->sell all houses
        '''
        return gene
    def sell2(self,gene):
        '''
         0->sell properties from the lowest earners based on rent til min is reached
         1->sell at least 2 properties from lowest rent til min is reached
         2->sell at least 3 lowest properties til min is reached
         3->sell at least 4 lowest properties til min is reached
         4->sell at least 5 lowest properties til min is reached
         5->sell at least 6 lowest properties til min is reached
         6->sell at least 7 lowest properties til min is reached
        '''
        return gene
    def sell3(self,gene):
        '''
        0->sell non-sets until minimum is reached
        1->sell 2 non-sets until minimum is reached
        2->sell sets until minimum is reached
        3->sell 2 sets until minimum is reached
        4->sell 1 set and 1 non-set until minimum is reached
        '''