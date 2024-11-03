"""
Main Blackjack game file
"""

from cards import Deck, Card
from game_logic import calculate_hand_value, is_blackjack, is_bust, determine_winner

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = []
        self.dealer_hand = []
        
    def start_round(self):
        """Start a new round of Blackjack"""
        self.player_hand = []
        self.dealer_hand = []
        
        # Deal initial cards
        for _ in range(2):
            self.player_hand.append(self.deck.deal())
            self.dealer_hand.append(self.deck.deal())
            
    def display_hands(self, show_all_dealer_cards=False):
        """Display the current hands"""
        print("\n" + "="*50)
        print("DEALER'S HAND:")
        if show_all_dealer_cards:
            for card in self.dealer_hand:
                print(f"  {card}")
            print(f"  Total: {calculate_hand_value(self.dealer_hand)}")
        else:
            print(f"  {self.dealer_hand[0]}")
            print("  [Hidden Card]")
            
        print("\nYOUR HAND:")
        for card in self.player_hand:
            print(f"  {card}")
        print(f"  Total: {calculate_hand_value(self.player_hand)}")
        print("="*50)
        
    def player_turn(self):
        """Handle player's turn"""
        while True:
            self.display_hands()
            
            if is_bust(self.player_hand):
                print("BUST! You went over 21.")
                return
                
            if is_blackjack(self.player_hand):
                print("BLACKJACK!")
                return
                
            action = input("\nDo you want to (H)it or (S)tand? ").lower()
            
            if action in ['h', 'hit']:
                self.player_hand.append(self.deck.deal())
                print(f"You drew: {self.player_hand[-1]}")
                
            elif action in ['s', 'stand']:
                print("You stand.")
                break
            else:
                print("Invalid input. Please enter 'H' for Hit or 'S' for Stand.")
                
    def dealer_turn(self):
        """Handle dealer's turn (dealer hits on 16 or less, stands on 17 or more)"""
        print("\nDealer's turn...")
        self.display_hands(show_all_dealer_cards=True)
        
        while calculate_hand_value(self.dealer_hand) < 17:
            print("Dealer hits...")
            self.dealer_hand.append(self.deck.deal())
            print(f"Dealer drew: {self.dealer_hand[-1]}")
            self.display_hands(show_all_dealer_cards=True)
            
        if is_bust(self.dealer_hand):
            print("Dealer BUSTS!")
        else:
            print("Dealer stands.")
            
    def play_round(self):
        """Play one complete round of Blackjack"""
        self.start_round()
        
        # Check for immediate blackjack
        player_blackjack = is_blackjack(self.player_hand)
        dealer_blackjack = is_blackjack(self.dealer_hand)
        
        if player_blackjack and dealer_blackjack:
            self.display_hands(show_all_dealer_cards=True)
            print("Both have Blackjack! It's a push.")
            return 'push'
        elif player_blackjack:
            self.display_hands(show_all_dealer_cards=True)
            print("Blackjack! You win!")
            return 'player'
        elif dealer_blackjack:
            self.display_hands(show_all_dealer_cards=True)
            print("Dealer has Blackjack! You lose.")
            return 'dealer'
        
        # Normal gameplay
        self.player_turn()
        
        if not is_bust(self.player_hand):
            self.dealer_turn()
            
        # Determine winner
        winner = determine_winner(self.player_hand, self.dealer_hand)
        
        self.display_hands(show_all_dealer_cards=True)
        
        if winner == 'player':
            print("🎉 You win!")
        elif winner == 'dealer':
            print("💸 Dealer wins!")
        else:
            print("🤝 It's a push!")
            
        return winner

def main():
    """Main game loop"""
    print("Welcome to Blackjack!")
    print("Get as close to 21 as possible without going over!\n")
    
    game = BlackjackGame()
    
    while True:
        result = game.play_round()
        
        play_again = input("\nDo you want to play another round? (Y/N): ").lower()
        if play_again not in ['y', 'yes']:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()