# The initiation of Bridge game.
# It requires 4 players, one of them is called the declarer.
# Every player gets 13 cards.

import random

def create_deck(rank, suit):
    '''(list, list) ->list
    uding two given lists, rank and suit create a list of card
    >>> shuffle(["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", 
    "King", "Ace"], ["Clubs", "Diamonds", "Hearts", "Spades"])
    ['2 of Clubs', '2 of Diamonds', '2 of Hearts', '2 of Spades', '3 of Clubs',
    '3 of Diamonds', '3 of Hearts', '3 of Spades', '4 of Clubs', '4 of Diamonds',
    '4 of Hearts', '4 of Spades', '5 of Clubs', '5 of Diamonds', '5 of Hearts',
    '5 of Spades', '6 of Clubs', '6 of Diamonds', '6 of Hearts', '6 of Spades',
    '7 of Clubs', '7 of Diamonds', '7 of Hearts', '7 of Spades', '8 of Clubs',
    '8 of Diamonds', '8 of Hearts', '8 of Spades', '9 of Clubs', '9 of Diamonds',
    '9 of Hearts', '9 of Spades', '10 of Clubs', '10 of Diamonds', '10 of Hearts',
    '10 of Spades', 'Jack of Clubs', 'Jack of Diamonds', 'Jack of Hearts',
    'Jack of Spades', 'Queen of Clubs', 'Queen of Diamonds', 'Queen of Hearts',
    'Queen of Spades', 'King of Clubs', 'King of Diamonds', 'King of Hearts',
    'King of Spades', 'Ace of Clubs', 'Ace of Diamonds', 'Ace of Hearts',
    'Ace of Spades']
    '''
    # creates a deck in the order given in docsting
    # if you swap these two for loops, still you'll have a sorted deck but
    # in diferent order. Try it and see the order
    deck = []
    for rank_item in rank:
        for suit_item in suit:
            deck.append(rank_item + " of " + suit_item)    
    return deck

def shuffle(deck):
    ''' (list) -> list
    shuffles the given deck
    >>> shuffle (['2 of Clubs', '2 of Diamonds', '2 of Hearts', '2 of Spades', '3 of Clubs',
    '3 of Diamonds', '3 of Hearts', '3 of Spades', '4 of Clubs', '4 of Diamonds',
    '4 of Hearts', '4 of Spades', '5 of Clubs', '5 of Diamonds', '5 of Hearts',
    '5 of Spades', '6 of Clubs', '6 of Diamonds', '6 of Hearts', '6 of Spades',
    '7 of Clubs', '7 of Diamonds', '7 of Hearts', '7 of Spades', '8 of Clubs',
    '8 of Diamonds', '8 of Hearts', '8 of Spades', '9 of Clubs', '9 of Diamonds',
    '9 of Hearts', '9 of Spades', '10 of Clubs', '10 of Diamonds', '10 of Hearts',
    '10 of Spades', 'Jack of Clubs', 'Jack of Diamonds', 'Jack of Hearts',
    'Jack of Spades', 'Queen of Clubs', 'Queen of Diamonds', 'Queen of Hearts',
    'Queen of Spades', 'King of Clubs', 'King of Diamonds', 'King of Hearts',
    'King of Spades', 'Ace of Clubs', 'Ace of Diamonds', 'Ace of Hearts',
    'Ace of Spades'])
    ['Ace of Hearts', 'Queen of Clubs', '6 of Spades', '9 of Hearts', 
    'Jack of Diamonds', '10 of Hearts', '5 of Diamonds', '6 of Hearts', 
    'Queen of Diamonds', '6 of Clubs', '4 of Spades', '9 of Clubs', 
    '4 of Hearts', '3 of Diamonds', 'King of Clubs', '5 of Clubs', '10 of Spades',
    'King of Diamonds', '2 of Clubs', '7 of Hearts', '8 of Clubs', 'Ace of Clubs',
    'Jack of Clubs', 'Ace of Spades', '2 of Diamonds', 'Jack of Spades', 
    'Ace of Diamonds', '3 of Spades', '2 of Spades', '9 of Diamonds', '3 of Clubs', 
    '7 of Spades', '2 of Hearts', '9 of Spades', '6 of Diamonds', 'Jack of Hearts',
    '3 of Hearts', 'Queen of Spades', '10 of Clubs', '5 of Spades', '7 of Diamonds', 
    '7 of Clubs', '5 of Hearts', '8 of Spades', '4 of Diamonds', 'King of Hearts',
    '10 of Diamonds', '8 of Hearts', 'Queen of Hearts', '4 of Clubs', 
    '8 of Diamonds', 'King of Spades']
    '''
    # shuffle the deck, do not use python's shuffle function
    # swap each item with a random item in the list
    for i in range(0, len(deck)):
        rand = random.randint(0, len(deck)-1)  # [0, 51]
        temp = deck[i]
        deck[i] = deck[rand]
        deck[rand] = temp
    return deck

