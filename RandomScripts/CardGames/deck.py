# deck class for instansiating a standard 52 card deck
# Written by: Piero Orderique
# 12/19/2020

from card import Card
from random  import randint, shuffle

class Deck():
    def __init__(self) -> None:
        """Create 52 card deck"""
        self.deck = [Card(rank, suit) for rank in Card.ranks for suit in Card.suits]

    def __str__(self) -> str:
        readableDeck = [str(c) for c in self.deck]
        return str(readableDeck)

    def swap(self, idx1, idx2) -> None:
        """swaps the positions of the 2 cards in the deck"""
        self.deck[idx1], self.deck[idx2] = self.deck[idx2], self.deck[idx1]

    def shuffle(self, *, times):
        """performs specified number of random swaps in the deck"""
        for i in range(times):
            idx1 = randint(0,len(self.deck)-1)
            idx2 = randint(0,len(self.deck)-1)
            print('cards swapped {} <-> {}'.format(self.deck[idx1], self.deck[idx2]))
            self.swap(idx1,idx2)

    def sort(type = 'bysuit', order = 'ascending'):
        """sorts deck by suit - [all Hs, Ss, Ds, Cs]"""
        pass

# debugging   
if __name__ == "__main__":
    deck1 = Deck()
    print("ORIGINAL DECK: \n"+ str(deck1)) # before swap
    print('---'*10)
    deck1.shuffle(times=100)
    print(deck1)
