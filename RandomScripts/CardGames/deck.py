# deck class for instansiating a standard 52 card deck
# Written by: Piero Orderique
# 12/19/2020

from card import Card

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

    def shuffle(self, times = 1):
        """mixes up card order in the deck"""
        pass

    def sort(type = 'bysuit', order = 'ascending'):
        """sorts deck by suit - [all Hs, Ss, Ds, Cs]"""
        pass

# debugging   
if __name__ == "__main__":
    deck1 = Deck()
    print(deck1) # before swap
    print('---'*10)
    deck1.swap(3,51)
    print(deck1) # after swap