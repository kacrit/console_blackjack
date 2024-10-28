"""
Game logic for Blackjack
"""

class Hand:
    def __init__(self):
        self.cards = []
        
    def add_card(self, card):
        """Add a card to the hand"""
        self.cards.append(card)
        
    def get_value(self):
        """Calculate the total value of the hand, handling Aces properly"""
        value = 0
        aces = 0
        
        for card in self.cards:
            card_value = card.value()
            value += card_value
            if card.rank == 'Ace':
                aces += 1
                
        # Adjust for Aces if total value is over 21
        while value > 21 and aces > 0:
            value -= 10  # Convert Ace from 11 to 1
            aces -= 1
            
        return value
    
    def is_blackjack(self):
        """Check if hand is a blackjack (Ace + 10-value card)"""
        return len(self.cards) == 2 and self.get_value() == 21
    
    def is_busted(self):
        """Check if hand value exceeds 21"""
        return self.get_value() > 21
    
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

class BlackjackGame:
    def __init__(self):
        from cards import Deck
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        
    def deal_initial_cards(self):
        """Deal initial two cards to player and dealer"""
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())
    
    def player_hit(self):
        """Player draws another card"""
        self.player_hand.add_card(self.deck.deal())
        return self.player_hand.get_value()
    
    def dealer_play(self):
        """Dealer plays according to standard rules (hit until 17 or higher)"""
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.deal())
        return self.dealer_hand.get_value()
    
    def determine_winner(self):
        """Determine the winner of the game"""
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()
        
        if self.player_hand.is_busted():
            return "dealer"
        elif self.dealer_hand.is_busted():
            return "player"
        elif player_value > dealer_value:
            return "player"
        elif dealer_value > player_value:
            return "dealer"
        else:
            return "tie"