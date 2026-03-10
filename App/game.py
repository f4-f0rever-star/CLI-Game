from card_and_deck import Deck

class PokerGame:
    def __init__(self):
        self.deck = Deck()
        self.pot = 0
        self.community_cards = []

    def start_new_round(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.community_cards = []
        self.pot = 0

    def get_winner(self, player1, player2):
        player1_best = max([card.value for card in player1.hand])
        player2_best = max([card.value for card in player2.hand])

        if player1_best > player2_best:
            return player1
        elif player2_best > player1_best:
            return player2
        else:
            return None