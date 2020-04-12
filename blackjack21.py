"""
Assignment 5 Jose Guimaraes.

Blackjack # 21 Assignment.
This python program will use terminal or prompt to start a "21" game.

"""
import random
import sys
import os
import time

# creating deck of Cards
DECK_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4


def draw_cards(n_deal):
    '''
    Using random sample to draw cards from the deck and remove
    those from it. This function is used on start_deal(), hit_stand, game_score
    '''
    cards = []
    cards = random.sample(DECK_CARDS, n_deal)
    for i in cards:
        DECK_CARDS.remove(i)
    return cards


def sum_cards(cards):
    '''
    Check the card and add properly values of A, K, J AND Q to get hand sum.
    '''
    total = []
    for i in cards:
        if i in ('J', 'Q', 'K'):
            total.append(10)
        elif i == 'A'and sum(total) < 11:
            total.append(11)
        elif i == 'A'and sum(total) >= 11:
            total.append(1)
        else:
            total.append(i)
# If statment used when the dealt hand have more than 3 cards and Aces.
# Change Ace 11 Value to 1.
    if sum(total) > 21 and 11 in total:
        total.remove(11)
        total.append(1)
    return sum(total)


def clear():
    '''
    Funcion to clear prompt or terminal to have a better look on the screen.
    '''
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


def instructions_21():
    '''
    Game Instructions
    '''
    print('''Blackjack is a card game that pits player versus dealer. It is
played with one or more decks of cards. Cards are counted as their respective
numbers, face cards as ten, and ace as either eleven or one (in our game it
will show on the counter as an 11 unless you are over 21). The object of
Blackjack is the beat the dealer. This can be accomplished by getting Blackjack
(first two cards equal 21) without dealer Blackjack, having your final card
count be higher than the dealers without exceeding 21, or by not exceeding 21
and dealer busting by exceeding their card count of 21.

In Blackjack, or 21, the player must decide what to bet before the hand. Once
you click "deal" your bet is set, and two cards are dealt to the player face up
and two cards are dealt to the dealer, one face up and one face down. You must
then decide if you will "hit" (take another card from the deck) or "stand"
(keep the hand you are dealt).

Once the Blackjack hand is played out, three outcomes can occur. First you can
win (as previously described), secondly you can lose (bust hand or have less
than dealer hand), or you can push (have same hand - number count or Blackjack
- as dealer). If you win, you get your bet money back PLUS that same amount
from the dealer, YAY! If you win with Blackjack, you get your original bet back
PLUS you win 1.5 times your bet from the dealer, WOOHOO! If you lose, the
dealer takes your bet money. If you push, you keep your bet money but do not
win anything additional.
''')
    input('Hit enter to go back!')
    clear()
    main()


def prompt_hit(player_cards, dealer_cards):
    '''
    Prompt player to choose between hit or stay_stand.
    '''
    while True:
        hit_stand = input('''Do you want to hit or Stand?

    (Press any time "q" to quit)

    Enter "1" to hit or "2" to stand: ''')
        hit_stand = hit_stand.lower()
        clear()
        if hit_stand == '1':
            player_cards += draw_cards(1)
            game_score(player_cards, dealer_cards, hit_stand)
        elif hit_stand == '2':
            game_score(player_cards, dealer_cards, hit_stand)
        elif hit_stand == 'q':
            clear()
            print("THANK YOU TO PLAY BLACKJACK!")
            sys.exit()
        else:
            print('Try again!The options are "1" hit, "2" stay or "q" quit')
    return hit_stand


