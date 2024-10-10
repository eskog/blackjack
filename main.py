import random

class DeckOfCards:
    '''
    Simulates a deck of cards. Has methods for shuffeling the decks, and dealing out a single card.
    '''
    def __init__(self):
        self.cards = [2,3,4,5,6,7,8,9,10,10,10, 11] #Cards represented by their values, the 10s are JQK and 11 is Ace
        self.cards = self.cards * 4
        print(self.cards)

    def shuffle(self, times):
        for _ in range(times):
            random.shuffle(self.cards)

    def dealcard(self):
        return self.cards.pop()


class Player:
    '''
    PLayer object. Keeps track of dealt hand, its score and if the player is the dealer or not.
    '''
    score = 0
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.hand = []
        self.hiddencard = 0
    def add_score(self, card):
        if self.score + card > 21 and card == 11:
            self.score += 1
        else:
            self.score = self.score + card
    def get_score(self):
        self.reset_score()
        for card in self.hand:
            self.add_score(card)
        return self.score
    def reveal_hidden_card(self):
        self.add_score(self.hiddencard)
        print("Hidden card is {} and the dealers score is now {}".format(self.hiddencard, self.score))
        return self.hiddencard
    def read_cards(self):
        return self.hand
    def reset_score(self):
        self.score = 0

#game_setup will take the players and a deck of cards. shuffle and deal the initial cards
def game_setup(player, dealer, deck):
    print("Shuffling the cards")
    deck.shuffle(10)
    print("Dealing the cards")
    player.hand.append(deck.dealcard())
    dealer.hand.append(deck.dealcard())
    player.hand.append(deck.dealcard())
    dealer.hiddencard = deck.dealcard()

#Prints the score of the player and the dealer
def get_status(player, dealer):
    print("Player has {} for a value of {}".format(player.hand, player.get_score()))
    print("Dealers hand is {} for a value of {}".format(dealer.hand, dealer.get_score()))

#Logic for the players turn. Will give option to hit or stand. Will keep on until stand or bust.
def player_action(player, deck):
    while player.score <= 21:
        choice = input("[H]it or [S]tand?")
        if choice.lower() == 'h':
            card = deck.dealcard()
            player.hand.append(card)
            player.add_score(card)
            print("Current hand: {}, score {}".format(player.hand, player.score))
        if choice.lower() == 's':
            break
#Logic for the dealers turn. Will draw until score over 18.
def dealer_action(dealer, deck):
    dealer.reveal_hidden_card()
    while dealer.score < 18:
        card = deck.dealcard()
        dealer.hand.append(card)
        dealer.add_score(card)
        print("Dealer drew a {} and now has a score of {}".format(card, dealer.score))
def get_result(player, dealer):
    if player.score > 21:
        print("Player busted")
    elif player.score > dealer.score or dealer.score > 21:
        print("Player wins")
    else:
        print("Dealer wins!")


def __main__():
    player = Player()
    dealer = Player(dealer=True)
    deck = DeckOfCards()
    
    game_setup(player, dealer, deck)
    get_status(player, dealer)
    player_action(player, deck)
    get_status(player, dealer)
    dealer_action(dealer,deck)
    get_result(player,dealer)

    


        

if __name__ == "__main__":
    __main__()