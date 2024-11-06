# Command-line Blackjack Game

A simple Python implementation of the classic Blackjack card game for the command line.

## How to Use

### Prerequisites
- Python 3.6 or higher

### Installation & Running
1. Save all three files in the same directory:
   - `blackjack.py`
   - `deck.py` 
   - `hand.py`

2. Run the game:
   ```bash
   python blackjack.py
   ```

### Game Rules
- The goal is to get a hand value as close to 21 as possible without exceeding it
- Number cards (2-10) are worth their face value
- Face cards (Jack, Queen, King) are worth 10 points
- Aces are worth 11 points, but can be counted as 1 point to avoid busting
- A "natural blackjack" (Ace + 10-value card) wins automatically
- Dealer must hit until they reach 17 or higher

### Gameplay
1. The game starts by dealing 2 cards to both player and dealer
2. Only one of the dealer's cards is visible initially
3. On your turn, you can:
   - **Hit (H)**: Take another card
   - **Stand (S)**: Keep your current hand
4. If you go over 21, you "bust" and lose immediately
5. After you stand, the dealer reveals their hidden card and plays according to house rules
6. The highest hand under 21 wins

### Features
- Automatic Ace value adjustment (11 or 1)
- Deck reshuffling when empty
- Score tracking and winner determination
- Play again option
- Clear visual display of hands and scores

Enjoy playing! 🃏