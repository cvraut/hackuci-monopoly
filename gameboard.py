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
            player.process(self.cards[player.get_current_space()])
            boolafter = player.in_jail
            i = 0  # counter for number of double rolls
            while (i < 3 and die1 == die2 and boolafter == boolbefore):
                die1, die2 = player.move()
                player.process(self.cards[player.get_current_space()])
                i += 1
                boolafter = player.in_jail
            if (i == 3):
                player.go_to_jail()


class SpecialDeck:
    def __init__(self):
        self._chance = []
        self._chest = []

        f = open("ChanceCards.txt", "r")
        for line in f:
            self._chance.append(line.strip().split())

        print(self._chance)


        '''
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
        self._chest.append(SpecialCard(2, 200))
        self._chest.append(SpecialCard(2, 50))
        self._chest.append(SpecialCard(2, 'Stock sale collect $50'))
        self._chest.append(SpecialCard(2, 'Get out of jail'))
        self._chest.append(SpecialCard(2, 'Collect $50 from each player'))
        self._chest.append(SpecialCard(2, 'Xmas fund colect $100'))
        self._chest.append(SpecialCard(2, 'Income tax refund collect $20'))
        self._chest.append(SpecialCard(2, 'Collect $10 from each player for your birthday'))
        self._chest.append(SpecialCard(2, 'Life insurance matures-- collect $100'))
        self._chest.append(SpecialCard(2, 'Pay hospital fees of $100'))
        self._chest.append(SpecialCard(2, 'Pay school fees of $150'))
        self._chest.append(SpecialCard(2, 'Receive $25 consultancy fee'))
        self._chest.append(SpecialCard(2, 'Street repairs: $40 per HS $115 per HL'))
        self._chest.append(SpecialCard(2, 'You inherit $100'))
        '''
    '''
  def get_chance(self, index, player):
      if self._chance[index] == 0:
          player.advance_to_go()
      elif self._chance[index] == 1:
          player_owner.go_to_jail()
      #add in other cases

  def get_chest(self, index):
      if self._chest[index] == 0:
          self._player_owner.advance_to_go()
      elif self._chest[index] == 1:
          self._player_owner.go_to_jail()
      # add in other cases
  This is moved into player

      '''


class SpecialCard:
    def __init__(self, type, label):
        self._type = type
        self._label = label

    def get_special_card(self):
        return (self._type, self._label)


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
        print(100* player1.spaces_landed_on[i] / sum(player1.spaces_landed_on))
    print(smallest(player1.spaces_landed_on))
