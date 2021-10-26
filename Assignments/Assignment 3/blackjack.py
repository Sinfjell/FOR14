import random


def shuffledDeck():
    'returns shuffled deck'
    
    # suits is a set of 4 Unicode symbols: back spade and club,
    # and white diamond and heart 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    deck = []

    # create deck of 52 cards
    for suit in suits:
        for rank in ranks:             # card is the concatenation
            deck.append(rank+' '+suit) # of suit and rank

    # shuffle the deck and return
    random.shuffle(deck)
    return deck



def dealCard():
    
    return card



def total(hand):
 
    return result



def compareHands(house, player):
 


def blackjack():
 

    
if __name__ == '__main__':
    blackjack()