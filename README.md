# Command-Line Blackjack Game

A simple Python implementation of the classic Blackjack card game for the command line.

## How to Use

### Prerequisites
- Python 3.6 or higher

### Installation & Running
1. Save all three files in the same directory:
   - `cards.py`
   - `game_logic.py` 
   - `blackjack.py`

2. Run the game:
   ```bash
   python blackjack.py
   ```

### Game Rules
- The goal is to get as close to 21 as possible without going over
- Number cards are worth their face value
- Face cards (Jack, Queen, King) are worth 10
- Aces are worth 11, but become 1 if the hand would otherwise bust
- Blackjack (Ace + 10-value card) pays immediately
- Dealer must hit until they reach 17 or higher

### Gameplay
1. The game starts by dealing two cards to both player and dealer
2. Only one of the dealer's cards is visible initially
3. On your turn, you can:
   - **Hit (h)**: Take another card
   - **Stand (s)**: Keep your current hand
4. If you go over 21, you bust and lose immediately
5. After you stand, the dealer reveals their hidden card and plays according to fixed rules
6. The highest hand under or equal to 21 wins

### Controls
- `h` or `H` - Hit (take another card)
- `s` or `S` - Stand (keep your current hand)
- `y` or `Y` - Play another game
- `n` or `N` - Quit the game

Enjoy playing Blackjack!