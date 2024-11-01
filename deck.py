"""
Deck module for Blackjack game
Handles card deck creation and management
"""

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def get_value(self):
        """Get the numerical value of the card"""
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif self.rank == 'Ace':
            return 11  # Ace handled specially in Hand class
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()
    
    def create_deck(self):
        """Create a standard 52-card deck"""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
    
    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.cards)
    
    def deal(self):
        """Deal one card from the deck"""
        if len(self.cards) == 0:
            self.create_deck()
            self.shuffle()
            print("Deck reshuffled!")
        return self.cards.pop()
    
    def __len__(self):
        return len(self.cards)