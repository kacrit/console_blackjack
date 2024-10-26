#!/usr/bin/env python3
"""
Simple Command-line Blackjack Game
Main game logic and user interface
"""

from deck import Deck
from hand import Hand

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.game_over = False
    
    def start_game(self):
        """Start a new game of Blackjack"""
        print("🎰 Welcome to Blackjack! 🎰")
        print("=" * 40)
        
        # Shuffle deck and deal initial cards
        self.deck.shuffle()
        self.player_hand.clear()
        self.dealer_hand.clear()
        
        # Deal initial cards (2 each)
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        
        self.game_over = False
        self.play_round()
    
    def play_round(self):
        """Play one round of Blackjack"""
        # Check for natural blackjack
        if self.player_hand.is_blackjack():
            self.show_hands(show_all=True)
            print("🎉 Blackjack! You win! 🎉")
            return
        
        # Player's turn
        while not self.game_over:
            self.show_hands()
            
            if self.player_hand.is_busted():
                print("💥 Bust! You lose. 💥")
                self.game_over = True
                break
            
            action = input("\nDo you want to (H)it or (S)tand? ").strip().lower()
            
            if action in ['h', 'hit']:
                self.player_hand.add_card(self.deck.deal())
                print(f"You drew: {self.player_hand.cards[-1]}")
                
            elif action in ['s', 'stand']:
                self.dealer_play()
                break
            else:
                print("Invalid input. Please enter 'H' for Hit or 'S' for Stand.")
        
        self.ask_play_again()
    
    def dealer_play(self):
        """Dealer's turn to play"""
        print("\n🃏 Dealer's turn...")
        self.show_hands(show_all=True)
        
        # Dealer hits until 17 or higher
        while self.dealer_hand.get_value() < 17:
            print("Dealer hits...")
            self.dealer_hand.add_card(self.deck.deal())
            print(f"Dealer drew: {self.dealer_hand.cards[-1]}")
            print(f"Dealer's hand: {self.dealer_hand}")
        
        self.determine_winner()
    
    def determine_winner(self):
        """Determine the winner of the round"""
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()
        
        print(f"\n{'='*40}")
        print(f"Your hand: {self.player_hand} (Value: {player_value})")
        print(f"Dealer's hand: {self.dealer_hand} (Value: {dealer_value})")
        print('='*40)
        
        if dealer_value > 21:
            print("🎉 Dealer busts! You win! 🎉")
        elif player_value > dealer_value:
            print("🎉 You win! 🎉")
        elif player_value < dealer_value:
            print("💸 Dealer wins! 💸")
        else:
            print("🤝 It's a tie! 🤝")
        
        self.game_over = True
    
    def show_hands(self, show_all=False):
        """Display the current hands"""
        print(f"\n{'='*40}")
        print(f"Your hand: {self.player_hand} (Value: {self.player_hand.get_value()})")
        
        if show_all:
            print(f"Dealer's hand: {self.dealer_hand} (Value: {self.dealer_hand.get_value()})")
        else:
            # Show only dealer's first card
            print(f"Dealer's hand: {self.dealer_hand.cards[0]} + [Hidden Card]")
        print('='*40)
    
    def ask_play_again(self):
        """Ask player if they want to play again"""
        while True:
            play_again = input("\nDo you want to play again? (Y/N): ").strip().lower()
            if play_again in ['y', 'yes']:
                print("\n" + "="*50)
                self.start_game()
                break
            elif play_again in ['n', 'no']:
                print("Thanks for playing! Goodbye! 👋")
                break
            else:
                print("Please enter 'Y' for Yes or 'N' for No.")

def main():
    """Main function to start the game"""
    game = BlackjackGame()
    game.start_game()

if __name__ == "__main__":
    main()