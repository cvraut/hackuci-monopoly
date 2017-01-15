from card import BaseCard
from card import PropertyCard
from card import special_card
from player import Player


class GameBoard:
    def __init__(self):
        self.cards = []  # This board is an array of all the cards
        self.open_file()
        self.iterate_file()
        self.players = []

    def get_card(self, index):
        return self.cards[i]

    def open_file(self):
        self.file = open("Properties.txt", "r")  # opens the readable file

    def iterate_file(self):
        for i in range(0, 40):
            self.read_string()  # processes the string

    def read_string(self):
        arr = self.file.readline().rstrip().split(" ")  # split into different parts
        if (arr[0] == "Special"):
            newcard = special_card(arr[1])
        elif (arr[0] == "Property"):
            newcard = PropertyCard(arr[2], arr[1], int(arr[9]), arr[3:9], 0, 0, int(arr[9]) / 2, int(arr[10]))

        elif (arr[0] == "Railroad"):
            newcard = BaseCard(arr[1], 200, [25, 50, 100, 200], 0)

        elif (arr[0] == "Utility"):
            newcard = BaseCard(arr[1], 150, [4, 10], 0)

        self.cards.append(newcard)
        # print(newcard.get_name())

    def compute_round(self):
        for player in self.players:

            boolbefore = player.in_jail
            die1, die2 = player.move()
            player.process(self.cards)
            boolafter = player.in_jail
            i = 0  # counter for number of double rolls
            while (i < 3 and die1 == die2 and boolafter == boolbefore):
                die1, die2 = player.move()
                player.process(self.cards)
                i += 1
                boolafter = player.in_jail
            if (i == 3):
                player.go_to_jail()


def smallest(arr):
     small = 0
     for i in range (1, 40):
         if (arr[small] > arr[i]):
             small = i
     return small



if __name__ == '__main__':
    obj = GameBoard()
    player1 = Player(1500)
    obj.players.append(player1)
    for i in range(1000000):
        obj.compute_round()

    print()
    print()
    for i in range(len(player1.spaces_landed_on)):

        print(100* player1.spaces_landed_on[i] / (sum(player1.spaces_landed_on)-player1.spaces_landed_on[29]))
    print(smallest(player1.spaces_landed_on))
