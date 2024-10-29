"""
Main Blackjack game - Command line interface
"""

from game_logic import BlackjackGame

def display_hand(hand, is_dealer=False, hide_dealer_card=False):
    """Display the hand with proper formatting"""
    if is_dealer and hide_dealer_card:
        # Show only the first card for dealer initially
        print(f"Dealer's hand: {hand.cards[0]}, [Hidden Card]")
        print(f"Dealer's showing value: {hand.cards[0].value()}")
    else:
        print(f"{'Dealer' if is_dealer else 'Player'}'s hand: {hand}")
        print(f"{'Dealer' if is_dealer else 'Player'}'s value: {hand.get_value()}")

def play_game():
    """Main game loop"""
    print("Welcome to Blackjack!")
    print("=" * 40)
    
    while True:
        # Initialize new game
        game = BlackjackGame()
        game.deal_initial_cards()
        
        # Show initial hands
        display_hand(game.dealer_hand, is_dealer=True, hide_dealer_card=True)
        print("-" * 20)
        display_hand(game.player_hand)
        
        # Check for immediate blackjack
        if game.player_hand.is_blackjack():
            print("\n🎉 Blackjack! You win!")
        else:
            # Player's turn
            while True:
                action = input("\nDo you want to (h)it or (s)tand? ").lower().strip()
                
                if action == 'h':
                    game.player_hit()
                    display_hand(game.player_hand)
                    
                    if game.player_hand.is_busted():
                        print("\n💥 Bust! You went over 21.")
                        break
                elif action == 's':
                    break
                else:
                    print("Please enter 'h' for hit or 's' for stand.")
                    continue
            
            # Dealer's turn (if player didn't bust)
            if not game.player_hand.is_busted():
                print("\n" + "=" * 20)
                print("Dealer's turn:")
                display_hand(game.dealer_hand, is_dealer=True)
                game.dealer_play()
                display_hand(game.dealer_hand, is_dealer=True)
        
        # Determine and display result
        print("\n" + "=" * 40)
        winner = game.determine_winner()
        
        if winner == "player":
            print("🎉 You win!")
        elif winner == "dealer":
            print("💔 Dealer wins!")
        else:
            print("🤝 It's a tie!")
        
        # Ask to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower().strip()
        if play_again != 'y':
            print("Thanks for playing!")
            break
        print("\n" + "=" * 40)

if __name__ == "__main__":
    play_game()