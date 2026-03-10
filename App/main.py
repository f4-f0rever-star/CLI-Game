import os
from card_and_deck import Deck
from game import PokerGame
from players import Player

def play():
    user = Player("Author", 1000)
    pc = Player("Computer", 1000)
    poker = PokerGame()

    print("Welcome to CLI Poker!")

    while user.chips > 0 and pc.chips > 0:
        poker.start_new_round()
        user.folded = False
        pc.folded = False

        user.hand = [poker.deck.deal(), poker.deck.deal()]
        pc.hand = [poker.deck.deal(), poker.deck.deal()]

        print(f"\n--- NEW ROUND ---")
        print(f"Your hand: {user.hand[0]}, {user.hand[1]}")

        choice = input("Bet Ksh 100 or Fold? (b/f): ")
        if choice == 'f':
            print("You folded!")
            pc.chips += 50 
            continue
        
        poker.pot += user.bet(100)
        poker.pot += pc.bet(100)

        for i in range(3):
            poker.community_cards.append(poker.deck.deal())
        
        print(f"Community: {[str(c) for c in poker.community_cards]}")
        
        print(f"PC Hand was: {pc.hand[0]}, {pc.hand[1]}")
        winner = poker.get_winner(user, pc)
        
        if winner == user:
            print(f"You won Ksh{poker.pot}!")
            user.chips += poker.pot
        elif winner == pc:
            print(f"PC won Ksh{poker.pot}!")
            pc.chips += poker.pot
        else:
            print("It's a tie! Pot split.")
            user.chips += poker.pot // 2
            pc.chips += poker.pot // 2

        print(f"Chips -> You: {user.chips}, PC: {pc.chips}")
        
        if input("Keep playing? (y/n): ") == 'n':
            break

if __name__ == "__main__":
    play()
