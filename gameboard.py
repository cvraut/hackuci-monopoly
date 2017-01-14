
from card import base_card
from card import property_card
from card import special_card

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
        arr = self.file.readline().rstrip().split(" ") # split into different parts
        if (arr[0] == "Special"):
            newcard = special_card (arr[1])
        elif (arr[0] == "Property"):
            newcard = property_card(arr[2], arr[1], int(arr[9]), arr[3:9], 0, 0, int(arr[9])/2, int(arr[10]))
        elif (arr[0] == "Railroad"):
            newcard = base_card("", arr[1], 200, [25,50,100,200], 0)
        elif (arr[0] == "Utility"):
            newcard = base_card("", arr[1], 150, [4,10], 0)
        self.board.append(newcard)
        print(newcard.get_name())
        

if __name__ == '__main__':
    obj = gameboard()
