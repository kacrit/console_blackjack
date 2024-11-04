"""
Hand module for Blackjack game
Handles player and dealer hand management
"""

class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        """Add a card to the hand"""
        self.cards.append(card)
    
    def get_value(self):
        """Calculate the value of the hand, handling Aces appropriately"""
        value = 0
        aces = 0
        
        # Calculate base value and count aces
        for card in self.cards:
            if card.rank == 'Ace':
                aces += 1
            value += card.get_value()
        
        # Adjust for aces (convert 11 to 1 if needed to avoid bust)
        while value > 21 and aces > 0:
            value -= 10  # Convert Ace from 11 to 1
            aces -= 1
        
        return value
    
    def is_blackjack(self):
        """Check if hand is a natural blackjack (Ace + 10-value card)"""
        return len(self.cards) == 2 and self.get_value() == 21
    
    def is_busted(self):
        """Check if hand value exceeds 21"""
        return self.get_value() > 21
    
    def clear(self):
        """Clear all cards from hand"""
        self.cards = []
    
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)