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

    def shuffle(self, times = 1):
        """mixes up card order in the deck"""
        pass

    def sort(type = 'bysuit', order = 'ascending'):
        """sorts deck by suit - [all Hs, Ss, Ds, Cs]"""
        pass
        
if __name__ == "__main__":
    deck1 = Deck()
    print(deck1)