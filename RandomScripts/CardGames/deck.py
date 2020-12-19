# deck class for instansiating a standard 52 card deck
# Written by: Piero Orderique
# 12/19/2020

from card import Card
from random  import randint, shuffle

class Deck():
    def __init__(self) -> None:
        """Creates 52 card deck."""
        self.deck = [Card(rank, suit) for rank in Card.ranks for suit in Card.suits]

    def __str__(self) -> str:
        readableDeck = [str(c) for c in self.deck]
        return str(readableDeck)

    def swap(self, idx1, idx2) -> None:
        """Swaps the positions of the 2 cards in the deck."""
        self.deck[idx1], self.deck[idx2] = self.deck[idx2], self.deck[idx1]

    def shuffle(self, *, times):
        """Performs specified number of random swaps in the deck."""
        for i in range(times):
            idx1 = randint(0,len(self.deck)-1)
            idx2 = randint(0,len(self.deck)-1)
            # print('cards swapped {} <-> {}'.format(self.deck[idx1], self.deck[idx2]))
            self.swap(idx1,idx2)

    def full_shuffle(self):
        """
        Completes a FULL shuffle on the deck.

        Experimental (not sure how accurate this is):
        For a suffle to be considered "full," we want the probability that no card 
        is in the same place that it started to be around 0.5
        > Let R = # cards in same spot after shuffle
        > We want Pr(R = 0) ~ 0.5 (OR P(R >= 1) <= 0.5)
            > Using Chernoff: P(R >= cEx[R]) <=  e^(-clnc+1-c)
                > Ex[R] = Ex[R_1] + ... + Ex[R_52] 
                    > where R_i = 0 if card i changed spot 1 if it stayed in place
                    > P(R_i = 1) = 1 - Pr(R_i = 0) = 1 - 51/(52)^2
                    > Ex[R_i] = 1 - 51/(52)^2 so Ex[R] =  (52^2 - 51)/52 = 51
                > cEx[R] = 1 so c = 1/51
                > P(R >= cEx[R]) <=  e^(-clnc+1-c) = 0.999
                > 0.999^t = 0.5 -> t = 693 times -->This is how many times we will run 
        """
        times = 693
        self.shuffle(times=times)

    def sort(type = 'bysuit', order = 'ascending'):
        """sorts deck by suit - [all Hs, Ss, Ds, Cs]"""
        pass

# debugging   
if __name__ == "__main__":
    deck1 = Deck()
    print("\nORIGINAL DECK: \n" + str(deck1)) # before swap
    print('---'*10)
    deck1.full_shuffle()
    print(deck1)
