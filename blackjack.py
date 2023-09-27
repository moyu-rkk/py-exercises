# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:30:33 2021

@author: robin
"""
import random

# 本次遇到的三类问题
# 1. if判断句多个or并列的问题
# 2. 判断句位置的问题（梳理并理解两个while loop的嵌套关系以后就能解决惹，还能删减重复命令）
# 3. 可能的情况考虑不全面的问题（穷举要细心惹）
#
# 功能应该是做齐了，目前也没出bug，就是码多了点丑了点- -
#
# += is shorthand for .extend(list) function which extend list by appending elements from the iterable
# you can't put an int in it while creating a list?string? for math calculating looks like it works


############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.
#
# ############## Our Blackjack House Rules #####################
#
# # The deck is unlimited in size.
# # There are no jokers.
# # The Jack/Queen/King all count as 10.
# # The Ace can count as 11 or 1.
# # Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


def hands(x):
    deck = []
    for i in range(x):
        deck.append(random.choice(cards))
    return deck


def update(card, a):
    card += hands(a)
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    score = sum(card)
    return card, score


def current_deck(player_deck, player_score, dealer_deck):
    current = f"  Your cards: {player_deck}, current score: {player_score}\n  Computer's first card: {dealer_deck[0]}\n"
    return current


def final_deck(player_deck, player_score, dealer_deck, dealer_score):
    final = f"  Your final hand: {player_deck}, final score: {player_score}\n" \
            f"  Computer's final hand: {dealer_deck}, final score: {dealer_score}\n"
    return final


def check(player_score, dealer_score):
    result = ''
    if player_score > 21 and dealer_score > 21:
        result = 0
    elif player_score > 21:
        result = 1
    elif dealer_score > 21:
        result = 2
    elif player_score == 21 and dealer_score == 21:
        result = 3
    elif player_score == 21:
        result = 4
    elif player_score > dealer_score:
        result = 5
    elif dealer_score == 21:
        result = 6
    elif dealer_score > player_score:
        result = 7
    elif player_score == dealer_score:
        result = 8

    # UnboundLocalError: local variable 'result' referenced before assignment
    # 说明你忘了考虑打平的情况，于是没有check到，于是result就没有被assign到
    # 为什么打平也要分两种情况：①一种都是21，强制终止游戏；②一种是玩家选择终止以后的结果
    return result


def display(num):
    result = ''
    if num == 0:
        result = "You both went off. Drew."
    elif num == 1:
        result = "You went off. You lose."
    elif num == 2:
        result = "Dealer went off. You win."
    elif num == 3 or num == 8:
        result = "Drew."
    elif num == 4 or num == 5:
        result = "You win."
    elif num == 6 or num == 7:
        result = "You lose."
    return result


def game():
    flag = True
    
    while flag:
        
        dealer_deck = hands(2)
        player_deck = hands(2)
        
        dealer_score = sum(dealer_deck)
        player_score = sum(player_deck)
        
        compare = check(player_score, dealer_score)
        
        print(current_deck(player_deck, player_score, dealer_deck))
        
        if compare == 0 or compare == 1 or compare == 2 or compare == 3 or compare == 4 or compare == 6:
            # 所以为什么这里不能偷懒，如果写x == 1 or 2这种句式就会失去判断作用
            print(final_deck(player_deck, player_score, dealer_deck, dealer_score))
            print(display(compare))
        else:
            draw = input("Type 'y' to get another card ,type 'n' to pass: ")
            if draw == 'n':
                if dealer_score < 17:
                    playernew = update(player_deck, 1)
                    player_deck = playernew[0]
                    player_score = playernew[1]
                    
                    dealernew = update(dealer_deck, 1)
                    dealer_deck = dealernew[0]
                    dealer_score = dealernew[1]
                    
                    compare = check(player_score, dealer_score)
                    
                    print(final_deck(player_deck, player_score, dealer_deck, dealer_score))
                    print(display(compare))
                else:
                    print(final_deck(player_deck, player_score, dealer_deck, dealer_score))
                    print(display(compare))
                
                # same problem here it only breaks the nested loop so if you choose not to play it still goes on
        
            while draw == 'y':
                playernew = update(player_deck, 1)
                player_deck = playernew[0]
                player_score = playernew[1]
                
                dealernew = update(dealer_deck, 1)
                dealer_deck = dealernew[0]
                dealer_score = dealernew[1]
                
                compare = check(player_score, dealer_score)
                
                if compare == 0 or compare == 1 or compare == 2 or compare == 3 or compare == 4 or compare == 6:
                    print(final_deck(player_deck, player_score, dealer_deck, dealer_score))
                    print(display(compare))
                    
                    break
              
# when you say a new game you mean break the nested while loop and go back to the big while loop
# or continue go on executing the nested loop
# that's the reason why you choose starting a new game
# it doesn't create new decks instead it keeps on going with the old decks
# 其实一开始就是这个问题，提升的点在于：①梳理清楚了9种比分情况；②abstract出有两个循环嵌套aka定位到了问题
              
                else:
                    print(current_deck(player_deck, player_score, dealer_deck))
                    
                draw = input("Type 'y' to get another card ,type 'n' to pass: ")
                    
                if draw == 'y':
                    continue
                elif draw == 'n':
                    if dealer_score < 17:
                        playernew = update(player_deck, 1)
                        player_deck = playernew[0]
                        player_score = playernew[1]
                        
                        dealernew = update(dealer_deck, 1)
                        dealer_deck = dealernew[0]
                        dealer_score = dealernew[1]
                        
                        compare = check(player_score, dealer_score)
                        
                        print(final_deck(player_deck, player_score, dealer_deck, dealer_score))
                        print(display(compare))
                        
                    else:
                        print(final_deck(player_deck, player_score, dealer_deck, dealer_score))
                        print(display(compare))
                    
                        break
                        
        new_game = input("\nDo you wanna play a game of Blackjack. Type 'y' or 'n'.\n")
            
        if new_game == 'y':
            continue
        elif new_game == 'n':
            flag = False


game()
