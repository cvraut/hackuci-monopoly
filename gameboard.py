
from card import base_card
from card import property_card

class gameboard:
    def __init__(self):
        self.board = [] # This board is an array of all the cards
        self.open_file()
        self.iterate_file()
        
    def open_file (self):
        self.file = open ("Property.txt", "r") # opens the readable file
    
    def iterate_file (self):
        for i in range (0, 40):
            self.read_string () # processes the string

    def read_string (self):
        arr = self.file.readline().replace("\n","").split(" ") # split into different parts
        if (arr[0] == "Special"):
            newcard = (arr[1])
        elif (arr[0] == "Property"):
            newcard = self.new_property_card(arr)
        elif (arr[0] == "Railroad"):
            newcard = self.new_railroad_card(arr)
        elif (arr[0] == "Utility"):
            newcard = self.new_utility_card(arr)
        self.board.append(newcard)
        #print (newcard)

    def new_property_card(self, arr):
        return arr[1]
    def new_railroad_card(self, arr):
        return arr[1]
    def new_utility_card(self, arr):
        return arr[1]

if __name__ == '__main__':
    obj = gameboard()
