"""
Card and Deck classes for Blackjack game
"""

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def value(self):
        """Return the Blackjack value of the card"""
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif self.rank == 'Ace':
            return 11  # Ace starts as 11, can be reduced to 1 if needed
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        """Create a standard 52-card deck"""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
                
    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.cards)
        
    def deal(self):
        """Deal one card from the deck"""
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            # If deck is empty, create a new shuffled deck
            self.build()
            self.shuffle()
            return self.cards.pop()