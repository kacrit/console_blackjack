# Command-Line Blackjack Game

A simple Python implementation of the classic Blackjack card game for the command line.

## How to Use

### Prerequisites
- Python 3.6 or higher

### Running the Game

1. **Save all files** in the same directory:
   - `cards.py`
   - `game_logic.py` 
   - `blackjack.py`

2. **Run the main game file**:
   ```bash
   python blackjack.py
   ```

### Game Rules

- The goal is to get a hand value as close to 21 as possible without exceeding it
- Number cards (2-10) are worth their face value
- Face cards (Jack, Queen, King) are worth 10 points
- Aces are worth 11 points, but can be reduced to 1 point if needed to avoid busting
- Blackjack (Ace + 10-value card) pays immediately
- Dealer must hit on 16 or less and stand on 17 or more

### Gameplay

1. The game starts by dealing 2 cards to both player and dealer
2. Only one of the dealer's cards is visible initially
3. On your turn, you can:
   - **Hit (H)**: Take another card
   - **Stand (S)**: Keep your current hand
4. If you go over 21, you bust and lose immediately
5. After you stand, the dealer reveals their hidden card and plays according to fixed rules
6. The highest hand under 21 wins

### Features

- Proper Ace value handling (11 or 1)
- Automatic deck reshuffling when empty
- Blackjack detection
- Bust detection
- Win/lose/push determination
- Clean command-line interface

Enjoy playing Blackjack!