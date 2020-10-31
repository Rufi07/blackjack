import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}
# Chips = {'red': 50, 'white': 100, 'black': 500} ***do I really need this or does it make betting needlessly complicated***

#set playing to true so we can end the game later to create folding/ quitting functionality
playing = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


# build, shuffle and deal deck,
class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_composition= ''
        for card in self.deck:
            deck_composition += '\n' + card.__str__()
        return "The deck has " + deck_composition

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        one_card = self.deck.pop()
        return one_card


# tDeck = Deck()
# tDeck.shuffle()
# tDeck.__str__()


#hand will start empty and need to be filled from randomized deck. need value and a way to handlle ace vakue of 11 or 1
class Hand:
    def __init__(self):
       self.card = []
       self.value = 0

    def get_Card(self, card):
        self.card.append(card)
        if self.value > 10:
            values['ace'] =1
        self.value += values[card.rank]


#need a balance of money earned from betting, maybe use chips to bet to keep values consistent?
class Wallet:
    def __init__(self):
        self.total = 500
        self.bet = 0

    def loser(self):
        self.total -= self.bet

    def winner(self):
        self.total += self.bet

#betting based on Chips dictionary may be needlessly complicated.
# as long as bet< wallet bets should be accepted

def make_bet(wallet):
    while True:
        try:
            wallet.bet = int(input("How much would you like to bet? "))
        except ValueError:
            print("whoops, bet must be a whole number.")
        else:
            if wallet.bet > wallet.total:
                print("You can't play with money you don't have. Make a smaller bet.")

                # i want to create a way to replace bet if the bet is too large.




def hit(hand, deck):
    hand.get_Card(deck.deal())



while True:
    print("Welcome to Blackjack motherfucker!")

    game_deck = Deck()
    game_deck.shuffle()

    player1_hand = Hand()
    player1_hand.get_Card(game_deck.deal())
    player1_hand.get_Card(game_deck.deal())

    dealer_hand = Hand()
    dealer_hand.get_Card(game_deck.deal())
    dealer_hand.get_Card(game_deck.deal())
















