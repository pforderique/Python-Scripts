# card class for instansiating card types
# Written by: Piero Orderique
# 12/19/2020

class Card:
    # suits = {hearts, spades, diamonds, clubs}
    # ranks = {2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A}

    # (rank: value) dictionary lookup
    values = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':11, 'Q':12, 'K':13, 'A': 14}

    def __init__(self, rank: str, suit: str,) -> None:
        self.suit = suit
        self.rank = rank
        self.value = self.values[rank]

    def __str__(self) -> str:
        return self.rank+ " of " + self.suit.capitalize()

# testing
if __name__ == "__main__":
    print(Card('J', 'diamonds'))