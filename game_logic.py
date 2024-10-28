"""
Game logic functions for Blackjack
"""

def calculate_hand_value(hand):
    """
    Calculate the value of a hand, handling Aces properly
    """
    value = 0
    aces = 0
    
    for card in hand:
        if card.rank == 'Ace':
            aces += 1
        value += card.value()
    
    # Adjust for Aces if total value is over 21
    while value > 21 and aces > 0:
        value -= 10  # Convert Ace from 11 to 1
        aces -= 1
        
    return value

def is_blackjack(hand):
    """Check if hand is a Blackjack (Ace + 10-value card)"""
    return len(hand) == 2 and calculate_hand_value(hand) == 21

def is_bust(hand):
    """Check if hand value exceeds 21"""
    return calculate_hand_value(hand) > 21

def determine_winner(player_hand, dealer_hand):
    """
    Determine the winner between player and dealer
    Returns: 'player', 'dealer', or 'push'
    """
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if is_bust(player_hand):
        return 'dealer'
    elif is_bust(dealer_hand):
        return 'player'
    elif player_value > dealer_value:
        return 'player'
    elif dealer_value > player_value:
        return 'dealer'
    else:
        return 'push'  # Tie