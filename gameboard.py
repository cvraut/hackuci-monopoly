
from card import base_card
from card import property_card
from card import special_card

class gameboard:
    def __init__(self):
<<<<<<< HEAD
        self._board = [] # This board is an array of all the cards
        self._file = open('Property.txt', 'r')
        self.iterate_file()
        

    def iterate_file(self):
        for line in self.file:
            self.read_string(line) # processes the string


    def read_string(self, line):
        arr = line.rstrip().split(' ') # split into different parts
        if (arr[0] == "Special"):
            newcard = special_card(arr[1])
        elif (arr[0] == "Property"):
            newcard = property_card(arr[2], arr[1], int(arr[9]), arr[3:9], 0, 0, int(arr[9])/2, int(arr[10]))
        elif (arr[0] == "Railroad"):
            newcard = base_card("", arr[1], 200, [25,50,100,200], 0)
        elif (arr[0] == "Utility"):
            newcard = base_card("", arr[1], 150, [4,10], 0)
        self._board.append(newcard)
        print(newcard.get_name())
=======
        self._cards = [] # This board is an array of all the cards
        self._file = open('Property.txt', 'r')
        self._iterate_file()

    
    def _iterate_file(self):
        for line in self._file:
            self.read_string(line) # processes the string


    def read_string(self, line):
        arr = line.rstrip().split(" ") # split into different parts
        if (arr[0] == "Special"):
            newcard = special_card (arr[1])
            print (newcard.get_name())
        elif (arr[0] == "Property"):
            newcard = property_card(arr[2], arr[1], int(arr[9]), arr[3:9], 0, 0, int(arr[9])/2, int(arr[10]))
            print (newcard.get_name())
            print (newcard.get_hotel())
            print (newcard.get_mortgage_value())
            print(newcard.get_total_rent())
        elif (arr[0] == "Railroad"):
            newcard = base_card(arr[1], 200, [25,50,100,200], 0)
            print(newcard.get_name())
            print(newcard.get_total_rent())
        else:
            newcard = base_card(arr[1], 150, [4,10], 0)
            print(newcard.get_name())
            print(newcard.get_total_rent())
        self._cards.append(newcard)
        #print(newcard.get_name())
        
>>>>>>> de565b2859a09e889763e365e3d1cd3de614b5ec

if __name__ == '__main__':
    obj = gameboard()
