from card import BaseCard
from card import PropertyCard
from card import special_card
from make_graph import MakeGraph
from player import Player


class GameBoard:
    def __init__(self):
        self.cards = []  # This board is an array of all the cards
        self._file = open("Properties.txt", "r")
        self._iterate_file()
        self.players = []

    def get_card(self, index):
        return self.cards[i]

    def _iterate_file(self):
        for line in self._file:
            self.read_string(line)  # processes the string

    def read_string(self, line):
        arr = line.rstrip().split(" ")  # split into different parts
        
        if (arr[0] == "Special"):
            newcard = special_card(arr[1])
        elif (arr[0] == "Property"):
            newcard = PropertyCard(arr[2], arr[1], int(arr[9]), arr[3:9], 0, 0, int(arr[9]) / 2, int(arr[10]))
        elif (arr[0] == "Railroad"):
            newcard = BaseCard(arr[1], 200, [25, 50, 100, 200], 0)
        elif (arr[0] == "Utility"):
            newcard = BaseCard(arr[1], 150, [4*7, 10*7], 0)
                
        self.cards.append(newcard)

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




def most_popular (arr, names, colors):
    figurexvals = []
    figureyvals = []
    for i in range(len(arr)):
        figureyvals.append(100*arr[i]/(sum(arr)-arr[29]))
        figurexvals.append (names[i].get_name())
        print("{:25s}{:10f}".format(figurexvals[i], figureyvals[i]))
    print()
    graph = MakeGraph ()
    graph.draw_figure_no_sort(figurexvals, figureyvals, "Name of Location","Percent Landed", "Most Often Landed Spots", colors)
    graph.show_plts()
    




def makes_money (arr, cards, colors):
    figurexvals = []
    figureyvals = []
    
    for i in range(len(arr)):
        if (cards[i].get_cost() > 0):
           figureyvals.append(cards[i].get_cost()/(int(cards[i].get_house_rents()[0])*arr[i]/(sum(arr)-arr[29])))
           #print (cards[i].get_cost())
           #print (int(cards[i].get_house_rents()[0]))
           #print (arr[i]/(sum(arr)-arr[29]))
           figurexvals.append (cards[i].get_name())
           print("{:25s}{:10f}".format(figurexvals[-1], figureyvals[-1]))
    print()
    graph = MakeGraph (figurexvals, figureyvals, "Name of Location", "Dice Rolls to Make Money Back", "Which Single Properties Earn Their Cost Back Longest", colors)
    graph.show_plts()




def makes_money_all_properties(arr, cards, colors):
    figurexvals = []
    figureyvals = []
    for numhouses in range (5):
        for i in range(len(arr)):
            #print (type(cards [i]))
            if (cards[i].get_cost() > 0 and type(cards[i]) == PropertyCard):
                #print (cards[i].get_name())
                totalcost = cards[i].get_cost()+(numhouses+1)*cards[i].get_house_cost()
                figureyvals.append(totalcost/(int(cards[i].get_house_rents()[numhouses+1]))/arr[i]*(sum(arr)-arr[29]))
                figurexvals.append (cards[i].get_name()+" " + str(numhouses+1)+ " H.")
                print("{:25s}{:10f}".format(figurexvals[-1], figureyvals[-1]))
        print()
    graph = MakeGraph ()
    graph.draw_figure_no_sort(figurexvals, figureyvals, "Name of Location and Number of Houses", "Dice Rolls to Make Money Back", "Optimal House Strategy", colors, 100)
    graph.show_plts()

#def print_into_file (xvals, yvals):



def most_revenue(arr, cards, colors):
    figurexvals = []
    figureyvals = []
    for i in range(len(arr)):
        #print (type(cards [i]))
        if (cards[i].get_cost() > 0 and type(cards[i]) == PropertyCard):
            #print (cards[i].get_name())
            figureyvals.append(int(cards[i].get_house_rents()[0])*arr[i]/(sum(arr)-arr[29]))
            figurexvals.append (cards[i].get_name())
            print("{:25s}{:10f}".format(figurexvals[-1], figureyvals[-1]))
    print()
    graph = MakeGraph(figurexvals, figureyvals, "Name of Location", "Money Per Dice Roll", "Most Money Per Dice Roll On A Single Property", colors)
    graph.show_plts()

#def print_into_file (xvals, yvals):




if __name__ == '__main__':
    array = [0]*40
    for b in range (1000):
        obj = GameBoard()
        player1 = Player(1500)
        obj.players.append(player1)
        for i in range(100):
            obj.compute_round()
            for c in range (len(player1.spaces_landed_on)):
                array[c]+=player1.spaces_landed_on[c]

    color = ["brown", "gray", "brown", "gray", "black", "cyan", "gray", "cyan", "cyan", "gray", "magenta", "black", "magenta", "magenta", "black", "orange","gray","orange","orange", "gray","red","gray", "red","red","black","yellow", "yellow", "black", "yellow", "gray", "green", "green", "gray","green","black", "gray", "blue", "grey", "blue", "tan"]

    print()
    print()

    for card in obj.cards:
        card.set_name(card.get_name().replace("_", " "))
    
    obj.cards[1].set_name("Community Chest #1")
    obj.cards[6].set_name("Chance #1")
    obj.cards[16].set_name("Community Chest #2")
    obj.cards[21].set_name("Chance #2")
    obj.cards[32].set_name("Community Chest #3")
    obj.cards[35].set_name("Chance #3")

    most_popular (array, obj.cards, color)

    color = ["brown","brown","black", "cyan","cyan", "cyan", "magenta", "black", "magenta", "magenta", "black", "orange","orange", "orange","red", "red","red","black","yellow", "yellow", "black", "yellow", "green", "green", "green","black", "blue","blue"]

    makes_money (array, obj.cards, color)


    color = ["brown","brown", "cyan","cyan", "cyan", "magenta","magenta", "magenta", "orange","orange", "orange","red", "red","red","yellow", "yellow", "yellow", "green", "green", "green","blue","blue"]*5
 
    most_revenue(array, obj.cards, color)


    makes_money_all_properties (array, obj.cards, color)

