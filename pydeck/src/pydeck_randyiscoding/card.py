# --------------------------------------------------------
# Name: Randy Easton
# Date: 8/1/2025
# Assignment: [Insert Assignment Name or Number Here]
# --------------------------------------------------------
# Purpose:
# Constructs the properties of each individual card. Handles card values, suits etc
# --------------------------------------------------------

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def is_wild(self, duceswild=False):
        return duceswild and str(self.rank) == '2'
    def value(self, acehigh=False):
        value_map = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14 if acehigh else 1}
        return value_map.get(self.rank, int(self.rank)) if str(self.rank).isdigit() else value_map.get(self.rank, 0)
