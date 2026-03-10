from card_and_deck import Card

class Player:
    def __init__(self, name, chips=1000):
        self.name = name
        self.chips = chips
        self.hand = []
        self.is_folded = False

    def bet(self, amount):
        if amount > self.chips:
            actual_bet = self.chips
            self.chips = 0
            return actual_bet
        else:
            self.chips -= amount
            return amount