def find_declarer(players, deck):
    '''(list, list) -> list
    declares who is the declarer by setting the item at an index to true.
    so if first player gets the ace of spade, player[0] is set to true and if 
    fourth player gets this card them player[3] is set to true.
    >>>find_declare([False, False, False, False], ['Ace of Hearts', 'Queen of Clubs', 
    '6 of Spades', '9 of Hearts', 'Jack of Diamonds', '10 of Hearts', '5 of Diamonds', '6 of Hearts', 
    'Queen of Diamonds', '6 of Clubs', '4 of Spades', '9 of Clubs', 
    '4 of Hearts', '3 of Diamonds', 'King of Clubs', '5 of Clubs', '10 of Spades',
    'King of Diamonds', '2 of Clubs', '7 of Hearts', '8 of Clubs', 'Ace of Clubs',
    'Jack of Clubs', 'Ace of Spades', '2 of Diamonds', 'Jack of Spades', 
    'Ace of Diamonds', '3 of Spades', '2 of Spades', '9 of Diamonds', '3 of Clubs', 
    '7 of Spades', '2 of Hearts', '9 of Spades', '6 of Diamonds', 'Jack of Hearts',
    '3 of Hearts', 'Queen of Spades', '10 of Clubs', '5 of Spades', '7 of Diamonds', 
    '7 of Clubs', '5 of Hearts', '8 of Spades', '4 of Diamonds', 'King of Hearts',
    '10 of Diamonds', '8 of Hearts', 'Queen of Hearts', '4 of Clubs', 
    '8 of Diamonds', 'King of Spades'])
    [False, False, False, True]
    '''
    # Declarer is the one who tells which suit is the trump.
    # For now, the person who gets ace of spades will be the declarer
    # players keep receiving a card one at a time, until one of them becomes
    # a declarer.
    # the first picked cards is for player_0, 2nd for player_1, 3rd for
    # player_2, 4th for player_3    
    
    
    ace_of_spades = 'Ace of Spades'
    players[deck.index(ace_of_spades)%4] = True
    return players

def deal(deck):
    player_1 = []
    player_2 = []
    player_3 = []
    player_4 = []
    for index in range (0, len(deck), 4):
        player_1.append(deck[index])
        player_2.append(deck[index+1])
        player_3.append(deck[index+2])
        player_4.append(deck[index+3])
    return ([player_1, player_2, player_3, player_4])
        
        
if (__name__ == "__main__"):
    # declare ranks and suits
    rank = ["2", "3", "4", "5", "6", "7", "8", "9",
            "10", "Jack", "Queen", "King", "Ace"]
    
    suit = ["Clubs", "Diamonds", "Hearts", "Spades"]    
    deck = create_deck(rank, suit)
    # shuffle the card to pick the declarer
    deck = shuffle(deck)
    players = [False, False, False, False]
    players = find_declarer(players, deck)
    # shuffle again for actual game
    deck = shuffle(deck)
    #each player should get a list of 13 cards.
    player_1 = deal(deck) [0]
    player_2 = deal(deck) [1]
    player_3 = deal(deck) [2]
    player_4 = deal(deck) [3]
    
    # deal the cards for each player
    print(player_1)
    print(player_2)
    print(player_3)
    print(player_4)
        
    
    

    







