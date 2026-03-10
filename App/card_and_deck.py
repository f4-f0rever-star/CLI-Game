import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
                      '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}[rank]

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        for s in suits:
            for r in ranks:
                new_card = Card(s, r)
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n=1):
        return self.cards.pop() 