def game_score(player_cards, dealer_cards, hit_stand):
    '''
    Deal all dealer cards until sum equal 16.
    Checking card and prompt results.
    '''
    print(f'''Your hand is {player_cards}.Totalizing {sum_cards(player_cards)}
________________________________________________________________

And dealer knowing card is {dealer_cards[0]}

''')
    while sum_cards(dealer_cards) < 17 and hit_stand == '2':
        print(f'''Dealer Cards are {dealer_cards}.
        Dealer will dealt another cards! Wait and good lucky!!!!''')
        time.sleep(3)
        dealer_cards += draw_cards(1)
        print(f'Dealer cards now are {dealer_cards}')
        time.sleep(3)
    if sum_cards(player_cards) == 21 and sum_cards(dealer_cards) != 21:
        while sum_cards(dealer_cards) < 17:
            print(f'''Dealer Cards are {dealer_cards}.
            Dealer will dealt another cards! Wait and good lucky!!!!''')
            time.sleep(3)
            dealer_cards += draw_cards(1)
            print(f'Dealer cards now are {dealer_cards}')
            time.sleep(3)
        print(f'''YOU WIN! You got a blackjack {sum_cards(player_cards)}.
        Player hand {player_cards} || Dealer hand {dealer_cards} ''')
        play_again(player_cards, dealer_cards)
    elif sum_cards(player_cards) == 21 and sum_cards(dealer_cards) == 21:
        print(f'''Push! We are both with 21!
        Player hand {player_cards} || Dealer hand {dealer_cards}''')
        play_again(player_cards, dealer_cards)
    elif sum_cards(player_cards) > 21:
        print(f'''GONE BUST! YOU LOST!!
        Player hand {player_cards} || Dealer hand {dealer_cards[0:2]}''')
        play_again(player_cards, dealer_cards)
    elif sum_cards(dealer_cards) > 21 and hit_stand == '2':
        print(f'''DEALER GONE BUST! YOU WIN!
        Player hand {player_cards} || Dealer hand {dealer_cards}''')
        play_again(player_cards, dealer_cards)
    elif sum_cards(player_cards) < 22 and hit_stand != '2':
        prompt_hit(player_cards, dealer_cards)
    elif (sum_cards(player_cards) > sum_cards(dealer_cards)
          and hit_stand == '2'):
        print(f'''YOU WIN!
        Player hand {player_cards} || Dealer hand {dealer_cards}''')
        play_again(player_cards, dealer_cards)
    elif (sum_cards(player_cards) < sum_cards(dealer_cards)
          and hit_stand == '2'):
        print(f'''YOU LOST!
        Player hand {player_cards} || Dealer hand {dealer_cards}''')
        play_again(player_cards, dealer_cards)
    elif (sum_cards(player_cards) == sum_cards(dealer_cards)
          and hit_stand == '2'):
        print(f'''PUSH!
        Player hand {player_cards} || Dealer hand {dealer_cards}''')
        play_again(player_cards, dealer_cards)
    else:
        print('ERROR! Play again?')
        play_again(player_cards, dealer_cards)


def play_again(player_cards, dealer_cards):
    '''
    Return cards to deck and prompt user after win, lost or push if wants to
    play again.
    '''
    # Return cards to deck
    for i in player_cards + dealer_cards:
        DECK_CARDS.append(i)
    while True:
        player_choice = input('''
Do you want to play again?
Enter "y" yes or "q" to quit:  ''')
        player_choice = player_choice.lower()
        if player_choice == 'y':
            main()
        elif player_choice == 'q':
            clear()
            print("THANK YOU TO PLAY BLACKJACK!")
            sys.exit()
        else:
            print("Options are 'y' or 'q' Try again!")
            clear()


def start_deal():
    '''
    Initial dealt - define variable player and dealer cards and define the
    first knowning dealer card.
    Dealer_knowing is assigned as a variable to calculte properly 'A' Value.
    To propely assigned as "1" or "11" the 'A' string is
    removed form the list and appended at the end of the list.
    '''
    clear()
    hit_stand = '0'
    player_cards = draw_cards(2)
    dealer_cards = draw_cards(2)
    game_score(player_cards, dealer_cards, hit_stand)
    return player_cards, dealer_cards


def main():
    '''
    Ask player to start a game, check instructions or quit.
    When player call for a function to draw cards.
    '''
    clear()
    print('''___________________________________________________________________
Welcome to Blackjack! Also known to some as twenty-one, is one of
the most popular casino games around - and also super simple to learn!
______________________________________________________________________''')
    player_start = input('''
Enter "s" if you want to start a game, "i" for instructions or "q' quit: ''')
    player_start = player_start.lower()
    if player_start in ('start', 's'):
        start_deal()
    elif player_start == "i":
        instructions_21()
    elif player_start == "q":
        clear()
        print("THANK YOU TO PLAY BLACKJACK!")
        sys.exit()
    else:
        print('ERROR! Play again?')
        main()


if __name__ == '__main__':
    main()
